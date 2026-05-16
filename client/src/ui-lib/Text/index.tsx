import React from "react";

interface TextProps extends React.HTMLAttributes<HTMLParagraphElement> {}
export function Text(props: TextProps) {
  const { children, ...rest } = props;
  return <p {...rest}>{children}</p>;
}
