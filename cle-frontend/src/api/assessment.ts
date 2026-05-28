import axios from "axios";
import { API_BASE_URL } from "./config";
import type { AssessmentRequest, AssessmentResponse } from "../types/assessment";

export async function assessLowBackPain(
  payload: AssessmentRequest
): Promise<AssessmentResponse> {
  const response = await axios.post(`${API_BASE_URL}/lbp-assessment`, payload);
  return response.data;
}
