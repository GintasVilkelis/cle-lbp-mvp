import { mapConsumerAnswersToAssessment } from "../mapping/consumerToClinical";
import { assessLowBackPain } from "../api/assessment";
import { CONSUMER_QUESTIONS } from "../data/consumerQuestions";
import type { ConsumerQuestion } from "../types/questions";

import { useState } from "react";
import { useNavigate } from "react-router-dom";

export default function ConsumerQuestionPage() {
  const navigate = useNavigate();
  const [currentIndex, setCurrentIndex] = useState(0);
  const [answers, setAnswers] = useState<Record<string, string>>({});

  const question: ConsumerQuestion | undefined =
    CONSUMER_QUESTIONS[currentIndex];

  if (!question) {
    const submit = async () => {
      const request = mapConsumerAnswersToAssessment(
        answers,
        CONSUMER_QUESTIONS
      );
      const result = await assessLowBackPain(request);
      navigate("/patient-results", { state: result });
    };

    return (
      <div style={{ padding: "2rem", maxWidth: "700px" }}>
        <h1>All questions completed</h1>
        <p>Click below to see your results.</p>
        <button onClick={submit}>See Results</button>
      </div>
    );
  }

  const handleAnswer = (value: string) => {
    setAnswers(prev => ({
      ...prev,
      [question.id]: value
    }));
  };

  const next = () => {
    setCurrentIndex(i => i + 1);
  };

  const prev = () => {
    setCurrentIndex(i => Math.max(0, i - 1));
  };

  return (
    <div style={{ padding: "2rem", maxWidth: "800px" }}>
      {/* Section 1: Question */}
      <section style={{ marginBottom: "1.5rem" }}>
        <h2>{question.title}</h2>
        <p>{question.prompt}</p>
      </section>

      {/* Section 2: How to answer accurately */}
      <section
        style={{
          marginBottom: "1.5rem",
          padding: "1rem",
          border: "1px solid #ddd",
          borderRadius: "6px",
          backgroundColor: "#f9f9f9"
        }}
      >
        <h3>How to answer this question</h3>
        <p>{question.how_to_answer}</p>
      </section>

      {/* Section 3: Answer input (multimedia-ready) */}
      <section style={{ marginBottom: "2rem" }}>
        {question.media && question.media.type === "image" && (
          <div style={{ marginBottom: "1rem" }}>
            <img
              src={question.media.url}
              alt={question.media.alt ?? ""}
              style={{ maxWidth: "100%" }}
            />
          </div>
        )}

        {/* For now: simple buttons for options */}
        <div>
          {question.options.map(opt => (
            <button
              key={opt.value}
              onClick={() => handleAnswer(opt.value)}
              style={{
                marginRight: "0.5rem",
                marginBottom: "0.5rem",
                padding: "0.5rem 1rem",
                border:
                  answers[question.id] === opt.value
                    ? "2px solid #007bff"
                    : "1px solid #ccc",
                borderRadius: "4px",
                backgroundColor:
                  answers[question.id] === opt.value ? "#e6f0ff" : "#fff",
                cursor: "pointer"
              }}
            >
              {opt.label}
            </button>
          ))}
        </div>
      </section>

      {/* Navigation */}
      <div style={{ display: "flex", justifyContent: "space-between" }}>
        <button onClick={prev} disabled={currentIndex === 0}>
          Previous
        </button>
        <button onClick={next} disabled={!answers[question.id]}>
          Next
        </button>
      </div>
    </div>
  );
}
