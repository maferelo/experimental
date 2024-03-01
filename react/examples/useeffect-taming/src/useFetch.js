import { useEffect, useState } from "react";

/*
Rules
* Always use the setter for useState
* Always put a dependency array on useEffect, useCallback, useMemo
* To run useEffect only once, pass an empty array as the dependency array
* Don't depend on data you set
*/

export function useFetch(options) {
  const [data, setData] = useState(null);

  useEffect(() => {
    console.log("useFetch useEffect");
    fetch(options.url)
      .then((res) => res.json())
      .then((data) => {
        console.log("useFetch useEffect data", data);
        setData(data);
      });
    // always use scalars as dependencies int, string, bool
    // function objects or arrays need refs or useCallback
  }, [options.url]);

  return {
    data,
  };
}
