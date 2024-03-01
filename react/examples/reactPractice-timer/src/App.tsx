import { useRef, useState } from "react";
import "./styles.css";

let appRender = 0;
let INITIAL_TIME = 300; // 5 minutes
export default function App() {
  console.log(`appRender = ${appRender++}`);
  const [time, setTime] = useState(INITIAL_TIME);
  let instervalRef = useRef<NodeJS.Timeout | null>(null);

  const handleStart = () => {
    if (!instervalRef.current) {
      instervalRef.current = setInterval(() => {
        setTime((prevTime) => {
          if (prevTime === 0) {
            handleStop();
            return INITIAL_TIME;
          }
          return prevTime - 1;
        });
      }, 1000);
    }
  };

  const handleStop = () => {
    clearInterval(instervalRef.current!);
    instervalRef.current = null;
  };

  const handleReset = () => {
    setTime(INITIAL_TIME);
  };

  return (
    <>
      <div>{time}</div>
      <button onClick={handleStart}>START</button>
      <button onClick={handleStop}>STOP</button>
      <button onClick={handleReset}>RESET</button>
    </>
  );
}
