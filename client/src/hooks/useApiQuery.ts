import { useQuery, type UseQueryOptions } from "@tanstack/react-query";
import type { APIResponse } from "@/services/api/contracts/api.contract";

export function useApiQuery<TData, TError = Error>(
  options: UseQueryOptions<APIResponse<TData>, TError, APIResponse<TData>>,
) {
  const query = useQuery(options);
  const response = query.data;

  return {
    ...query,
    data: response?.data,
    apiStatus: response?.status,
    statusCode: response?.status_code,
  };
}
