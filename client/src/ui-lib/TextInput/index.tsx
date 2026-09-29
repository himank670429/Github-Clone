import { useState } from "react";
import { EyeClosedIcon, EyeIcon } from "@primer/octicons-react";
import {
  FormControl,
  IconButton,
  TextInput as PrimerTextInput,
} from "@primer/react";

interface TextInputProps extends React.ComponentProps<typeof PrimerTextInput> {
  label?: string;
  showPasswordToggle?: boolean;
}

export function TextInput(props: TextInputProps) {
  const { label, showPasswordToggle, type, trailingVisual, ...rest } = props;
  const [passwordVisible, setPasswordVisible] = useState(false);
  const canTogglePassword = showPasswordToggle && type === "password";

  return (
    <FormControl className="min-w-100">
      {label && <FormControl.Label>{label}</FormControl.Label>}
      <PrimerTextInput
        {...rest}
        type={canTogglePassword && passwordVisible ? "text" : type}
        trailingVisual={
          canTogglePassword ? (
            <IconButton
              aria-label={passwordVisible ? "Hide password" : "Show password"}
              icon={passwordVisible ? EyeClosedIcon : EyeIcon}
              onClick={() => setPasswordVisible((visible) => !visible)}
              size="small"
              type="button"
              variant="invisible"
            />
          ) : (
            trailingVisual
          )
        }
      />
    </FormControl>
  );
}
