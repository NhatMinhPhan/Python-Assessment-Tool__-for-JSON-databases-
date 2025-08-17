import { useState } from "react";

export default function Authentication({
  purposeOfAuthentication,
  submitAction,
}) {
  const [hasSubmitted, setHasSubmitted] = useState(false);
  const [showError, setShowError] = useState(false);
  const [errorMessage, setErrorMessage] = useState("PLACEHOLDER");

  const submitInfo = () => {
    setShowError(false); // Hide the error message
    setHasSubmitted(true); // Hide the submit button
    // Disable the input fields
    document.getElementById("username").disabled = true;
    document.getElementById("password").disabled = true;

    // Temporary, insecure login data storage
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    // Usernames must be at least 8 letters long
    if (username === undefined || username === null || username.length < 8) {
      setShowError(true);
      if (purposeOfAuthentication.toLowerCase().trim() == "register")
        // Register
        setErrorMessage("Your username must be at least 8 letters long.");
      // Login
      else setErrorMessage("Invalid username / password.");
      setHasSubmitted(false);

      // Enable the input fields
      document.getElementById("username").disabled = false;
      document.getElementById("password").disabled = false;
      return;
    }

    // Passwords must be at least 8 letters long
    if (password === undefined || password === null || password.length < 8) {
      setShowError(true);
      if (purposeOfAuthentication.toLowerCase().trim() == "register")
        // Register
        setErrorMessage("Your password must be at least 8 letters long.");
      // Login
      else setErrorMessage("Invalid username / password.");
      setHasSubmitted(false);

      // Enable the input fields
      document.getElementById("username").disabled = false;
      document.getElementById("password").disabled = false;
      return;
    }

    // Check if username already exists
    fetch(import.meta.env.VITE_ACCOUNTS)
      .then((response) => response.json())
      .then((accounts) => {
        // The following if-statement can only be run on the REGISTRATION page
        if (
          accounts.length > 0 &&
          purposeOfAuthentication.toLowerCase().trim() == "register"
        ) {
          const username_already_used = (element) =>
            element["username"] === username;

          const username_in_accounts = accounts.some(username_already_used);
          // By using "some", it checks if there exists at least 1 element that satisifies the requirement

          if (username_in_accounts) {
            setShowError(true);
            setErrorMessage(
              "The username you've chosen already exists! Please pick another one."
            );
            setHasSubmitted(false);

            // Enable the input fields
            document.getElementById("username").disabled = false;
            document.getElementById("password").disabled = false;
            return;
          }
        }
        // The following else-if-statement can only be run on the LOGIN page
        else if (
          accounts.length > 0 &&
          purposeOfAuthentication.toLowerCase().trim() == "login"
        ) {
          const user_found = accounts.find(
            (element) => element["username"] === username
          ); // Finds the first instance satisfying this condition

          if (
            user_found === undefined || // Nonexistent user
            (user_found !== undefined && user_found["password"] !== password) // Incorrect password
          ) {
            setShowError(true);
            setErrorMessage("Invalid username / password.");
            setHasSubmitted(false);

            // Enable the input fields
            document.getElementById("username").disabled = false;
            document.getElementById("password").disabled = false;
            return;
          }
        }
        submitAction(username, password);
      });
  };

  return (
    <div>
      <h2>
        {purposeOfAuthentication.charAt(0).toUpperCase() +
          purposeOfAuthentication.slice(1)}
      </h2>
      <form>
        <label htmlFor="username">Username:</label>
        <br></br>
        <input type="text" name="username" id="username"></input>
        <br></br>
        <label htmlFor="password">Password:</label>
        <br></br>
        <input type="password" name="password" id="password"></input>
        <br></br>
        {showError ? (
          <div>
            <p style={{ color: "red", marginBottom: "0px" }}>{errorMessage}</p>
            <br></br>
          </div>
        ) : null}
        {!hasSubmitted ? (
          <button type="button" onClick={() => submitInfo()}>
            Submit
          </button>
        ) : (
          <p>Processing...</p>
        )}
      </form>
    </div>
  );
}
