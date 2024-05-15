import { createBrowserRouter } from "react-router-dom";

import { Login } from "./components/auth/login/index.jsx";
import App from "./App.jsx";
import { NotFound404 } from "./components/common/route/notFound404.jsx";
import { SignUp } from "./components/auth/signUp";
import { LayOut } from "./components/common/layout/main/index.jsx";
import PrivateRoute from "./components/common/route/privateRoute.jsx";
import Medicine from "./components/page/medicine/index.jsx";
import DashBoard from "./components/page/dashBoard/index.jsx";
import { pageCms } from "./components/page/page.jsx";
import { Otp } from "./components/auth/otp/index.jsx";
import { ForgotPassword } from "./components/auth/forgotPassword/index.jsx";

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    children: [
      {
        path: "login",
        children: [
          {
            path: "",
            element: <Login />,
          },
        ],
      },
      {
        path: "register",
        children: [
          {
            path: "",
            element: <SignUp />,
          },
          {
            path: "verify-email",
            element: <Otp />,
          },
        ],
      },
      {
        path: "forgot-password",
        children: [
          {
            path: "",
            element: <ForgotPassword />,
          },
        ],
      },
      {
        path: "",
        element: <LayOut />,
        children: [
          {
            path: "",
            element: <PrivateRoute />,
            children: [
              {
                path: "",
                element: <DashBoard />,
              },
              ...pageCms,
            ],
          },
        ],
      },
      {
        path: "*",
        element: <NotFound404 />,
      },
    ],
  },
]);
export default router;
