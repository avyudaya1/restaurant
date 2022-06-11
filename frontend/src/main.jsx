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
import LoginPage from "./components/LoginPage";
import CookieIcon from '@mui/icons-material/Cookie';
import RestaurantIcon from '@mui/icons-material/Restaurant';

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
    loginPage={LoginPage}
  >
    {(permissions) => [
      <Resource name="itemcategories" options={{ label: 'Item Categories'}} {...categorycommon}/>,
      <Resource name="items" {...items} icon={RestaurantIcon}/>,
      <Resource name="menuitemcategories" options={{ label: 'Menuitem Categories'}} {...categorycommon}/>,
      <Resource name="menuitems" {...menuitems} icon={CookieIcon} />,
    ]}
  </Admin>
);
