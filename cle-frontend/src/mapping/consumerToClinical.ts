import type { ConsumerQuestion } from "../types/questions";
import type { AssessmentRequest } from "../types/assessment";

/**
 * Convert Consumer Edition answers into the AssessmentRequest
 * expected by the backend NICE engine.
 */
export function mapConsumerAnswersToAssessment(
  answers: Record<string, string>,
  _questions: ConsumerQuestion[]
): AssessmentRequest {
  // Helper: convert "yes"/"no" → boolean
  const toBool = (v: string | undefined): boolean => {
    if (!v) return false;
    const s = v.trim().toLowerCase();
    return s === "yes" || s === "true";
  };

  // Extract values by question ID
  const get = (id: string): string | undefined => answers[id];

  // -------------------------------
  // PATIENT SECTION
  // -------------------------------
  const patient = {
    age: Number(get("age")) || 0,
    sex: get("sex") || "Other"
  };

  // -------------------------------
  // PAIN SECTION
  // -------------------------------
  const pain = {
    duration: get("pain_duration") || "< 6 weeks",
    onset: get("pain_onset") || "Gradual",
    location: get("pain_location") || "Central"
  };

  // -------------------------------
  // RED FLAGS SECTION
  // -------------------------------
  const red_flags = {
    urinary_retention: toBool(get("urinary_retention")),
    urinary_incontinence: toBool(get("urinary_incontinence")),
    bowel_incontinence: toBool(get("bowel_incontinence")),
    saddle_anaesthesia: toBool(get("saddle_anaesthesia")),
    bilateral_leg_weakness: toBool(get("bilateral_leg_weakness")),
    progressive_leg_weakness: toBool(get("progressive_leg_weakness")),

    fever: toBool(get("fever")),
    recent_infection: toBool(get("recent_infection")),
    IV_drug_use: toBool(get("IV_drug_use")),
    immunosuppression: toBool(get("immunosuppression")),

    history_of_cancer: toBool(get("history_of_cancer")),
    unexplained_weight_loss: toBool(get("unexplained_weight_loss")),
    night_pain: toBool(get("night_pain")),

    recent_trauma: toBool(get("recent_trauma")),
    osteoporosis: toBool(get("osteoporosis")),
    prolonged_steroid_use: toBool(get("prolonged_steroid_use")),
    age_over_70: toBool(get("age_over_70"))
  };

  // -------------------------------
  // FINAL STRUCTURE
  // -------------------------------
  const request: AssessmentRequest = {
    mode: "consumer",
    patient,
    pain,
    red_flags
  };

  return request;
}
