import { useRef } from "react";
import Authentication from "./components/Authentication";
import { useNavigate, Link } from "react-router";

export default function AccountLogin({ updateLoginSession }) {
  const registrationLink = useRef();
  let navigate = useNavigate();

  const submitAction = (username, password) => {
    registrationLink.current.remove();

    fetch(import.meta.env.VITE_ACCOUNTS)
      .then((response) => response.json())
      .then((accounts) => {
        const user_found = accounts.find(
          (element) => element["username"] === username
        ); // Finds the first instance satisfying this condition (it surely exists)
        updateLoginSession(username, user_found["id"]);
        return user_found["id"];
      })
      .then((userID) => {
        // Checks if there is a corresponding user_answers for this user with the user ID. If not, generate one.
        fetch(import.meta.env.VITE_ANSWER_SUBMISSION_ENDPOINT)
          .then((response) => response.json())
          .then((all_users_answers) => {
            const user_answers_found = all_users_answers.find(
              (element) => element["id"] === userID
            ); // Finds the first instance with the passed userID argument
            if (user_answers_found !== undefined) navigate("/"); // Entry exists
            else {
              // Generate an entry
              const requestOptsForAnswers = {
                method: "POST",
                headers: {
                  "Content-Type": "application/json",
                },
                body: JSON.stringify({ id: userID }),
              };
              fetch(
                import.meta.env.VITE_ANSWER_SUBMISSION_ENDPOINT,
                requestOptsForAnswers
              )
                .then((response) => response.status)
                .then((status) => {
                  console.log(status);
                  navigate("/");
                });
            }
          });
      });
  };

  return (
    <div>
      <Authentication
        purposeOfAuthentication="login"
        submitAction={submitAction}
      />
      <Link to="/register" ref={registrationLink}>
        Register
      </Link>
    </div>
  );
}
