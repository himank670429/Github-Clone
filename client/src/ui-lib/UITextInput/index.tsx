import { FormControl, TextInput, type TextInputProps } from "@primer/react";

interface UITextInputProps extends TextInputProps {
  label: string;
  error?: string;
  touched?: boolean;
  required?: boolean;
  wrapperClassName?: string;
  labelClassName?: string;
}
export function UITextInput(props: UITextInputProps) {
  return (
    <FormControl className={props.wrapperClassName} required={props.required}>
      <FormControl.Label className={props.labelClassName}>
        {props.label}
      </FormControl.Label>
      <TextInput {...props} />
      {props.touched && props.error && (
        <FormControl.Validation variant="error">
          {props.error}
        </FormControl.Validation>
      )}
    </FormControl>
  );
}
