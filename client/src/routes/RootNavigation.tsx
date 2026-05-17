import { BrowserRouter, Routes as RouterRoutes, Route } from "react-router-dom";
import { Routes } from "./Routes";

// Pages
import { Login, Signup, Home } from "@/pages";

export const RootNavigation = () => {
  return (
    <BrowserRouter>
      <RouterRoutes>
        <Route path={Routes.HOME} element={<Home />} />
        <Route path={Routes.LOGIN} element={<Login />} />
        <Route path={Routes.REGISTER} element={<Signup />} />
      </RouterRoutes>
    </BrowserRouter>
  );
};
