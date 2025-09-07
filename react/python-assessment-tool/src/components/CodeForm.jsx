import { useState, useRef, useEffect } from "react";

export default function CodeForm({ submitButtonMethod, editable }) {
  const [showConfirmation, setShowConfirmation] = useState(false);
  const codeTextArea = useRef(null);

  useEffect(() => {
    if (editable === true) {
      codeTextArea.current.disabled = false;
    } else codeTextArea.current.disabled = true;
  });

  const finalizedSubmit = () => {
    if (showConfirmation) submitButtonMethod(true);
    else {
      setShowConfirmation(true);

      // If the user does not submit their answers in 5s, reset.
      setTimeout(() => setShowConfirmation(false), 5000);
    }
  };

  return (
    <form>
      <label htmlFor="code-input">
        {editable === true
          ? "Copy and paste your Python code below:"
          : "Your code has already been submitted. You cannot make any further changes."}
      </label>
      <br></br>
      <textarea name="code" id="code-input" ref={codeTextArea}></textarea>
      {editable === true ? (
        <div>
          <br></br>
          <button
            type="button"
            id="code-submit"
            onClick={() => finalizedSubmit()}
          >
            Finalize and Submit All
          </button>
          <br></br>
          <label htmlFor="code-submit">
            {!showConfirmation ? (
              "You will not be able to edit your code after submission."
            ) : (
              <b>Ready to submit everything? Click again to confirm.</b>
            )}
          </label>
        </div>
      ) : null}
    </form>
  );
}
