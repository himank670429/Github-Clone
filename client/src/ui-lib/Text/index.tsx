import {Text as PrimerText} from "@primer/react";

export function Text(props: React.ComponentProps<typeof PrimerText>) {
  return <PrimerText {...props} />;
}