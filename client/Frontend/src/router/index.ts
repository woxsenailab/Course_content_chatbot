import { createBrowserRouter } from "react-router-dom";
import Homepage from "../pages/Homepage";
import Layout from "./Outlet";

const router = createBrowserRouter([
  {
    element: Layout(),
    children: [
      {
        path: "/",
        element: Homepage(),
      },
    //   {
    //     path:"/admin/SignIn",
    //     element:SignIn()
    //   }
    ],
  },
]);

export default router;
