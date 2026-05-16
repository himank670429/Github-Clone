import { FormControl, Text, TextInput, Button } from "@/ui-lib";
import { useFormik } from "formik";

interface LoginFormValues {
  username: string;
  password: string;
}

export function Login() {
  const formik = useFormik<LoginFormValues>({
    initialValues: {
      username: "",
      password: "",
    },
    onSubmit: (values) => {
      console.log(values);
    },
  });

  return (
    <div className="flex flex-col gap-4 items-center justify-center h-dvh grow">
      <Text>Sign in to Github</Text>

      <form onSubmit={formik.handleSubmit}>
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
          />
        </FormControl>

        <FormControl className="min-w-100">
          <FormControl.Label>Password</FormControl.Label>
          <TextInput
            className="w-full"
            value={formik.values.password}
            onChange={formik.handleChange}
            inputMode="text"
            name="password"
            aria-required
            required
          />
        </FormControl>

        <Button type="submit">
          Sign In
        </Button>
      </form>
    </div>
  );
}
