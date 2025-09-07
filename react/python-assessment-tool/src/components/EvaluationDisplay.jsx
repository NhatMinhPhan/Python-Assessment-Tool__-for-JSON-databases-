import { useState, useEffect } from "react";

export default function EvaluationDisplay({ text, questionNumber }) {
  const [judgeText, setJudgeText] = useState("");
  const [overallAverageText, setOverallAverageText] = useState("");

  useEffect(() => {
    // The last sentence indicates the overall average, beginning with a newline character (\n).
    // So, begin by finding the last index of \n.
    setOverallAverageText(text[text.length - 1]);
    setJudgeText(text[questionNumber]);
  }, [text, questionNumber]);

  return (
    <div>
      <div className="eval-display">
        {judgeText !== undefined
          ? judgeText
              .split("\n")
              .map((line, index) => <p key={index}>{line}</p>)
          : "Placeholder"}
      </div>
      <p id="overall-average-text">
        <b>
          {overallAverageText !== undefined
            ? overallAverageText
            : "Placeholder"}
        </b>
      </p>
    </div>
  );
}
