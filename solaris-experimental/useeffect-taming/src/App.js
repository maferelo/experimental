import "./App.css";

import { useState } from "react";
import { useFetch } from "./useFetch";

function App() {
  const [url, setUrl] = useState(null);
  const { data } = useFetch({
    url,
  });

  console.log("App rendering");

  return (
    <div className="App">
      <div>Hello</div>
      <div>{JSON.stringify(data)}</div>
      <button onClick={() => setUrl("/jack.json")}>Load Jack</button>
      <button onClick={() => setUrl("/sally.json")}>Load Sally</button>
    </div>
  );
}

export default App;
