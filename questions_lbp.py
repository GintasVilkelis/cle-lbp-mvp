# questions_lbp.py

QUESTION_DEFS = {

    # ----- Cauda Equina -----

    "urinary_retention": {
        "prompt_short": "Does the patient have urinary retention?",
        "prompt_explained": "Does the patient have urinary retention (difficulty passing urine, feeling of incomplete emptying)?",
        "explanation": "Urinary retention can indicate cauda equina syndrome, a medical emergency."
    },

    "urinary_incontinence": {
        "prompt_short": "Does the patient have urinary incontinence?",
        "prompt_explained": "Does the patient have urinary incontinence (loss of bladder control)?",
        "explanation": "Urinary incontinence can indicate cauda equina syndrome."
    },

    "saddle_anaesthesia": {
        "prompt_short": "Does the patient have saddle anaesthesia?",
        "prompt_explained": "Does the patient have saddle anaesthesia (numbness in the area that would touch a saddle)?",
        "explanation": "Saddle anaesthesia is a key sign of cauda equina syndrome."
    },

    "bowel_incontinence": {
        "prompt_short": "Does the patient have bowel incontinence?",
        "prompt_explained": "Does the patient have bowel incontinence (loss of control of bowel movements)?",
        "explanation": "Bowel incontinence is a red flag for cauda equina syndrome."
    },


    # ----- Neurological deficit -----

    "progressive_leg_weakness": {
        "prompt_short": "Is there progressive leg weakness?",
        "prompt_explained": "Is there progressive leg weakness (worsening weakness over hours or days)?",
        "explanation": "Progressive weakness may indicate serious neurological pathology."
    },

    "bilateral_leg_weakness": {
        "prompt_short": "Is there bilateral leg weakness?",
        "prompt_explained": "Is there weakness in both legs?",
        "explanation": "Bilateral weakness suggests central neurological involvement."
    },


    # ----- Infection -----

    "fever": {
        "prompt_short": "Does the patient have fever?",
        "prompt_explained": "Does the patient have fever (temperature above normal)?",
        "explanation": "Fever may indicate spinal infection."
    },

    "recent_infection": {
        "prompt_short": "Has the patient had a recent serious infection?",
        "prompt_explained": "Has the patient had a recent serious infection (e.g., urinary tract infection, skin infection)?",
        "explanation": "Recent infection increases risk of spinal infection."
    },

    "iv_drug_use": {
        "prompt_short": "Does the patient use intravenous drugs?",
        "prompt_explained": "Does the patient use intravenous drugs (injecting drugs into veins)?",
        "explanation": "IV drug use increases risk of spinal infection."
    },

    "immunosuppressed": {
        "prompt_short": "Is the patient immunosuppressed?",
        "prompt_explained": "Is the patient immunosuppressed (due to medication or illness)?",
        "explanation": "Immunosuppression increases risk of spinal infection."
    },

    "no_relief_when_lying_down": {
        "prompt_short": "Does the pain fail to improve when lying down?",
        "prompt_explained": "Does the pain fail to improve when lying down (pain remains or worsens at rest)?",
        "explanation": "Pain not improving when lying down is a red flag for infection or malignancy."
    },


    # ----- Malignancy -----

    "history_of_cancer": {
        "prompt_short": "Is there a history of cancer?",
        "prompt_explained": "Does the patient have a history of cancer?",
        "explanation": "History of cancer increases risk of spinal metastases."
    },

    "unexplained_weight_loss": {
        "prompt_short": "Is there unexplained weight loss?",
        "prompt_explained": "Has the patient had unexplained weight loss?",
        "explanation": "Unexplained weight loss may indicate malignancy."
    },


    # ----- Fracture -----

    "significant_trauma": {
        "prompt_short": "Has there been significant trauma?",
        "prompt_explained": "Has there been significant trauma (e.g., fall from height, car accident)?",
        "explanation": "Significant trauma increases risk of vertebral fracture."
    },

    "minor_trauma_osteoporosis": {
        "prompt_short": "Has there been minor trauma in a patient with osteoporosis?",
        "prompt_explained": "Has there been minor trauma in a patient with osteoporosis (e.g., simple fall)?",
        "explanation": "Minor trauma can cause fractures in osteoporotic patients."
    },

    "long_term_steroids": {
        "prompt_short": "Is the patient on long-term corticosteroids?",
        "prompt_explained": "Is the patient on long-term corticosteroids?",
        "explanation": "Long-term steroid use increases fracture risk."
    },


    # ----- Classification (radicular, inflammatory, serious) -----

    "leg_pain_worse_than_back": {
        "prompt_short": "Is leg pain worse than back pain?",
        "prompt_explained": "Is leg pain worse than back pain?",
        "explanation": "Leg-dominant pain suggests radicular pain."
    },

    "dermatomal_distribution": {
        "prompt_short": "Is the pain in a dermatomal distribution?",
        "prompt_explained": "Is the pain in a dermatomal distribution (following a nerve root)?",
        "explanation": "Dermatomal pain suggests nerve root involvement."
    },

    "positive_slr": {
        "prompt_short": "Is the straight-leg raise test positive?",
        "prompt_explained": "Is the straight-leg raise test positive?",
        "explanation": "Positive SLR suggests radicular pain."
    },

    "sensory_changes": {
        "prompt_short": "Are there sensory changes?",
        "prompt_explained": "Are there sensory changes (numbness, tingling) in a nerve-root pattern?",
        "explanation": "Sensory changes support radicular pain."
    },

    "motor_weakness_radicular": {
        "prompt_short": "Is there motor weakness in a nerve-root pattern?",
        "prompt_explained": "Is there motor weakness in a nerve-root pattern?",
        "explanation": "Motor weakness suggests nerve root compression."
    },

    "reflex_changes": {
        "prompt_short": "Are there reflex changes?",
        "prompt_explained": "Are there reflex changes (reduced ankle/knee reflexes)?",
        "explanation": "Reflex changes support radicular pain."
    },

    "night_pain": {
        "prompt_short": "Is there severe night pain?",
        "prompt_explained": "Is there severe night pain (pain waking the patient from sleep)?",
        "explanation": "Night pain may indicate serious pathology."
    },

    "pain_at_rest": {
        "prompt_short": "Is there pain at rest?",
        "prompt_explained": "Is there pain at rest (pain not related to movement)?",
        "explanation": "Pain at rest may indicate serious pathology."
    },

    "morning_stiffness": {
        "prompt_short": "Is there morning stiffness lasting > 30 minutes?",
        "prompt_explained": "Is there morning stiffness lasting more than 30 minutes?",
        "explanation": "Morning stiffness suggests inflammatory back pain."
    },

    "improves_with_exercise": {
        "prompt_short": "Does the pain improve with exercise?",
        "prompt_explained": "Does the pain improve with exercise?",
        "explanation": "Improvement with exercise suggests inflammatory back pain."
    },

    "worse_with_rest": {
        "prompt_short": "Is the pain worse with rest?",
        "prompt_explained": "Is the pain worse with rest?",
        "explanation": "Pain worse with rest suggests inflammatory back pain."
    },
}
