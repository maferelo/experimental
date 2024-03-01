import { useState } from "react";

export const Counter = () => {
  const [count, setCount] = useState(0);

  const increment = () => setCount(count + 1);
  return (
    <div>
      <div>Counter</div>
      <span>{count}</span>
      <br />
      <button onClick={increment}>Increment</button>
    </div>
  );
};
