import { useLocation, useNavigate } from "react-router-dom";
import type { AssessmentResponse } from "../types/assessment";

export default function ResultsPage() {
  const navigate = useNavigate();
  const location = useLocation();

  const result = location.state as AssessmentResponse | undefined;

  if (!result) {
    return (
      <div style={{ padding: "2rem" }}>
        <h1>No Results</h1>
        <p>No assessment data was provided.</p>
        <button onClick={() => navigate("/")}>Back to Assessment</button>
      </div>
    );
  }

  return (
    <div style={{ padding: "2rem", maxWidth: "900px" }}>
      <h1>Assessment Results</h1>

      {/* Summary */}
      <section style={{ marginBottom: "2rem" }}>
        <h2>Summary</h2>
        <p>{result.summary}</p>
      </section>

      {/* Red Flags */}
      <section style={{ marginBottom: "2rem" }}>
        <h2>Red Flags</h2>
        {result.red_flags.length === 0 ? (
          <p>No red flags detected.</p>
        ) : (
          <ul>
            {result.red_flags.map((rf, idx) => (
              <li key={idx}>{rf}</li>
            ))}
          </ul>
        )}
      </section>

      {/* Conditions */}
      <section style={{ marginBottom: "2rem" }}>
        <h2>Conditions</h2>

        {result.conditions.length === 0 ? (
          <p>No conditions identified.</p>
        ) : (
          result.conditions.map(cond => (
            <div
              key={cond.code}
              style={{
                border: "1px solid #ccc",
                padding: "1rem",
                marginBottom: "1rem",
                borderRadius: "6px"
              }}
            >
              <h3>{cond.name}</h3>
              <p>
                <strong>Likelihood:</strong> {cond.likelihood}
              </p>

              <p>
                <strong>Routing:</strong> {cond.routing.level} —{" "}
                {cond.routing.description}
              </p>

              <div>
                <strong>Reasons:</strong>
                <ul>
                  {cond.reasons.map((r, idx) => (
                    <li key={idx}>{r}</li>
                  ))}
                </ul>
              </div>
            </div>
          ))
        )}
      </section>

      {/* Reasoning Trace */}
      <section style={{ marginBottom: "2rem" }}>
        <h2>Reasoning Trace</h2>
        {result.reasoning_trace.length === 0 ? (
          <p>No reasoning trace provided.</p>
        ) : (
          <ol>
            {result.reasoning_trace.map((step, idx) => (
              <li key={idx}>{step}</li>
            ))}
          </ol>
        )}
      </section>

      {/* Question Explanations */}
      <section style={{ marginBottom: "2rem" }}>
        <h2>Question Explanations</h2>
        {Object.keys(result.question_explanations).length === 0 ? (
          <p>No explanations provided.</p>
        ) : (
          <ul>
            {Object.entries(result.question_explanations).map(
              ([key, explanation]) => (
                <li key={key}>
                  <strong>{key}:</strong> {explanation}
                </li>
              )
            )}
          </ul>
        )}
      </section>

      <button onClick={() => navigate("/")}>Back to Assessment</button>
    </div>
  );
}
