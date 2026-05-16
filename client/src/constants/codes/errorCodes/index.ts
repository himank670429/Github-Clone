export * from './validationErrorCodes';
export * from './authErrorCodes';

import { AUTH_ERROR_CODES } from './authErrorCodes';
import { VALIDATION_ERROR_CODES } from './validationErrorCodes';

export const ERROR_CODES = {
    ...AUTH_ERROR_CODES,
    ...VALIDATION_ERROR_CODES,
} as const;

export type ErrorCode = keyof typeof ERROR_CODES;