import { useState, useRef } from "react";
import "./App.css";

function App() {
  const [loggedIn, setLoggedIn] = useState(true);
  const [hasSubmitted, setHasSubmitted] = useState(false);
  const [questionNumber, setQuestionNumber] = useState(0);
  const totalNumberOfQuestions = 7;

  const arrOfAnswers = useRef(new Array(totalNumberOfQuestions)); // Array storing answers for each question

  const submitAnswers = () => {
    fetch(window.location.href, {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify(arrOfAnswers.current),
    })
      .then((response) => response.json())
      .then((json) => console.log(json));
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

  const updateCurrentAnswer = () => {
    const copy = arrOfAnswers.current.slice();
    copy[questionNumber] = document.getElementById("code-input").value;
    arrOfAnswers.current = copy;
    console.log(arrOfAnswers.current);
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
    if (questionNumber >= totalNumberOfQuestions - 1) return;

    updateCurrentAnswer();
    if (arrOfAnswers.current[questionNumber + 1] === undefined)
      document.getElementById("code-input").value = "";
    else
      document.getElementById("code-input").value =
        arrOfAnswers.current[questionNumber + 1];
    setQuestionNumber(questionNumber + 1);
  };

  return (
    <div>
      {!hasSubmitted ? (
        <h2>
          Question {questionNumber + 1}/{totalNumberOfQuestions}
        </h2>
      ) : null}

      {loggedIn && !hasSubmitted ? (
        <CodeForm submitButtonMethod={submitButtonMethod} />
      ) : loggedIn && hasSubmitted ? (
        <p>Your code has now been finalized and rendered uneditable.</p>
      ) : (
        <p>You must log into your account first to access the form.</p>
      )}

      {!hasSubmitted ? (
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

function CodeForm({ submitButtonMethod }) {
  return (
    <form>
      <label htmlFor="code-input">Copy and paste your Python code below:</label>
      <br></br>
      <textarea name="code" id="code-input"></textarea>
      <br></br>
      <button
        type="button"
        id="code-submit"
        onClick={() => submitButtonMethod(true)}
      >
        Finalize and Submit All
      </button>
      <br></br>
      <label htmlFor="code-submit">
        You will not be able to edit your code after submission.
      </label>
    </form>
  );
}

export default App;
