import ReactDOM from "react-dom/client";
import { Admin, Resource } from "react-admin";
import drfProvider, {
  tokenAuthProvider,
  fetchJsonWithAuthToken,
  jwtTokenAuthProvider,
  fetchJsonWithAuthJWTToken,
} from "ra-data-django-rest-framework";
import { parseBool } from "./helpers";
import items from "./items";
import menuitems from "./menuitems";
import categorycommon from "./categorycommon";
import Dashboard from "./components/Dashboard";

let dataProvider;
let authProvider;
const useJWTAuth = parseBool(import.meta.env.VITE_APP_USE_JWT_AUTH);

if (useJWTAuth) {
  console.log(
    "Using rest_framework_simplejwt.authentication.JWTAuthentication"
  );
  authProvider = jwtTokenAuthProvider({ obtainAuthTokenUrl: "/api/token/" });
  dataProvider = drfProvider("/api", fetchJsonWithAuthJWTToken);
} else {
  console.log("Using rest_framework.authentication.TokenAuthentication");
  authProvider = tokenAuthProvider();
  dataProvider = drfProvider("/api", fetchJsonWithAuthToken);
}

ReactDOM.createRoot(document.getElementById("root")).render(
  <Admin
    title="Restaurant"
    dashboard={Dashboard}
    authProvider={authProvider}
    dataProvider={dataProvider}
  >
    {(permissions) => [
      <Resource name="itemcategories" {...categorycommon}/>,
      <Resource name="items" {...items} />,
      <Resource name="menuitemcategories" {...categorycommon}/>,
      <Resource name="menuitems" {...menuitems} />,
    ]}
  </Admin>
);
