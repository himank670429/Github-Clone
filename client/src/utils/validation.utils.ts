import * as Yup from 'yup';
import { getErrorMessage } from './message.utils';

export const loginValidationSchema = Yup.object().shape({
  email: Yup.string().required("")
});