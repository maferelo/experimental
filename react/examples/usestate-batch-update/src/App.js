import { useEffect, useState } from "react";

// In react 18 batch update is enabled by default
export default function App() {
  const [count, setCount] = useState(0);
  console.log(`count: ${count}`);

  const [name, setName] = useState("John");
  const [email, setEmail] = useState("john@gmail.com");

  useEffect(() => {
    console.log(`name: ${name}`);
  }, [name]);

  return (
    <div className="App">
      <button onClick={() => setCount(count + 1)}>+</button>
    </div>
  );
}
