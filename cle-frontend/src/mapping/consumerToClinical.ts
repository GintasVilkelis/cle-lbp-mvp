import type { AssessmentRequest } from "../types/assessment";
import type { ConsumerQuestion } from "../types/questions";

export function mapConsumerAnswersToAssessment(
    answers: Record<string, any>,
    questions: ConsumerQuestion[]
): AssessmentRequest {
    // Start with default structure
    const result: AssessmentRequest = {
        mode: "teaching",
        patient: {
            age: 0,
            sex: "Other"
        },
        pain: {
            duration: "< 6 weeks",
            onset: "Gradual",
            location: "Central"
        },
        red_flags: {
            urinary_retention: "No",
            urinary_incontinence: "No",
            bowel_incontinence: "No",
            saddle_anaesthesia: "No",
            bilateral_leg_weakness: "No",
            progressive_leg_weakness: "No",

            fever: "No",
            recent_infection: "No",
            IV_drug_use: "No",
            immunosuppression: "No",

            history_of_cancer: "No",
            unexplained_weight_loss: "No",
            night_pain: "No",

            recent_trauma: "No",
            osteoporosis: "No",
            prolonged_steroid_use: "No",
            age_over_70: "No"
        }
    };

    // Apply mappings from each question
    for (const q of questions) {
        const answer = answers[q.id];
        if (answer === undefined) continue;

        if (q.maps_to) {
            const { section, field } = q.maps_to as {
                section: "patient" | "pain" | "red_flags";
                field: string;
            };

            if (section === "patient") {
                (result.patient as any)[field] = q.type === "number" ? Number(answer) : answer;
            } else if (section === "pain") {
                (result.pain as any)[field] = answer;
            } else if (section === "red_flags") {
                (result.red_flags as any)[field] = answer;
            }
        }
    }

    return result;
}
