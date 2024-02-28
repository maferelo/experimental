import { useEffect, useState } from "react";

const Timer = () => {
  const [count, setCount] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setCount((count) => count + 1);
    }, 1000);
    return () => clearInterval(interval);
    // an empty array of dependencies means this effect will only run once
    // similar to componentDidMount
  }, []);

  return <div className="timer">Timer: {count}</div>;
};

export default function App() {
  return (
    <div className="App">
      <Timer />
    </div>
  );
}
