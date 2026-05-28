export interface AssessmentRequest {
  mode: string;
  patient: {
    age: number;
    sex: string;
  };
  pain: {
    duration: string;
    onset: string;
    location: string;
  };
  red_flags: {
    urinary_retention: string;
    urinary_incontinence: string;
    bowel_incontinence: string;
    saddle_anaesthesia: string;
    bilateral_leg_weakness: string;
    progressive_leg_weakness: string;

    fever: string;
    recent_infection: string;
    IV_drug_use: string;
    immunosuppression: string;

    history_of_cancer: string;
    unexplained_weight_loss: string;
    night_pain: string;

    recent_trauma: string;
    osteoporosis: string;
    prolonged_steroid_use: string;
    age_over_70: string;
  };
}

export interface ConditionOutput {
  code: string;
  name: string;
  likelihood: string;
  reasons: string[];
  routing: {
    level: string;
    description: string;
  };
}

export interface AssessmentResponse {
  summary: string;
  red_flags: any[];
  conditions: ConditionOutput[];
  reasoning_trace: string[];
  question_explanations: Record<string, string>;
}
