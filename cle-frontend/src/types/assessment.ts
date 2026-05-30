// ---------------------------------------------------------
// INPUT MODEL (what the frontend sends to backend)
// ---------------------------------------------------------

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

    leg_pain_worse_than_back: boolean;
    dermatomal_distribution: boolean;
    positive_slr: boolean;
    sensory_changes: boolean;
    motor_weakness_radicular: boolean;
    reflex_changes: boolean;

    no_relief_when_lying_down: boolean;

    fever: boolean;
    recent_infection: boolean;
    iv_drug_use: boolean;
    immunosuppressed: boolean;

    history_of_cancer: boolean;
    unexplained_weight_loss: boolean;
    night_pain: boolean;
    pain_at_rest: boolean;

    significant_trauma: boolean;
    minor_trauma_osteoporosis: boolean;
    long_term_steroids: boolean;
  };
}

// ---------------------------------------------------------
// OUTPUT MODELS (what backend returns to frontend)
// ---------------------------------------------------------

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
