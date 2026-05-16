import {
  type ErrorCode,
  type SuccessCode,
  ERROR_CODES,
  SUCCESS_CODES,
} from "@/constants";


export const getErrorMessage = (code: ErrorCode): string => {
  return ERROR_CODES[code];
}

export const getSuccessMessage = (code: SuccessCode): string => {
  return SUCCESS_CODES[code];
}