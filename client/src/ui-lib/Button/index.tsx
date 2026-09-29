import { Button as PrimerButton } from "@primer/react";

export function Button(props: React.ComponentProps<typeof PrimerButton>) {
  return <PrimerButton {...props} />;
}