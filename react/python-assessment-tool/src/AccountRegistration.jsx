import { useRef, useEffect } from "react";
import Authentication from "./components/Authentication";
import { useNavigate, Link } from "react-router";

export default function AccountRegistration({
  getSessionUsername,
  getSessionUserId,
}) {
  const loginLink = useRef();
  // For automatic redirect to the LOGIN page:
  let navigate = useNavigate();

  useEffect(() => {
    // Upon mount, if the user has already logged in, redirect to index.
    const USER_NAME = getSessionUsername();
    const USER_ID = getSessionUserId();
    if (
      USER_NAME !== "" &&
      USER_ID !== "" &&
      USER_NAME !== undefined &&
      USER_ID !== undefined &&
      USER_NAME !== null &&
      USER_ID !== null
    )
      navigate("/");
  }, []);

  const submitAction = (username, password) => {
    // Remove the link to the LOGIN page
    loginLink.current.remove();

    // Submit the login data
    const submission = {};
    submission["username"] = username;
    submission["password"] = password;

    const requestOptions = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(submission),
    };

    fetch(import.meta.env.VITE_FLASK_REGISTER, requestOptions).then(
      (response) => {
        console.log(response.status);
        if (response.status == 200) navigate("/login");
      }
    );
  };

  return (
    <div>
      <Authentication
        purposeOfAuthentication="register"
        submitAction={submitAction}
      />
      <Link to="/login" ref={loginLink}>
        Login
      </Link>
    </div>
  );
}
