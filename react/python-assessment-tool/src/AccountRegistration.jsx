import { useRef } from "react";
import Authentication from "./components/Authentication";
import { useNavigate, Link } from "react-router";

export default function AccountRegistration() {
  const loginLink = useRef();
  // For automatic redirect to the LOGIN page:
  let navigate = useNavigate();

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

    fetch(import.meta.env.VITE_ACCOUNTS, requestOptions)
      .then((response) => response.json())
      .then((json) => {
        // After the successful POST response, get the "id" of the account and add a new entry to user_answers
        const id = json["id"];
        const requestOptsForAnswers = {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ id: id }),
        };
        fetch(
          import.meta.env.VITE_ANSWER_SUBMISSION_ENDPOINT,
          requestOptsForAnswers
        )
          .then((response) => response.status)
          .then((status) => {
            console.log(status);
            navigate("/login");
          });
      });
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
