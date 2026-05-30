import { useLocation, useNavigate } from "react-router-dom";
import { useState } from "react";

export default function ResultsPage() {
  const location = useLocation();
  const navigate = useNavigate();
  const result = location.state;

  const [showTrace, setShowTrace] = useState(false);

  if (!result) {
    return (
      <div style={{ padding: "2rem" }}>
        <h2>No results available</h2>
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

  // Clean routing: use engine's routing.description only
  const renderRouting = (routing: any) => {
    if (!routing) return null;

    const clean = routing.description?.replace(/^ROUTE:\s*/i, "") ?? "";
    return (
      <p>
        <strong>Recommended Action:</strong> {clean}
      </p>
    );
  };

  return (
    <div style={{ padding: "2rem", maxWidth: "900px", margin: "0 auto" }}>
      <h1>Assessment Results</h1>

      {/* SUMMARY */}
      <section style={{ marginBottom: "2rem" }}>
        <h2>Summary</h2>
        <p>{summary}</p>
      </section>

      {/* RED FLAGS */}
      <section style={{ marginBottom: "2rem" }}>
        <h2>Red Flags</h2>
        {red_flags.length === 0 ? (
          <p>No red flags detected.</p>
        ) : (
          <ul>
            {red_flags.map((rf: any, idx: number) => (
              <li key={idx} style={{ marginBottom: "0.5rem" }}>
                <strong>{rf.label}</strong>
                <div>{rf.reason}</div>
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
                borderRadius: "8px",
                background: "#fafafa"
              }}
            >
              <h3 style={{ marginTop: 0 }}>{cond.name}</h3>

              <p>
                <strong>Likelihood:</strong> {cond.likelihood ?? "unknown"}
              </p>

              {cond.reasons?.length > 0 && (
                <>
                  <strong>Reasons:</strong>
                  <ul>
                    {cond.reasons.map((r: string, i: number) => (
                      <li key={i}>{r}</li>
                    ))}
                  </ul>
                </>
              )}

              {renderRouting(cond.routing)}
            </div>
          ))
        )}
      </section>

      {/* REASONING TRACE */}
      <section style={{ marginBottom: "2rem" }}>
        <h2
          style={{ cursor: "pointer", userSelect: "none" }}
          onClick={() => setShowTrace(!showTrace)}
        >
          Clinical Reasoning Trace {showTrace ? "▲" : "▼"}
        </h2>

        {showTrace && (
          <div
            style={{
              maxHeight: "300px",
              overflowY: "auto",
              background: "#f0f0f0",
              padding: "1rem",
              borderRadius: "6px",
              fontFamily: "monospace",
              fontSize: "0.9rem",
              whiteSpace: "pre-wrap"
            }}
          >
            {reasoning_trace.length === 0 ? (
              <p>No reasoning trace available.</p>
            ) : (
              reasoning_trace.map((line: any, idx: number) => (
                <div key={idx}>• {line}</div>
              ))
            )}
          </div>
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
