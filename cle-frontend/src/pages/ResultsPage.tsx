import { useLocation, useNavigate } from "react-router-dom";

export default function ResultsPage() {
  const location = useLocation();
  const navigate = useNavigate();

  // The backend result is passed via React Router state
  const result = location.state;

  if (!result) {
    return (
      <div style={{ padding: "2rem" }}>
        <h2>No results available</h2>
        <p>The assessment did not return any data.</p>
        <button onClick={() => navigate("/")}>Start Again</button>
      </div>
    );
  }

  const {
    summary,
    red_flags = [],
    conditions = [],
    question_explanations = {},
    reasoning_trace = []
  } = result;

  return (
    <div style={{ padding: "2rem", maxWidth: "800px", margin: "0 auto" }}>
      <h1>Assessment Results</h1>

      {/* SUMMARY */}
      <section style={{ marginBottom: "2rem" }}>
        <h2>Summary</h2>
        <p>{summary || "No summary available."}</p>
      </section>

      {/* RED FLAGS */}
      <section style={{ marginBottom: "2rem" }}>
        <h2>Red Flags</h2>
        {red_flags.length === 0 ? (
          <p>No red flags detected.</p>
        ) : (
          <ul>
            {red_flags.map((rf: any, idx: number) => (
              <li key={idx}>
                <strong>{rf.label}</strong>
                {rf.reason && <p>{rf.reason}</p>}
              </li>
            ))}
          </ul>
        )}
      </section>

      {/* CONDITIONS */}
      <section style={{ marginBottom: "2rem" }}>
        <h2>Possible Conditions</h2>
        {conditions.length === 0 ? (
          <p>No conditions detected.</p>
        ) : (
          conditions.map((cond: any, idx: number) => (
            <div
              key={idx}
              style={{
                border: "1px solid #ccc",
                padding: "1rem",
                marginBottom: "1rem",
                borderRadius: "8px"
              }}
            >
              <h3>{cond.name}</h3>
              <p>
                <strong>Likelihood:</strong> {cond.likelihood || "unknown"}
              </p>

              {cond.reasons && cond.reasons.length > 0 && (
                <>
                  <strong>Reasons:</strong>
                  <ul>
                    {cond.reasons.map((r: string, i: number) => (
                      <li key={i}>{r}</li>
                    ))}
                  </ul>
                </>
              )}

              {cond.routing && (
                <>
                  <strong>Recommended Action:</strong>
                  <p>
                    {cond.routing.level}: {cond.routing.description}
                  </p>
                </>
              )}
            </div>
          ))
        )}
      </section>

      {/* REASONING TRACE */}
      <section style={{ marginBottom: "2rem" }}>
        <h2>Clinical Reasoning Trace</h2>
        {reasoning_trace.length === 0 ? (
          <p>No reasoning trace available.</p>
        ) : (
          <ul>
            {reasoning_trace.map((step: any, idx: number) => (
              <li key={idx}>{step}</li>
            ))}
          </ul>
        )}
      </section>

      {/* QUESTION EXPLANATIONS */}
      <section style={{ marginBottom: "2rem" }}>
        <h2>Question Explanations</h2>
        {Object.keys(question_explanations).length === 0 ? (
          <p>No explanations available.</p>
        ) : (
          <ul>
            {Object.entries(question_explanations).map(
              ([qid, explanation]: any) => (
                <li key={qid}>
                  <strong>{qid}:</strong> {explanation}
                </li>
              )
            )}
          </ul>
        )}
      </section>

      <button onClick={() => navigate("/")}>Start New Assessment</button>
    </div>
  );
}
