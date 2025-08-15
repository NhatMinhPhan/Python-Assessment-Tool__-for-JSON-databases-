import { useState } from "react";

export default function CodeForm({ submitButtonMethod }) {
  const [showConfirmation, setShowConfirmation] = useState(false);

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
      <label htmlFor="code-input">Copy and paste your Python code below:</label>
      <br></br>
      <textarea name="code" id="code-input"></textarea>
      <br></br>
      <button type="button" id="code-submit" onClick={() => finalizedSubmit()}>
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
    </form>
  );
}
