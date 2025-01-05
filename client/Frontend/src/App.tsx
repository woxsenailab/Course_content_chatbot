import { RouterProvider } from "react-router-dom";
import router from "./router";

function app() {
  return (
    <>
      <RouterProvider router={router}/>
    </>
  );
}
export default app;