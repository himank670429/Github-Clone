import { API_URL } from "@/constants";
import { request } from "@/services/api/client/axios";
import type { APIResponse } from "@/services/api/contracts/api.contract";
import type {
  RegisterRequest,
  User,
} from "@/services/api/contracts/auth.contract";

export function registerUser(
  payload: RegisterRequest,
): Promise<APIResponse<User>> {
  return request<APIResponse<User>>({
    method: "POST",
    url: API_URL.auth.register,
    data: payload,
  });
}
