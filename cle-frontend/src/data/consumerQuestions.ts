import type { ConsumerQuestion } from "../types/questions";

export const CONSUMER_QUESTIONS: ConsumerQuestion[] = [
  {
    id: "age",
    title: "Your age",
    prompt: "How old are you?",
    how_to_answer:
      "Please enter your age in years. If you recently had a birthday, use your current age.",
    options: [],
    type: "number",
    maps_to: { section: "patient", field: "age" }
  },
  {
    id: "sex",
    title: "Your sex",
    prompt: "What is your biological sex?",
    how_to_answer:
      "Choose the option that best matches your biological sex, as this can influence certain medical risks.",
    options: [
      { value: "Male", label: "Male" },
      { value: "Female", label: "Female" },
      { value: "Other", label: "Other" }
    ],
    maps_to: { section: "patient", field: "sex" }
  },

  // Pain characteristics
  {
    id: "pain_duration",
    title: "How long have you had this back pain?",
    prompt: "When did this episode of back pain start?",
    how_to_answer:
      "Think about when this specific episode began. If the pain has been on and off, choose based on the most recent continuous period.",
    options: [
      { value: "< 6 weeks", label: "Less than 6 weeks" },
      { value: "6–12 weeks", label: "6–12 weeks" },
      { value: "> 12 weeks", label: "More than 12 weeks" }
    ],
    maps_to: { section: "pain", field: "duration" }
  },
  {
    id: "pain_onset",
    title: "How did the pain start?",
    prompt: "Did your back pain begin suddenly or gradually?",
    how_to_answer:
      "If the pain started during a specific moment (lifting, bending, twisting), choose 'Sudden'. If it built up over hours or days, choose 'Gradual'.",
    options: [
      { value: "Sudden", label: "Sudden" },
      { value: "Gradual", label: "Gradual" }
    ],
    maps_to: { section: "pain", field: "onset" }
  },
  {
    id: "pain_location",
    title: "Where is the pain located?",
    prompt: "Where do you feel the pain the most?",
    how_to_answer:
      "Choose the option that best matches where the pain is strongest. If it moves around, choose the most frequent location.",
    options: [
      { value: "Central", label: "Central (middle of the lower back)" },
      { value: "Left", label: "Left side" },
      { value: "Right", label: "Right side" }
    ],
    maps_to: { section: "pain", field: "location" }
  },

  // CES red flags
  {
    id: "urinary_retention",
    title: "Trouble starting urination",
    prompt: "Have you had difficulty starting to urinate or fully emptying your bladder?",
    how_to_answer:
      "Choose 'Yes' if you feel you cannot start urinating easily, or if your bladder feels full even after trying.",
    options: [
      { value: "Yes", label: "Yes" },
      { value: "No", label: "No" }
    ],
    maps_to: { section: "red_flags", field: "urinary_retention" }
  },
  {
    id: "urinary_incontinence",
    title: "Loss of bladder control",
    prompt: "Have you accidentally leaked urine or been unable to control your bladder?",
    how_to_answer:
      "Choose 'Yes' only if this is new or significantly worse than usual.",
    options: [
      { value: "Yes", label: "Yes" },
      { value: "No", label: "No" }
    ],
    maps_to: { section: "red_flags", field: "urinary_incontinence" }
  },
  {
    id: "bowel_incontinence",
    title: "Loss of bowel control",
    prompt: "Have you accidentally leaked stool or been unable to control your bowels?",
    how_to_answer:
      "Choose 'Yes' only if this is new or significantly worse than usual.",
    options: [
      { value: "Yes", label: "Yes" },
      { value: "No", label: "No" }
    ],
    maps_to: { section: "red_flags", field: "bowel_incontinence" }
  },
  {
    id: "saddle_anaesthesia",
    title: "Numbness in the groin area",
    prompt: "Have you felt numbness or unusual sensations around your groin, buttocks, or inner thighs?",
    how_to_answer:
      "This refers to the area that would touch a saddle when sitting on a bicycle. Choose 'Yes' if you have numbness, tingling, or reduced sensation there.",
    options: [
      { value: "Yes", label: "Yes" },
      { value: "No", label: "No" }
    ],
    maps_to: { section: "red_flags", field: "saddle_anaesthesia" }
  },
  {
    id: "bilateral_leg_weakness",
    title: "Weakness in both legs",
    prompt: "Have you noticed weakness in both legs at the same time?",
    how_to_answer:
      "Choose 'Yes' if both legs feel weaker than usual, especially when walking or standing.",
    options: [
      { value: "Yes", label: "Yes" },
      { value: "No", label: "No" }
    ],
    maps_to: { section: "red_flags", field: "bilateral_leg_weakness" }
  },
  {
    id: "progressive_leg_weakness",
    title: "Worsening leg weakness",
    prompt: "Has weakness in your legs been getting worse over hours or days?",
    how_to_answer:
      "Choose 'Yes' if you feel your legs are becoming progressively weaker over time.",
    options: [
      { value: "Yes", label: "Yes" },
      { value: "No", label: "No" }
    ],
    maps_to: { section: "red_flags", field: "progressive_leg_weakness" }
  },

  // Infection red flags
  {
    id: "fever",
    title: "Fever",
    prompt: "Have you had a fever recently?",
    how_to_answer:
      "Choose 'Yes' if your temperature has been above 38°C (100.4°F) or if you’ve felt unusually hot and sweaty.",
    options: [
      { value: "Yes", label: "Yes" },
      { value: "No", label: "No" }
    ],
    maps_to: { section: "red_flags", field: "fever" }
  },
  {
    id: "recent_infection",
    title: "Recent infection",
    prompt: "Have you had any recent infections (e.g., urinary, skin, chest)?",
    how_to_answer:
      "Choose 'Yes' if you were diagnosed with or treated for an infection in the last few weeks.",
    options: [
      { value: "Yes", label: "Yes" },
      { value: "No", label: "No" }
    ],
    maps_to: { section: "red_flags", field: "recent_infection" }
  },
  {
    id: "iv_drug_use",
    title: "IV drug use",
    prompt: "Do you use intravenous (injected) recreational drugs?",
    how_to_answer:
      "This information is confidential and only used for medical assessment. Choose 'Yes' if you have injected drugs recently.",
    options: [
      { value: "Yes", label: "Yes" },
      { value: "No", label: "No" }
    ],
    maps_to: { section: "red_flags", field: "IV_drug_use" }
  },
  {
    id: "immunosuppression",
    title: "Weakened immune system",
    prompt: "Do you have a weakened immune system?",
    how_to_answer:
      "Choose 'Yes' if you take steroids, chemotherapy, immunosuppressants, or have a condition affecting immunity.",
    options: [
      { value: "Yes", label: "Yes" },
      { value: "No", label: "No" }
    ],
    maps_to: { section: "red_flags", field: "immunosuppression" }
  },

  // Cancer red flags
  {
    id: "history_of_cancer",
    title: "History of cancer",
    prompt: "Have you ever been diagnosed with cancer?",
    how_to_answer:
      "Choose 'Yes' even if the cancer was treated successfully many years ago.",
    options: [
      { value: "Yes", label: "Yes" },
      { value: "No", label: "No" }
    ],
    maps_to: { section: "red_flags", field: "history_of_cancer" }
  },
  {
    id: "unexplained_weight_loss",
    title: "Unexplained weight loss",
    prompt: "Have you lost weight without trying in the last few months?",
    how_to_answer:
      "Choose 'Yes' if you lost more than 5% of your body weight unintentionally.",
    options: [
      { value: "Yes", label: "Yes" },
      { value: "No", label: "No" }
    ],
    maps_to: { section: "red_flags", field: "unexplained_weight_loss" }
  },
  {
    id: "night_pain",
    title: "Pain at night",
    prompt: "Does your back pain wake you up at night or prevent you from sleeping?",
    how_to_answer:
      "Choose 'Yes' if the pain wakes you up or keeps you awake on most nights.",
    options: [
      { value: "Yes", label: "Yes" },
      { value: "No", label: "No" }
    ],
    maps_to: { section: "red_flags", field: "night_pain" }
  },

  // Fracture red flags
  {
    id: "recent_trauma",
    title: "Recent trauma",
    prompt: "Have you had a fall, accident, or injury recently?",
    how_to_answer:
      "Choose 'Yes' if you fell, were hit, or had any event that could have strained your back.",
    options: [
      { value: "Yes", label: "Yes" },
      { value: "No", label: "No" }
    ],
    maps_to: { section: "red_flags", field: "recent_trauma" }
  },
  {
    id: "osteoporosis",
    title: "Osteoporosis",
    prompt: "Have you been diagnosed with osteoporosis?",
    how_to_answer:
      "Choose 'Yes' if a doctor has told you that you have osteoporosis or very low bone density.",
    options: [
      { value: "Yes", label: "Yes" },
      { value: "No", label: "No" }
    ],
    maps_to: { section: "red_flags", field: "osteoporosis" }
  },
  {
    id: "prolonged_steroid_use",
    title: "Long-term steroid use",
    prompt: "Have you taken steroid tablets for more than a few weeks?",
    how_to_answer:
      "Choose 'Yes' if you have taken oral steroids (like prednisolone) for more than 3 weeks.",
    options: [
      { value: "Yes", label: "Yes" },
      { value: "No", label: "No" }
    ],
    maps_to: { section: "red_flags", field: "prolonged_steroid_use" }
  },
  {
    id: "age_over_70",
    title: "Age over 70",
    prompt: "Are you over 70 years old?",
    how_to_answer:
      "Choose 'Yes' if you are 70 or older.",
    options: [
      { value: "Yes", label: "Yes" },
      { value: "No", label: "No" }
    ],
    maps_to: { section: "red_flags", field: "age_over_70" }
  }
];
