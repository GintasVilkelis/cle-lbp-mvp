import { Routes, Route } from "react-router-dom";
import AssessmentForm from "./pages/AssessmentForm";
import ResultsPage from "./pages/ResultsPage";
import ConsumerQuestionPage from "./pages/ConsumerQuestionPage";

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<AssessmentForm />} />
      <Route path="/results" element={<ResultsPage />} />
      <Route path="/consumer" element={<ConsumerQuestionPage />} />
      <Route path="/patient-results" element={<ResultsPage />} />
    </Routes>
  );
}
