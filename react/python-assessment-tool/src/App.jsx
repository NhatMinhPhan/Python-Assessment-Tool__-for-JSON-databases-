import { useState, useRef, useEffect } from "react";
import { useNavigate } from "react-router";
import CodeForm from "./components/CodeForm";
import "./App.css";

// importa.meta.env imports from an ".env.local" file, which is ignored by git.

function App({ getSessionUsername, getSessionUserId, clearLoginSession }) {
  const [loggedIn, setLoggedIn] = useState(true);
  const [hasSubmitted, setHasSubmitted] = useState(false);
  const [questionNumber, setQuestionNumber] = useState(0);
  const TOTAL_NUMBER_OF_QUESTIONS = Number.parseInt(
    import.meta.env.VITE_TOTAL_QUESTIONS
  );
  // const USER_NAME = import.meta.env.VITE_USER_NAME;
  // const USER_ID = Number.parseInt(import.meta.env.VITE_USER_ID);
  const USER_NAME = getSessionUsername();
  const USER_ID = getSessionUserId();

  // For navigation with React Router:
  let navigate = useNavigate();

  useEffect(() => {
    // Upon mount, if the user hasn't logged in, redirect to the LOGIN page
    if (
      USER_NAME === "" ||
      USER_ID === "" ||
      USER_NAME === undefined ||
      USER_ID === undefined ||
      USER_NAME === null ||
      USER_ID === null
    )
      navigate("/login");
    else {
      // Fetch visibility information from the server,
      // including if the user has already submitted their answers.
      // If they have, setHasSubmitted(true).
      fetch(import.meta.env.VITE_FLASK_EVAL_SET_VIEWABILITY + USER_ID)
        .then((response) => response.json())
        .then((visibilityInfo) => {
          if (visibilityInfo["submitted"] === true) {
            // User has made a submission
            setHasSubmitted(true);
          }
        });
    }

    // Cleanup function to be returned
    return () => {
      console.log("The user hasn't logged in or has logged out.");
    };
  }, []); // Empty dependency array ensures it runs only once on mount

  const arrOfAnswers = useRef(new Array(TOTAL_NUMBER_OF_QUESTIONS)); // Array storing answers for each question

  const updateCurrentAnswer = () => {
    const copy = arrOfAnswers.current.slice();
    copy[questionNumber] = document.getElementById("code-input").value;
    arrOfAnswers.current = copy;
  };

  const submitAnswers = () => {
    updateCurrentAnswer(); // updates the answer for the question the user is currently on
    const submission = {};

    // Replace all null/undefined/non-string items in arrOfAnswers.current with the empty string ""
    for (let i = 0; i < arrOfAnswers.current.length; i++) {
      if (
        arrOfAnswers.current[i] === null ||
        arrOfAnswers.current[i] === undefined ||
        typeof arrOfAnswers.current[i] !== "string"
      )
        arrOfAnswers.current[i] = "";
    }

    submission["answers"] = arrOfAnswers.current;
    submission["id"] = USER_ID + ""; // id must be a string

    const requestOptions = {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(submission),
    };

    fetch(import.meta.env.VITE_FLASK_EVAL_SUBMIT + USER_ID, requestOptions)
      .then((response) => response.json())
      .then((json) => console.log(json));
    // Submit to USER_ID, which must be added to the database after registration.
  };

  const submitButtonMethod = (boolean) => {
    console.assert(
      boolean === true || boolean === false,
      "The passed argument for boolean in submitButtonMethod is not a boolean"
    );
    if (boolean === true || boolean === false) {
      if (boolean === true) {
        submitAnswers();
        // clearLoginSession(); // Passed as an argument from main.jsx
        // navigate("/login");
      }
      setHasSubmitted(boolean);
    }
  };

  const previousQuestion = () => {
    if (questionNumber <= 0) return;

    updateCurrentAnswer();
    if (arrOfAnswers.current[questionNumber - 1] === undefined)
      document.getElementById("code-input").value = "";
    else
      document.getElementById("code-input").value =
        arrOfAnswers.current[questionNumber - 1];
    setQuestionNumber(questionNumber - 1);
  };

  const nextQuestion = () => {
    if (questionNumber >= TOTAL_NUMBER_OF_QUESTIONS - 1) return;

    updateCurrentAnswer();
    if (arrOfAnswers.current[questionNumber + 1] === undefined)
      document.getElementById("code-input").value = "";
    else
      document.getElementById("code-input").value =
        arrOfAnswers.current[questionNumber + 1];
    setQuestionNumber(questionNumber + 1);
  };

  const logout = () => {
    fetch(import.meta.env.VITE_FLASK_LOGOUT).then((response) => {
      if (response.status === 200) {
        setLoggedIn(false);
        clearLoginSession(); // Passed as an argument from main.jsx
        navigate("/login");
      }
    });
  };

  return (
    <div>
      {loggedIn ? (
        <div>
          <p id="user-id">
            Username: {USER_NAME} - User ID: {USER_ID}
            <br></br>
            Do not share the information above due to its confidential nature.
            <br></br>
            In addition, do not close or refresh this tab as your session and
            progress will not be saved.
          </p>
          <button type="button" id="logout-button" onClick={() => logout()}>
            Log out
          </button>
          <hr id="logout-hr"></hr>
        </div>
      ) : null}

      {!hasSubmitted && loggedIn ? (
        <h2>
          Question {questionNumber + 1}/{TOTAL_NUMBER_OF_QUESTIONS}
        </h2>
      ) : null}

      {loggedIn && !hasSubmitted ? (
        <CodeForm submitButtonMethod={submitButtonMethod} />
      ) : loggedIn && hasSubmitted ? (
        <p>Your code has now been finalized and rendered uneditable.</p>
      ) : (
        <p>You must log into your account first to access the form.</p>
      )}

      {!hasSubmitted && loggedIn ? (
        <div>
          <button
            type="button"
            onClick={() => previousQuestion()}
            id="previous-question-link"
          >
            Previous Question
          </button>
          {" | "}
          <button
            type="button"
            onClick={() => nextQuestion()}
            id="next-question-link"
          >
            Next Question
          </button>
        </div>
      ) : null}
    </div>
  );
}

export default App;
