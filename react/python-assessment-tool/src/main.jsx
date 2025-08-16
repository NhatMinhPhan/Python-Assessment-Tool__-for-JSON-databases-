import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import App from "./App.jsx";
import AccountRegistration from "./AccountRegistration.jsx";

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <AccountRegistration />
  </StrictMode>
);
