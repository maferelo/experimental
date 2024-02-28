import { memo, useCallback, useMemo, useState } from "react";

function Swatch({ color }) {
  console.log(`Swatch: ${color}`);
  return (
    <div
      style={{
        width: 100,
        height: 100,
        backgroundColor: color,
        borderRadius: 4,
      }}
    />
  );
}

/*
 * This is a memoized version of Swatch.
 * It will only re-render when the color prop changes.
 * Use it for performance optimization.
 */
Swatch = memo(Swatch);

export default function App() {
  const [count, setCount] = useState(0);
  const [color, setColor] = useState("red");

  // useMemo will only recompute the memoized value when one of the dependencies has changed.
  // This optimization helps to avoid expensive calculations on every render.
  // use it for objects and arrays
  // use useCallback for functions
  // like a computed object with dependencies
  // this works for state that doesn't change often
  const memoizedColor = useMemo(() => color, [color]);
  const setColorCallback = useCallback(() => setColor("blue"), []);
  console.log(`count: ${count}`);
  return (
    <div className="App">
      <button onClick={() => setCount(count + 1)}>+</button>
      <button onClick={() => setColor(color === "red" ? "blue" : "red")}>
        swatch
      </button>
      <Swatch color={memoizedColor} />
    </div>
  );
}
