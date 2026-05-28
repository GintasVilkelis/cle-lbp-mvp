import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { assessLowBackPain } from "../api/assessment";
import type { AssessmentRequest } from "../types/assessment";
import { RED_FLAG_QUESTIONS } from "../data/redFlagQuestions";

export default function AssessmentForm() {
  const navigate = useNavigate();

  const [form, setForm] = useState<AssessmentRequest>({
    mode: "teaching",
    patient: {
      age: 45,
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
  });

  const update = (
    section: "patient" | "pain" | "red_flags",
    field: string,
    value: any
  ) => {
    setForm(prev => ({
      ...prev,
      [section]: {
        ...prev[section],
        [field]: value
      }
    }));
  };

  const submit = async () => {
    try {
      const result = await assessLowBackPain(form);
      navigate("/results", { state: result });
    } catch (err) {
      console.error("Assessment failed:", err);
      alert("Error contacting backend");
    }
  };

  return (
    <div style={{ padding: "2rem", maxWidth: "700px" }}>
      <h1>Low Back Pain Assessment</h1>

      {/* Patient Section */}
      <section style={{ marginBottom: "2rem" }}>
        <h2>Patient</h2>

        <label>Age:</label>
        <input
          type="number"
          value={form.patient.age}
          onChange={e => update("patient", "age", Number(e.target.value))}
        />

        <label>Sex:</label>
        <select
          value={form.patient.sex}
          onChange={e => update("patient", "sex", e.target.value)}
        >
          <option value="Male">Male</option>
          <option value="Female">Female</option>
          <option value="Other">Other</option>
        </select>
      </section>

      {/* Pain Section */}
      <section style={{ marginBottom: "2rem" }}>
        <h2>Pain</h2>

        <label>Duration:</label>
        <select
          value={form.pain.duration}
          onChange={e => update("pain", "duration", e.target.value)}
        >
          <option value="< 6 weeks">&lt; 6 weeks</option>
          <option value="6–12 weeks">6–12 weeks</option>
          <option value="> 12 weeks">&gt; 12 weeks</option>
        </select>

        <label>Onset:</label>
        <select
          value={form.pain.onset}
          onChange={e => update("pain", "onset", e.target.value)}
        >
          <option value="Gradual">Gradual</option>
          <option value="Sudden">Sudden</option>
        </select>

        <label>Location:</label>
        <select
          value={form.pain.location}
          onChange={e => update("pain", "location", e.target.value)}
        >
          <option value="Central">Central</option>
          <option value="Left">Left</option>
          <option value="Right">Right</option>
        </select>
      </section>

      {/* Red Flags Section */}
      <section>
        <h2>Red Flags</h2>

        {RED_FLAG_QUESTIONS.map(group => (
          <div
            key={group.group}
            style={{
              border: "1px solid #ccc",
              padding: "1rem",
              marginBottom: "1rem",
              borderRadius: "6px"
            }}
          >
            <h3>{group.group}</h3>

            {group.fields.map(field => (
              <div key={field.key} style={{ marginBottom: "0.5rem" }}>
                <label>{field.label}: </label>
                <select
                value={form.red_flags[field.key as keyof AssessmentRequest["red_flags"]]}
                onChange={e =>
                    update("red_flags", field.key, e.target.value)
                }
                >
                  <option value="No">No</option>
                  <option value="Yes">Yes</option>
                </select>
              </div>
            ))}
          </div>
        ))}
      </section>

      <button onClick={submit} style={{ marginTop: "1rem" }}>
        Submit Assessment
      </button>
    </div>
  );
}
