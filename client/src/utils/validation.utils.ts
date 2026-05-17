import * as Yup from 'yup';
import { getErrorMessage } from './message.utils';

export const loginValidationSchema = Yup.object().shape({
  username: Yup.string().required(getErrorMessage('EV-0001')),
  password: Yup.string().required(getErrorMessage('EV-0001')),
});