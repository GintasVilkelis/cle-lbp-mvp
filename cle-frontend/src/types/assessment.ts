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
    urinary_retention: boolean;
    urinary_incontinence: boolean;
    bowel_incontinence: boolean;
    saddle_anaesthesia: boolean;
    bilateral_leg_weakness: boolean;
    progressive_leg_weakness: boolean;

    fever: boolean;
    recent_infection: boolean;
    IV_drug_use: boolean;
    immunosuppression: boolean;

    history_of_cancer: boolean;
    unexplained_weight_loss: boolean;
    night_pain: boolean;

    recent_trauma: boolean;
    osteoporosis: boolean;
    prolonged_steroid_use: boolean;
    age_over_70: boolean;
  };
}

export interface RedFlag {
  code: string;
  label: string;
  reason?: string;
}

export interface Condition {
  code: string;
  name: string;
  likelihood?: string;
  reasons?: string[];
  routing?: {
    level: string;
    description: string;
  };
  severity?: number;
  score?: number;
}

export interface AssessmentResponse {
  summary: string;
  red_flags: RedFlag[];
  conditions: Condition[];
  question_explanations: Record<string, any>;
  reasoning_trace: any[];
}
