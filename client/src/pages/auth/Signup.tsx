import { TextInput, Button, Text } from "@/ui-lib";
import { useFormik } from "formik";
import LoginImage from "@/assets/images/login-background.webp";

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
    <div className="grid grid-cols-2 size-full relative">
      <img src={LoginImage} alt="Login" className="h-full w-full object-cover absolute" />
      <div className="flex items-center justify-center" />
      <section className="flex z-1 rounded-2xl bg-white flex-col gap-4 items-center justify-center h-dvh grow">
        <Text className="text-lg font-medium">Sign in to Github</Text>

        <form onSubmit={formik.handleSubmit} className="flex flex-col gap-4">
          <TextInput
            label="Username or email address"
            className="w-full"
            value={formik.values.username}
            onChange={formik.handleChange}
            inputMode="text"
            name="username"
            aria-required
            required
          />

          <TextInput
            label="Password"
            className="w-full"
            value={formik.values.password}
            onChange={formik.handleChange}
            inputMode="none"
            type="password"
            showPasswordToggle
            name="password"
            aria-required
            
            required
          />

          <Button type="submit">Sign In</Button>

          <Text className="text-sm self-center text-gray-500">Dont have an account? <a className="text-blue-500 ">Sign up here</a></Text>
        </form>
      </section>
    </div>
  );
}
