import { useState, useRef } from "react";
import CodeForm from "./components/CodeForm";
import "./App.css";

// importa.meta.env imports from an ".env.local" file, which is ignored by git.

function App() {
  const [loggedIn, setLoggedIn] = useState(true);
  const [hasSubmitted, setHasSubmitted] = useState(false);
  const [questionNumber, setQuestionNumber] = useState(0);
  const TOTAL_NUMBER_OF_QUESTIONS = Number.parseInt(
    import.meta.env.VITE_TOTAL_QUESTIONS
  );
  const USER_NAME = import.meta.env.VITE_USER_NAME;
  const USER_ID = Number.parseInt(import.meta.env.VITE_USER_ID);

  const arrOfAnswers = useRef(new Array(TOTAL_NUMBER_OF_QUESTIONS)); // Array storing answers for each question

  const updateCurrentAnswer = () => {
    const copy = arrOfAnswers.current.slice();
    copy[questionNumber] = document.getElementById("code-input").value;
    arrOfAnswers.current = copy;
  };

  const submitAnswers = () => {
    updateCurrentAnswer(); // updates the answer for the question the user is currently on
    const submission = {};
    submission["answers"] = arrOfAnswers.current;
    submission["id"] = USER_ID + ""; // id must be a string

    const requestOptions = {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(submission),
    };

    fetch(
      import.meta.env.VITE_ANSWER_SUBMISSION_ENDPOINT + USER_ID,
      requestOptions
    )
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
      if (boolean === true) submitAnswers();
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
    setLoggedIn(false);
  };

  return (
    <div>
      {loggedIn ? (
        <div>
          <p id="user-id">
            User name: {USER_NAME} - User ID: {USER_ID}
            <br></br>
            Do not share the information above due to its confidential nature.
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
