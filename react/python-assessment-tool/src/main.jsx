import { StrictMode, useRef } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import App from "./App.jsx";
import AccountRegistration from "./AccountRegistration.jsx";
import { BrowserRouter, Routes, Route, Navigate } from "react-router";
import AccountLogin from "./AccountLogin.jsx";

const session = { username: "", userID: "" };

const clearSession = () => {
  session["username"] = "";
  session["userID"] = "";
};

const updateSession = (username, userID) => {
  session["username"] = username;
  session["userID"] = userID;
  console.log(session);
};

const getSessionUsername = () => session["username"];

const getSessionUserId = () => session["userID"];

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <BrowserRouter>
      <Routes>
        <Route
          index
          element={
            <App
              getSessionUsername={getSessionUsername}
              getSessionUserId={getSessionUserId}
              clearLoginSession={clearSession}
            />
          }
        />
        <Route
          path="login"
          element={<AccountLogin updateLoginSession={updateSession} />}
        />
        <Route path="register" element={<AccountRegistration />} />
        {/* Redirect any unmatched route (404) to the login page */}
        <Route path="*" element={<Navigate replace to="/login" />} />
      </Routes>
    </BrowserRouter>
  </StrictMode>
);
