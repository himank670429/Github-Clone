export type ApiStatus = "success" | "error";

export interface APIResponse<TData> {
  status: ApiStatus;
  status_code: string;
  data: TData | null;
  message?: string;
}
