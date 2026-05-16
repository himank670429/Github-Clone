export * from "./authSuccessCodes";

import { AUTH_SUCCESS_CODES } from "./authSuccessCodes";

export const SUCCESS_CODES = {
    ...AUTH_SUCCESS_CODES,
} as const;

export type SuccessCode = keyof typeof SUCCESS_CODES;