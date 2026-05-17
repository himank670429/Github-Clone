import { UITextInput, Text, Button, FormControl } from "@/ui-lib";
import { useFormik } from "formik";
import { loginValidationSchema } from "@/utils";
import { MarkGithubIcon } from "@primer/octicons-react";

interface SignupFormValues {
  username: string;
  password: string;
}

const initialValues: SignupFormValues = {
  username: "",
  password: "",
};

export function Signup() {
  /**
   * =====================================
   * hooks
   * =====================================
   */
  const formik = useFormik<SignupFormValues>({
    initialValues,
    validationSchema: loginValidationSchema,
    onSubmit: handleSubmit,
  });

  /**
   * =====================================
   * states
   * =====================================
   */
  const canSubmitForm = formik.isValid && formik.dirty;

  /**
   * =====================================
   * functions
   * =====================================
   */
  function handleSubmit(value: SignupFormValues) {
    console.log(value);
  }

  return (
    <div className="flex flex-col gap-4 items-center justify-center h-dvh grow">
      <MarkGithubIcon size={64} className="mb-1" />
      <Text className="text-2xl mb-5 font-semibold">
        Sign in to Github Clone
      </Text>

      <div className="flex flex-col gap-4 w-100">
        <UITextInput
          label="Username or email address"
          value={formik.values.username}
          onChange={formik.handleChange}
          inputMode="text"
          name="username"
          aria-required
          required
          onBlur={formik.handleBlur}
          error={formik.errors.username}
          touched={formik.touched.username}
        />

        <UITextInput
          label="Password"
          wrapperClassName="w-full"
          value={formik.values.password}
          onChange={formik.handleChange}
          inputMode="text"
          name="password"
          aria-required
          required
          onBlur={formik.handleBlur}
          error={formik.errors.password}
          touched={formik.touched.password}
          type="password"
        />

        <Button
          disabled={!canSubmitForm}
          variant={canSubmitForm ? "primary" : "default"}
          className="w-full py-4!"
          onClick={() => formik.handleSubmit()}
        >
          Sign In
        </Button>
      </div>

      <Text>
        New To Github Clone?{" "}
        <Button variant="link" className="font-normal!">
          Create an account
        </Button>
      </Text>
    </div>
  );
}
