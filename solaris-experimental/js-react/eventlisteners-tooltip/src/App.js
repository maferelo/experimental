import { useCallback, useEffect, useRef, useState } from "react";

export default function App() {
  const [tooltipShown, setTooltipShown] = useState(false);
  const tooltipPopperRef = useRef(null);

  const onMouseEnter = useCallback(() => {
    setTooltipShown(true);
  }, []);
  const onMouseLeave = useCallback(() => {
    setTooltipShown(false);
  }, []);

  useEffect(() => {
    const tooltipPopper = tooltipPopperRef.current;
    tooltipPopper.addEventListener("mouseenter", onMouseEnter);
    tooltipPopper.addEventListener("mouseleave", onMouseLeave);
    return () => {
      tooltipPopper.removeEventListener("mouseenter", onMouseEnter);
      tooltipPopper.removeEventListener("mouseleave", onMouseLeave);
    };
  }, [onMouseEnter, onMouseLeave]);

  return (
    <div className="App">
      <div ref={tooltipPopperRef}>Tooltip popper</div>
      {tooltipShown && <div className="tooltip">Tooltip</div>}
    </div>
  );
}
