import { FormControl, TextInput as PrimerTextInput } from "@primer/react";

interface TextInputProps extends React.ComponentProps<typeof PrimerTextInput> {
    label?: string;
}

export function TextInput(props: TextInputProps) {
  const { label, ...rest } = props;
  return (
    <FormControl className="min-w-100">
      {label && <FormControl.Label>{label}</FormControl.Label>}
      <PrimerTextInput
        {...rest}
      />
    </FormControl>
  );
}
