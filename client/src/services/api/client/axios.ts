import axios, { type AxiosRequestConfig } from "axios";

export const axiosClient = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || "http://localhost:8000",
  withCredentials: true,
  headers: {
    "Content-Type": "application/json",
  },
});

export async function request<TResponse>(
  config: AxiosRequestConfig,
): Promise<TResponse> {
  const response = await axiosClient.request<TResponse>(config);
  return response.data;
}
