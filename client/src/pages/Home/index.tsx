import { Button } from "@/ui-lib";
import { Routes } from "@/routes/Routes";
import { Link } from "react-router-dom";
export function Home() {
  return (
    <div>
      <Link to={Routes.LOGIN}>
        <Button>Go to login</Button>
      </Link>
      <Link to={Routes.REGISTER}>
        <Button>Go to signup</Button>
      </Link>
    </div>
  );
}
