import "./styles.css";

import { Counter } from "./components/Counter";

let appRender = 0;
export default function App() {
  console.log(`appRender = ${appRender++}`);

  return (
    <>
      <div>Hello World</div>
      <hr />
      <Counter />
    </>
  );
}
