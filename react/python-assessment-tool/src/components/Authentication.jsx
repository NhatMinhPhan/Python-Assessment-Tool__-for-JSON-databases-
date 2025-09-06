import { useEffect, useState } from "react";

export default function Authentication({
  purposeOfAuthentication,
  submitAction,
  loginFailed,
}) {
  const [hasSubmitted, setHasSubmitted] = useState(false);
  const [showError, setShowError] = useState(false);
  const [errorMessage, setErrorMessage] = useState("PLACEHOLDER");

  useEffect(() => {
    // When used in the LOGIN page, if login fails (due to a wrong password, etc.)
    if (
      purposeOfAuthentication.toLowerCase().trim() === "login" &&
      loginFailed === true
    ) {
      setErrorMessage("Invalid username / password.");
      setHasSubmitted(false);

      // Enable the input fields
      document.getElementById("username").disabled = false;
      document.getElementById("password").disabled = false;
    }
  });

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
    switch (purposeOfAuthentication.toLowerCase().trim()) {
      case "register":
        fetch(
          import.meta.env.VITE_FLASK_REGISTER_DUPLICATECHECK + username
        ).then((response) => {
          if (response.status !== 200) {
            setShowError(true);
            setErrorMessage(
              "The username you've chosen already exists! Please pick another one."
            );
            setHasSubmitted(false);
            document.getElementById("username").disabled = false;
            document.getElementById("password").disabled = false;
            return;
          } else submitAction(username, password);
        });
        break;

      case "login":
        fetch(import.meta.env.VITE_FLASK_LOGIN_DUPLICATECHECK + username).then(
          (response) => {
            if (response.status !== 200) {
              setShowError(true);
              setErrorMessage("Invalid username / password.");
              setHasSubmitted(false);
              document.getElementById("username").disabled = false;
              document.getElementById("password").disabled = false;
              return;
            } else submitAction(username, password);
          }
        );
        break;
    }
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
        {showError ||
        (purposeOfAuthentication.toLowerCase().trim() === "login" &&
          loginFailed === true) ? (
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
