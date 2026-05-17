import { FormControl, Text, TextInput, Button } from "@/ui-lib";
import { useFormik } from "formik";
import { loginValidationSchema } from "@/utils";
import { MarkGithubIcon } from "@primer/octicons-react";
import { Link } from "react-router-dom";
import { Routes } from "@/routes/Routes";
interface LoginFormValues {
  username: string;
  password: string;
}

const initialValues: LoginFormValues = {
  username: "",
  password: "",
};

export function Login() {

  /**
   * =====================================
   * hooks
   * =====================================
   */
  const formik = useFormik<LoginFormValues>({
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
  function handleSubmit(value: LoginFormValues) {
    console.log(value);
  }



  return (
    <div className="flex flex-col gap-4 items-center justify-center h-dvh grow">
      <MarkGithubIcon size={64} className="mb-1" />
      <Text className="text-2xl mb-5 font-semibold">Sign in to Github Clone</Text>

      <div className="flex flex-col gap-4">
        <FormControl className="min-w-100">
          <FormControl.Label>Username or email address</FormControl.Label>
          <TextInput
            className="w-full"
            value={formik.values.username}
            onChange={formik.handleChange}
            inputMode="text"
            name="username"
            aria-required
            required
            onBlur={formik.handleBlur}
          />

          {formik.errors.username && formik.touched.username && (
            <FormControl.Validation variant="error">
              {formik.errors.username}
            </FormControl.Validation>
          )}
        </FormControl>

        <FormControl className="min-w-100">
          <FormControl.Label className="flex! w-full justify-between">
            Password
            {/* <Button variant="link" className="ml-auto p-0">
              Forgot password?
            </Button> */}
          </FormControl.Label>

          <TextInput
            className="w-full"
            value={formik.values.password}
            onChange={formik.handleChange}
            type="password"
            name="password"
            aria-required
            required
            onBlur={formik.handleBlur}
          />
          {formik.errors.password && formik.touched.password && (
            <FormControl.Validation variant="error">
              {formik.errors.password}
            </FormControl.Validation>
          )}
        </FormControl>

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
        <Link to={Routes.REGISTER}>
          <Button variant="link" className="font-normal!">
            Create an account
          </Button>
        </Link>
      </Text>
    </div>
  );
}
