import React, { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./styles.css";

import App from "./App";

/*
 * Data - Components - VDOM - DOM
 * react does shallow compare
 */
const root = createRoot(document.getElementById("root"));
root.render(
  // https://react.dev/reference/react/StrictMode
  <StrictMode>
    <App />
  </StrictMode>
);
