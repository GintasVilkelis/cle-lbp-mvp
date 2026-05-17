import sys
from typing import Callable, Dict, Any, List

# =========================
# Core data structures
# =========================

State = Dict[str, Any]


class ReasoningLog:
    def __init__(self):
        self.entries: List[str] = []

    def add(self, message: str):
        self.entries.append(message)

    def show(self):
        print("\n=== REASONING LOG ===")
        for line in self.entries:
            print("- " + line)
        print("=====================\n")


class ClassificationResult:
    def __init__(self):
        self.categories: List[str] = []
        self.recommendations: List[str] = []

    def add_category(self, category: str):
        if category not in self.categories:
            self.categories.append(category)

    def add_recommendation(self, recommendation: str):
        if recommendation not in self.recommendations:
            self.recommendations.append(recommendation)

    def has_any_category(self) -> bool:
        return len(self.categories) > 0

    def show(self):
        print("\n=== RESULT ===")
        if self.categories:
            print("Categories:")
            for c in self.categories:
                print(f"  - {c}")
        else:
            print("Categories: none")

        if self.recommendations:
            print("Recommendations:")
            for r in self.recommendations:
                print(f"  - {r}")
        else:
            print("Recommendations: none")
        print("==============\n")


# =========================
# Rule engine
# =========================

class Rule:
    def __init__(self, name: str,
                 condition: Callable[[State, ClassificationResult], bool],
                 action: Callable[[State, ReasoningLog, ClassificationResult], None]):
        self.name = name
        self.condition = condition
        self.action = action

    def try_apply(self, state: State, log: ReasoningLog, result: ClassificationResult):
        if self.condition(state, result):
            log.add(f"Rule fired: {self.name}")
            self.action(state, log, result)


class Engine:
    def __init__(self, rules: List[Rule]):
        self.rules = rules

    def run(self, state: State) -> (ClassificationResult, ReasoningLog):
        log = ReasoningLog()
        result = ClassificationResult()

        log.add("Starting reasoning on state:")
        for k, v in state.items():
            log.add(f"  {k} = {v}")

        for rule in self.rules:
            rule.try_apply(state, log, result)

        if not result.categories:
            log.add("No non‑fallback classification rules fired.")
        return result, log


# =========================
# Helpers for rules
# =========================

def add_category(result: ClassificationResult, log: ReasoningLog, category: str):
    result.add_category(category)
    log.add(f"Added category: {category}")


def add_recommendation(result: ClassificationResult, log: ReasoningLog, recommendation: str):
    result.add_recommendation(recommendation)
    log.add(f"Added recommendation: {recommendation}")


# =========================
# LBP rules (red flags + fallback)
# =========================

def build_lbp_rules() -> List[Rule]:
    rules: List[Rule] = []

    # ===== Cauda equina red flags =====

    rules.append(
        Rule(
            name="red_flag_cauda_equina_urinary",
            condition=lambda s, res: (
                s.get("urinary_retention") is True
                or s.get("urinary_incontinence") is True
            ),
            action=lambda s, log, res: (
                add_category(res, log, "suspected_cauda_equina"),
                add_recommendation(res, log, "Emergency referral to hospital (suspected cauda equina syndrome)")
            )
        )
    )

    rules.append(
        Rule(
            name="red_flag_cauda_equina_saddle_anaesthesia",
            condition=lambda s, res: s.get("saddle_anaesthesia") is True,
            action=lambda s, log, res: (
                add_category(res, log, "suspected_cauda_equina"),
                add_recommendation(res, log, "Emergency referral to hospital (suspected cauda equina syndrome)")
            )
        )
    )

    rules.append(
        Rule(
            name="red_flag_cauda_equina_bowel_incontinence",
            condition=lambda s, res: s.get("bowel_incontinence") is True,
            action=lambda s, log, res: (
                add_category(res, log, "suspected_cauda_equina"),
                add_recommendation(res, log, "Emergency referral to hospital (suspected cauda equina syndrome)")
            )
        )
    )

    # ===== Severe / progressive neurological deficit =====

    rules.append(
        Rule(
            name="red_flag_neuro_progressive_or_bilateral_weakness",
            condition=lambda s, res: (
                s.get("progressive_leg_weakness") is True
                or s.get("bilateral_leg_weakness") is True
            ),
            action=lambda s, log, res: (
                add_category(res, log, "suspected_serious_neurological_pathology"),
                add_recommendation(res, log, "Urgent referral for specialist assessment / imaging")
            )
        )
    )

    # ===== Infection / systemic illness =====

    rules.append(
        Rule(
            name="red_flag_infection",
            condition=lambda s, res: (
                s.get("fever") is True
                or s.get("recent_infection") is True
                or s.get("iv_drug_use") is True
                or s.get("immunosuppressed") is True
                or s.get("no_relief_when_lying_down") is True
            ),
            action=lambda s, log, res: (
                add_category(res, log, "suspected_spinal_infection"),
                add_recommendation(res, log, "Urgent referral to hospital (possible spinal infection)")
            )
        )
    )

    # ===== Malignancy =====

    rules.append(
        Rule(
            name="red_flag_malignancy",
            condition=lambda s, res: (
                s.get("history_of_cancer") is True
                or s.get("unexplained_weight_loss") is True
                or s.get("no_relief_when_lying_down") is True
            ),
            action=lambda s, log, res: (
                add_category(res, log, "suspected_malignancy"),
                add_recommendation(res, log, "Urgent referral to rule out spinal malignancy")
            )
        )
    )

    # ===== Fracture risk =====

    rules.append(
        Rule(
            name="red_flag_fracture_trauma",
            condition=lambda s, res: (
                s.get("significant_trauma") is True
                or s.get("minor_trauma_osteoporosis") is True
            ),
            action=lambda s, log, res: (
                add_category(res, log, "suspected_vertebral_fracture"),
                add_recommendation(res, log, "Urgent imaging to exclude vertebral fracture")
            )
        )
    )

    rules.append(
        Rule(
            name="red_flag_fracture_age_steroids",
            condition=lambda s, res: (
                (s.get("age") is not None and s.get("age") >= 70)
                or s.get("long_term_steroids") is True
            ),
            action=lambda s, log, res: (
                add_category(res, log, "increased_fracture_risk"),
                add_recommendation(res, log, "Consider imaging / specialist assessment for possible fracture")
            )
        )
    )

    rules.append(
        Rule(
            name="classification_radicular_pain",
            condition=lambda s, res: (
                s.get("leg_pain_worse_than_back") is True
                or s.get("dermatomal_distribution") is True
                or s.get("positive_slr") is True
                or s.get("sensory_changes") is True
                or s.get("motor_weakness_radicular") is True
                or s.get("reflex_changes") is True
            ),
            action=lambda s, log, res: (
                add_category(res, log, "radicular_pain"),
                add_recommendation(res, log, "Consider conservative management, physiotherapy, and safety‑netting; refer if persistent or worsening")
            )
        )
    )

    rules.append(
        Rule(
            name="classification_inflammatory_back_pain",
            condition=lambda s, res: (
                s.get("morning_stiffness") is True
                or s.get("improves_with_exercise") is True
                or s.get("worse_with_rest") is True
            ),
            action=lambda s, log, res: (
                add_category(res, log, "possible_inflammatory_back_pain"),
                add_recommendation(res, log, "Consider rheumatology referral if persistent")
            )
        )
    )

    rules.append(
        Rule(
            name="classification_serious_non_red_flag",
            condition=lambda s, res: (
                s.get("night_pain") is True
                or s.get("pain_at_rest") is True
            ),
            action=lambda s, log, res: (
                add_category(res, log, "possible_serious_pathology"),
                add_recommendation(res, log, "Consider urgent imaging or specialist assessment")
            )
        )
    )

    # ===== Routing based on classifications =====
    rules.append(
        Rule(
            name="routing_emergency",
            condition=lambda s, res: "suspected_cauda_equina" in res.categories,
            action=lambda s, log, res: (
                add_recommendation(res, log, "ROUTE: Emergency referral to hospital")
            )
        )
    )

    rules.append(
        Rule(
            name="routing_urgent",
            condition=lambda s, res: any(cat in res.categories for cat in [
                "suspected_spinal_infection",
                "suspected_malignancy",
                "suspected_serious_neurological_pathology",
                "suspected_vertebral_fracture"
            ]),
            action=lambda s, log, res: (
                add_recommendation(res, log, "ROUTE: Urgent referral")
            )
        )
    )

    rules.append(
        Rule(
            name="routing_primary_care",
            condition=lambda s, res: any(cat in res.categories for cat in [
                "radicular_pain",
                "possible_inflammatory_back_pain"
            ]),
            action=lambda s, log, res: (
                add_recommendation(res, log, "ROUTE: Primary care management with safety‑netting")
            )
        )
    )


    # ===== Fallback: likely mechanical LBP =====
    # Only fires if no other categories were added.

    rules.append(
        Rule(
            name="fallback_mechanical_lbp",
            condition=lambda s, res: not res.has_any_category(),
            action=lambda s, log, res: (
                add_category(res, log, "likely_mechanical_lbp"),
                add_recommendation(res, log, "Conservative management and safety‑netting")
            )
        )
    )

    return rules


# =========================
# Input modes
# =========================
# So the correct insertion point is:
# ✔ Place the import (QUESTION_DEFS) at the top of the file, with the other imports 
# ✔ Place ask_question() immediately after ask_bool() 
# ✔ Place interactive_input() AFTER ask_question()

def ask_bool(prompt: str) -> bool:
    while True:
        ans = input(prompt + " (y/n): ").strip().lower()
        if ans in ["y", "yes"]:
            return True
        if ans in ["n", "no"]:
            return False
        print("Please answer y or n.")

from questions_lbp import QUESTION_DEFS

def ask_question(key: str, teaching: bool) -> bool:
        q = QUESTION_DEFS[key]
        prompt = q["prompt_explained"] if teaching else q["prompt_short"]
        return ask_bool(prompt)

def ask_int(prompt: str) -> int:
    while True:
        ans = input(prompt + " (number): ").strip()
        try:
            return int(ans)
        except ValueError:
            print("Please enter a valid integer.")


def interactive_input(teaching: bool) -> State:
    print("\n=== INTERACTIVE MODE (LBP) ===")
    state: State = {}

    # Red flags for cauda equina syndrome    
    state["urinary_retention"] = ask_question("urinary_retention", teaching)
    state["urinary_incontinence"] = ask_question("urinary_incontinence", teaching)
    state["saddle_anaesthesia"] = ask_question("saddle_anaesthesia", teaching)

    # Continue replacing all ask_bool(...) calls with ask_question(...)
    # For questions not yet in QUESTION_DEFS, keep ask_bool temporarily.
    state["bowel_incontinence"] = ask_question("bowel_incontinence", teaching)
    
    # Red flags for severe/progressive neurological deficit
    state["progressive_leg_weakness"] = ask_question("progressive_leg_weakness", teaching)
    state["bilateral_leg_weakness"] = ask_question("bilateral_leg_weakness", teaching)

    # Red flags for infection/systemic illness
    state["no_relief_when_lying_down"] = ask_question("no_relief_when_lying_down", teaching)
    state["fever"] = ask_question("fever", teaching)
    state["recent_infection"] = ask_question("recent_infection", teaching)
    state["iv_drug_use"] = ask_question("iv_drug_use", teaching)
    state["immunosuppressed"] = ask_question("immunosuppressed", teaching)

    # Red flags for malignancy
    state["history_of_cancer"] = ask_question("history_of_cancer", teaching)
    state["unexplained_weight_loss"] = ask_question("unexplained_weight_loss", teaching)

    # Red flags for fracture risk
    state["significant_trauma"] = ask_question("significant_trauma", teaching)
    state["minor_trauma_osteoporosis"] = ask_question("minor_trauma_osteoporosis", teaching)
    state["long_term_steroids"] = ask_question("long_term_steroids", teaching)
    state["age"] = ask_int("What is the patient's age?")

    # Additional clinical features (not currently used in rules, but could be in future iterations)
    state["leg_pain_worse_than_back"] = ask_question("leg_pain_worse_than_back", teaching)
    state["dermatomal_distribution"] = ask_question("dermatomal_distribution", teaching)
    state["positive_slr"] = ask_question("positive_slr", teaching)
    state["sensory_changes"] = ask_question("sensory_changes", teaching)
    state["motor_weakness_radicular"] = ask_question("motor_weakness_radicular", teaching)
    state["reflex_changes"] = ask_question("reflex_changes", teaching)
    state["night_pain"] = ask_question("night_pain", teaching)
    state["pain_at_rest"] = ask_question("pain_at_rest", teaching)
    state["morning_stiffness"] = ask_question("morning_stiffness", teaching)
    state["improves_with_exercise"] = ask_question("improves_with_exercise", teaching)
    state["worse_with_rest"] = ask_question("worse_with_rest", teaching)

    return state


def batch_input() -> State:
    print("\n=== BATCH MODE (LBP) ===")
    print("Enter key=value pairs, one per line. Empty line to finish.")
    print("Example: urinary_retention=yes")

    state: State = {}

    while True:
        line = input("> ").strip()
        if line == "":
            break
        if "=" not in line:
            print("Please use key=value format.")
            continue
        key, value = [x.strip() for x in line.split("=", 1)]
        if value.lower() in ["yes", "y", "true"]:
            state[key] = True
        elif value.lower() in ["no", "n", "false"]:
            state[key] = False
        else:
            try:
                state[key] = int(value)
            except ValueError:
                state[key] = value

    return state


# =========================
# Menu / main loop
# =========================

def main_menu():
    rules = build_lbp_rules()
    engine = Engine(rules)

    while True:
        print("=== CLE LBP MVP ===")
        print("1. Run interactive case with medical explanations (teaching mode)")
        print("2. Run interactive case without explanations (professional mode)")
        print("3. Run batch case")
        print("4. Exit")

        choice = input("Choose an option (1–4): ").strip()

        if choice == "1":
            state = interactive_input(teaching=True)
            result, log = engine.run(state)
            result.show()
            log.show()

        elif choice == "2":
            state = interactive_input(teaching=False)
            result, log = engine.run(state)
            result.show()
            log.show()

        elif choice == "3":
            state = batch_input()
            result, log = engine.run(state)
            result.show()
            log.show()

        elif choice == "4":
            print("Goodbye.")
            sys.exit(0)

        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")

# =========================
# API entry point for Streamlit / FastAPI
# =========================

def run_lbp_engine(input_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Main entry point for the NICE LBP engine when called programmatically
    (e.g., from Streamlit or FastAPI).

    input_data: {
        "mode": "teaching" | "pro",
        "patient": {...},
        "pain": {...},
        "red_flags": {...}
    }

    Returns a JSON friendly dict with:
        - summary
        - red_flags (list)
        - conditions (list)
        - question_explanations (optional)
        - reasoning_trace (list)
    """

    # 1. Convert UI payload → internal state format used by rules
    state: State = {}

    # Patient info
    state["age"] = input_data["patient"].get("age")

    # Pain characteristics (not yet used in rules, but included for future expansion)
    state["pain_duration"] = input_data["pain"].get("duration")
    state["pain_onset"] = input_data["pain"].get("onset")
    state["pain_location"] = input_data["pain"].get("location")

    # Red flags (convert "Yes"/"No" → True/False)
    rf = input_data["red_flags"]
    def yn(x): return True if x == "Yes" else False

    state.update({
        "urinary_retention": yn(rf.get("urinary_retention", "No")),
        "urinary_incontinence": yn(rf.get("urinary_incontinence", "No")),
        "saddle_anaesthesia": yn(rf.get("saddle_anaesthesia", "No")),
        "bowel_incontinence": yn(rf.get("bowel_incontinence", "No")),
        "progressive_leg_weakness": yn(rf.get("neuro_deficit", "No")),
        "bilateral_leg_weakness": False,  # UI does not yet collect this
        "no_relief_when_lying_down": yn(rf.get("night_pain", "No")),
        "fever": yn(rf.get("infection_signs", "No")),
        "recent_infection": yn(rf.get("infection_signs", "No")),
        "iv_drug_use": yn(rf.get("iv_drug_use", "No")),
        "immunosuppressed": yn(rf.get("immunosuppression", "No")),
        "history_of_cancer": yn(rf.get("cancer_history", "No")),
        "unexplained_weight_loss": yn(rf.get("weight_loss", "No")),
        "significant_trauma": yn(rf.get("recent_trauma", "No")),
        "minor_trauma_osteoporosis": yn(rf.get("minor_trauma_elderly", "No")),
        "long_term_steroids": yn(rf.get("steroid_use", "No")),
        "night_pain": yn(rf.get("night_pain", "No")),
        "pain_at_rest": yn(rf.get("night_pain", "No")),
    })

    # 2. Build and run the rule engine
    rules = build_lbp_rules()
    engine = Engine(rules)
    result, log = engine.run(state)

    # 3. Convert rule engine output → JSON friendly format
    red_flags_output = []
    for cat in result.categories:
        if "cauda_equina" in cat:
            red_flags_output.append({
                "code": "RF_CES",
                "label": "Suspected cauda equina syndrome",
                "reason": "One or more CES red flags present"
            })
        if "infection" in cat:
            red_flags_output.append({
                "code": "RF_INFECTION",
                "label": "Possible spinal infection",
                "reason": "Infection/systemic red flags present"
            })
        if "malignancy" in cat:
            red_flags_output.append({
                "code": "RF_MALIGNANCY",
                "label": "Possible spinal malignancy",
                "reason": "Malignancy red flags present"
            })
        if "fracture" in cat:
            red_flags_output.append({
                "code": "RF_FRACTURE",
                "label": "Possible vertebral fracture",
                "reason": "Fracture risk factors present"
            })

    # 4. Build conditions list
    conditions_output = []
    for cat in result.categories:
        conditions_output.append({
            "code": cat,
            "name": cat.replace("_", " ").title(),
            "likelihood": "high",
            "reasons": [cat],
            "routing": {
                "level": "urgent_care" if "suspected" in cat else "primary_care",
                "description": result.recommendations[-1] if result.recommendations else ""
            }
        })

    # 5. Build summary
    summary = (
        "Red flags detected — urgent assessment recommended."
        if red_flags_output else
        "No red flags detected."
    )

    # 6. Build reasoning trace
    reasoning_trace = log.entries

    # 7. Explanation mode
    question_explanations = None
    if input_data["mode"] == "teaching":
        question_explanations = {
            "infection_signs": "Fever, recent infection, IV drug use, or immunosuppression raise suspicion for spinal infection.",
            "cancer_history": "History of cancer or weight loss raises suspicion for malignancy.",
            "night_pain": "Night pain or pain at rest may indicate serious pathology.",
            "recent_trauma": "Trauma increases risk of vertebral fracture.",
            "bladder_bowel": "Bladder/bowel dysfunction suggests possible cauda equina syndrome."
        }

    # 8. Final output
    return {
        "summary": summary,
        "red_flags": red_flags_output,
        "conditions": conditions_output,
        "question_explanations": question_explanations,
        "reasoning_trace": reasoning_trace
    }


if __name__ == "__main__":
    main_menu()
