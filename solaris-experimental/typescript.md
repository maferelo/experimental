## Typescript notes / cheatsheet / refresher

### Typescript types

#### Primitives

```ts
// string | number | boolean | any | void | null | undefined | never
let a: number = 1;
const arr: Array<number> = [1, 2, 3];
```

#### Record

```ts
let thisRecord: Record<string, number> = {
  a: 1,
  b: 2,
  c: 3,
};
```

#### Function

```ts
let myFunc: (a: number, b: number) => number = (a, b) => a + b;
```

Default parameters

```ts
let myFunc: (a: number, b: number) => number = (a = 1, b = 2) => a + b;
```

Optional parameters

```ts
let myFunc: (a: number, b?: number) => number = (a, b) => a + (b || 0);
```

Function that returns a function

```ts
let myFunc: (mutate: (a: number) => number) => number = (mutate) => mutate(1);
```

#### Promise

```ts
let myPromise: Promise<number> = new Promise((resolve, reject) => {
  resolve(1);
});
```

#### Extending types

```ts
interface MyInterface {
  a: number;
  b: number;
}

interface MyExtendedInterface extends MyInterface {
  c: number;
}
```

#### Function overloads

Allows a function to have multiple signatures with different return types.

```ts
function myFunc(a: number, b: number): number;
function myFunc(a: string, b: string): string;
function myFunc(a: unknown, b: unknown): number | string {
  return (a as number) + (b as number);
}
```

#### Tuple

```ts
let myTuple: [number, string] = [1, "a"];
```

### Generics

```ts
function myFunc<T>(a: T): T {
  return a;
}

let a = myFunc<number>(1);
let b = myFunc<string>("a");
```

### React

#### Props

```tsx
interface Props {
  name: string;
  age: number;
}

const MyComponent: React.FC<Props> = ({ name, age }) => {
  return (
    <div>
      <p>Name: {name}</p>
      <p>Age: {age}</p>
    </div>
  );
};
```

#### State

```tsx
interface AppState {
  count: number;
}

const MyComponent: React.FC = () => {
  const [state, setState] = useState<AppState>({ count: 0 });

  const increment = () => {
    setState({ count: state.count + 1 });
  };

  const decrement = () => {
    setState({ count: state.count - 1 });
  };

  return (
    <div>
      <p>Count: {state.count}</p>
      <button onClick={increment}>Increment</button>
      <button onClick={decrement}>Decrement</button>
    </div>
  );
};
```

#### Reducer

```tsx
// Define the state type
interface AppState {
  count: number;
}

// Define the action types
type Action = { type: "increment" } | { type: "decrement" };

// Reducer function
const reducer = (state: AppState, action: Action): AppState => {
  switch (action.type) {
    case "increment":
      return { ...state, count: state.count + 1 };
    case "decrement":
      return { ...state, count: state.count - 1 };
    default:
      return state;
  }
};

const MyComponent: React.FC = () => {
  // Initialize state with an object of type AppState
  const [state, dispatch] = useReducer(reducer, { count: 0 });

  const increment = () => {
    dispatch({ type: "increment" });
  };

  const decrement = () => {
    dispatch({ type: "decrement" });
  };

  return (
    <div>
      <p>Count: {state.count}</p>
      <button onClick={increment}>Increment</button>
      <button onClick={decrement}>Decrement</button>
    </div>
  );
};

export default MyComponent;
```

#### Event handlers

```tsx
const MyComponent: React.FC = () => {
  const [state, setState] = useState<AppState>({ count: 0 });

  const increment = () => {
    setState({ count: state.count + 1 });
  };

  const decrement = () => {
    setState({ count: state.count - 1 });
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setState({ count: parseInt(e.target.value) });
  };

  return (
    <div>
      <p>Count: {state.count}</p>
      <button onClick={increment}>Increment</button>
      <button onClick={decrement}>Decrement</button>
      <input type="number" value={state.count} onChange={handleChange} />
    </div>
  );
};
```

#### Refs

```tsx
const MyComponent: React.FC = () => {
  const [state, setState] = useState<AppState>({ count: 0 });
  const inputRef = useRef<HTMLInputElement>(null);

  const increment = () => {
    setState({ count: state.count + 1 });
  };

  const decrement = () => {
    setState({ count: state.count - 1 });
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setState({ count: parseInt(e.target.value) });
  };

  const focusInput = () => {
    inputRef.current?.focus();
  };

  return (
    <div>
      <p>Count: {state.count}</p>
      <button onClick={increment}>Increment</button>
      <button onClick={decrement}>Decrement</button>
      <input
        ref={inputRef}
        type="number"
        value={state.count}
        onChange={handleChange}
      />
      <button onClick={focusInput}>Focus input</button>
    </div>
  );
};
```

#### Context

```tsx
interface AppState {
  count: number;
}

interface AppContext {
  state: AppState;
  dispatch: React.Dispatch<Action>;
}

const AppContext = createContext<AppContext>({
  state: { count: 0 },
  dispatch: () => {},
});

const reducer = (state: AppState, action: Action): AppState => {
  switch (action.type) {
    case "increment":
      return { ...state, count: state.count + 1 };
    case "decrement":
      return { ...state, count: state.count - 1 };
    default:
      return state;
  }
};

const MyComponent: React.FC = () => {
  const [state, dispatch] = useReducer(reducer, { count: 0 });

  return (
    <AppContext.Provider value={{ state, dispatch }}>
      <MyChildComponent />
    </AppContext.Provider>
  );
};

const MyChildComponent: React.FC = () => {
  const { state, dispatch } = useContext(AppContext);

  const increment = () => {
    dispatch({ type: "increment" });
  };

  const decrement = () => {
    dispatch({ type: "decrement" });
  };

  return (
    <div>
      <p>Count: {state.count}</p>
      <button onClick={increment}>Increment</button>
      <button onClick={decrement}>Decrement</button>
    </div>
  );
};
```

#### Custom hooks

```tsx
interface AppState {
  count: number;
}

const useCounter = (initialState: AppState) => {
  const [state, setState] = useState<AppState>(initialState);

  const increment = () => {
    setState({ count: state.count + 1 });
  };

  const decrement = () => {
    setState({ count: state.count - 1 });
  };

  return { state, increment, decrement };
};

const MyComponent: React.FC = () => {
  const { state, increment, decrement } = useCounter({ count: 0 });

  return (
    <div>
      <p>Count: {state.count}</p>
      <button onClick={increment}>Increment</button>
      <button onClick={decrement}>Decrement</button>
    </div>
  );
};
```

#### Higher order components

```tsx
interface AppState {
  count: number;
}

const withCounter = (Component: React.FC) => {
  const initialState: AppState = { count: 0 };

  const Counter: React.FC = () => {
    const [state, setState] = useState<AppState>(initialState);

    const increment = () => {
      setState({ count: state.count + 1 });
    };

    const decrement = () => {
      setState({ count: state.count - 1 });
    };

    return (
      <Component
        count={state.count}
        increment={increment}
        decrement={decrement}
      />
    );
  };

  return Counter;
};

interface Props {
  count: number;
  increment: () => void;
  decrement: () => void;
}

const MyComponent: React.FC<Props> = ({ count, increment, decrement }) => {
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={increment}>Increment</button>
      <button onClick={decrement}>Decrement</button>
    </div>
  );
};

export default withCounter(MyComponent);
```

#### Routing

```tsx
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";

const App: React.FC = () => {
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/about">About</Link>
            </li>
          </ul>
        </nav>

        <Switch>
          <Route path="/about">
            <About />
          </Route>
          <Route path="/">
            <Home />
          </Route>
        </Switch>
      </div>
    </Router>
  );
};

const Home: React.FC = () => {
  return <h2>Home</h2>;
};

const About: React.FC = () => {
  return <h2>About</h2>;
};
```
