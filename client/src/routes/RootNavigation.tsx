import { BrowserRouter, Routes as RouterRoutes, Route } from "react-router-dom";
import { Routes } from "./Routes";

// Pages
import { Login } from "@/pages";

export const RootNavigation = () => {
  return (
    <BrowserRouter>
      <RouterRoutes>
        <Route path={Routes.HOME} element={<Login />} />
        <Route path={Routes.LOGIN} element={<Login />} />
      </RouterRoutes>
    </BrowserRouter>
  );
};
