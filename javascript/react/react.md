# React

## Docs

### Hooks

#### [useEffect](https://react.dev/reference/react/useEffect)

Calling `useEffect` with an empty array as the second argument will cause the effect to only run once, on mount. This is equivalent to `componentDidMount` in class components.

```jsx
useEffect(() => {
  // do something
  return () => {
    // do something
  };
}, []);
```

The function returned from the effect will be called when the component unmounts. This is equivalent to `componentWillUnmount` in class components.

#### useReducer

Well written reducers don't send requests, sche

#### [useDebugValue](https://react.dev/reference/react/useDebugValue)

`useDebugValue` is a hook that allows you to display a label for custom hooks in React DevTools. It takes two arguments, the value to display and an optional function to format the value. The function is only called when the DevTools are open. It's useful for displaying values that are expensive to compute or are difficult to inspect and in a custom hook.

```jsx
useDebugValue(value, formatValue);
useDebugValue(date, (date) => date.toDateString());
```

#### [useContext](https://react.dev/reference/react/useContext)

`useContext` is a hook that allows you to use a context in a component. It takes a context object as an argument and returns the current context value. Should be defined outside the component as it will cause the component to rerender when the context changes. Better use Redux.

```jsx
import { createContext } from "react";

const initialState = {
  first: "Jack",
  last: "Herrington",
};

export type UserState = typeof initialState;

const context = createContext < typeof initialState > initialState;

const value = useContext(context);
```

#### [useRef](https://react.dev/reference/react/useRef)

`useRef` returns a mutable ref object whose `.current` property is initialized to the passed argument. It's useful for storing mutable values that don't cause a rerender when they change. It's also useful for storing values that are expensive to compute.

```jsx
const ref = useRef(initialValue);
```

#### [use](https://react.dev/reference/react/use)

`use` is a hook that allows you to use a promise in a component. It takes a promise as an argument and returns an object with the promise's current state. Should be defined outside the component as it will cause the component to rerender when the promise resolves. Better use Redux. can be used for conditional hooks.

```jsx
const promise = use(promise);
```

#### [useReducer](https://react.dev/reference/react/useReducer)

`useReducer` is a hook that allows you to use a reducer in a component. It takes a reducer and an initial state as arguments and returns an array with the current state and a dispatch function. Should be defined outside the component as it will cause the component to rerender when the state changes. Better use Redux.

```jsx
import React, { useReducer } from "react";

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

#### [useSyncExternalStore](https://react.dev/reference/react/useSyncExternalStore)

`useSyncExternalStore` is a hook that allows you to use a store in a component. It takes a subscribe function that returns a function that unsubscribes (cleanup) and a getSnapshot function as arguments and returns the current state of the store. Should be defined outside the component as it will cause the component to rerender when the store changes. Better use Redux.

```jsx
import { useSyncExternalStore } from "react";
import { todosStore } from "./todoStore.js";

function TodosApp() {
  const todos = useSyncExternalStore(
    todosStore.subscribe,
    todosStore.getSnapshot
  );
  // ...
}
```

## Best Practices

### Don't define components inside components

Defining components inside components will cause them to be redefined on every render. This will cause the component to be unmounted and remounted every time the parent component renders. This will cause the component to lose its state and any side effects will be run again.

Bad:

```jsx
function Parent() {
  function Child() {
    return <div>Child</div>;
  }

  return <Child />;
}
```

Good:

```jsx
function Child() {
  return <div>Child</div>;
}

function Parent() {
  return <Child />;
}
```

### Destructoring props

Destructuring props makes it easier to read and write components. It also makes it easier to see what props are being used in a component.

Bad:

```jsx
function MyComponent(props) {
  return <div>{props.name}</div>;
}
```

Good:

```jsx
function MyComponent({ name }) {
  return <div>{name}</div>;
}
```

### Lazy loading

Lazy loading is a technique that allows you to load components only when they are needed. This can improve performance by reducing the amount of code that needs to be loaded. Suspense is a React component that allows you to wrap lazy loaded components and display a loading indicator while the component is loading.

Bad:

```jsx
import React from "react";

import Component1 from "./Component1";
import Component2 from "./Component2";
import Component3 from "./Component3";

const MyComponent: React.FC = () => {
  return (
    <div>
      <Component1 />
      <Component2 />
      <Component3 />
    </div>
  );
};

export default MyComponent;
```

Good:

```jsx
import React, { Suspense } from "react";

const Component1 = React.lazy(() => import("./Component1"));

const MyComponent: React.FC = () => {
  return (
    <div>
      <Suspense fallback={<div>Loading...</div>}>
        <Component1 />
      </Suspense>
    </div>
  );
};

export default MyComponent;
```

### Higher order components

Higher order components are functions that take a component as an argument and return a new component. They are useful for adding functionality to components without changing their implementation. They can be used to add state, props, or other functionality to components.

Bad:

```jsx
import React from "react";

const MyComponent: React.FC = () => {
  return <div>MyComponent</div>;
};

export default MyComponent;
```

Good:

```jsx
import React from "react";

const withCounter = (Component: React.FC) => {
  const initialState = { count: 0 };

  const Counter: React.FC = () => {
    const [state, setState] = useState(initialState);

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

### Compound components

Compound components are components that share state and props. They are useful for creating reusable components that can be used in different ways. They can be used to create components that can be used in different ways.

```jsx
<Component>
  <Component.Item />
  <Component.Item />
  <Component.Item />
</Component>
```

```jsx
// index.tsx
export const Component: Props = Object.assign(Component, {
  Item: ComponentItem,
});
```

[Compound Components](https://github.com/Klerith/react-adv/blob/component-compound/src/02-component-patterns/components/index.ts)

### React-query

```jsx
import { useQuery } from "react-query";

const fetchUsers = async () => {
  const res = await fetch("https://jsonplaceholder.typicode.com/users");
  return res.json();
};

const Users = () => {
  const { data, isLoading, error } = useQuery("users", fetchUsers);

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  return (
    <div>
      {data.map((user) => (
        <div key={user.id}>{user.name}</div>
      ))}
    </div>
  );
};

export default Users;
```

### Use shorthand for boolean props

```jsx
// Bad
<Checkbox checked={true} />

// Good
<Checkbox checked />
```

### Avoid curly braces for string props

```jsx
// Bad
<Checkbox label={"Checkbox"} />

// Good
<Checkbox label="Checkbox" />
```

### Keep props key unique

```jsx
// Bad
<Checkbox key={1} />

// Good
<Checkbox key="1-1" />
```

## Architecture

### Application Requirements

- Functional Requirements: What the app do
- Non-Functional Requirements:
  - Performance
  - Usability
  - SEO

### Technical Decisions

- Project Structure: Feature-based, Domain-based, or Layer-based
- Rendering Strategy: SSR, CSR, or static site gqenerator
- State Management: Local, Global, Server, Form and URL state
- Styling: Component library
- Authentication: cookies, JWT, OAuth, or OpenID
- Testing: Unit, Integration, E2E, or Visual Regression

### Project Structure

- components: Reusable UI components
- config: configuration files
- features: feature-based modules
  - api: API calls
  - components: feature-specific components
  - types: feature-specific type definitions
  - index.ts*: feature entry point
- layouts: page layouts
- lib: configuration for external libraries
- pages: route-based pages
- providers: global state providers
- stores: global state stores
- testing: test utilities
- types: type definitions
- utils: utility functions

#### Clean Architecture

- Domain - Models/State: Interfaces, clases que son entidades de negocio. State es el estado de la aplicación
- Components: Bussiness logic, UI logic, and UI components
- Adapters: User Interface, API, y routing
- External Services: API, storage, and routing

Folder structure:

- adapters
- assets
- components
- contexts
- hooks
- interceptors
- models
- pages
- redux
- services
- styled-comopoents
- utils

- Model: redux, context, models
- Components: components, utilities, hooks
- Adapters: adapters, interceptors
- External Services: services

### Quality Assurance

- Typecheck: TypeScript
- Lint: ESLint
- Format: Prettier
- Pre-commit: Husky, lint-staged
- Components: Chakra UI, Storybook

#### Prettier

```json
{
  "scripts": {
    "prettier": "prettier \"**/*.+(json|ts|tsx)\"",
    "format:check": "npm run prettier -- --check",
    "format:fix": "npm run prettier -- --write",
  }
}
```

#### Husky

```bash
npx husky add .husky/pre-commit "npx lint-staged"
```

```ts
// lint-staged.config.js
module.exports = {
  '*.{ts,tsx}': [
    'npm run lint',
    "bash -c 'npm run types:check'",
    'npm run format:check',
], };
```

#### Eslint

Enforce importing from feature index files

```ts
// .eslintrc.js
rules: {
    'no-restricted-imports': [
      'error',
      {
        patterns: ['@/features/*/*'],
}, ],
    'import/no-cycle': 'error',
      ... rest of the eslint rules
}
```

#### Chakra UI

```tsx
// src/providers/app.tsx
import {
  ChakraProvider,
  GlobalStyle,
} from '@chakra-ui/react';

import { ReactNode } from 'react';
import { theme } from '@/config/theme';
type AppProviderProps = {
  children: ReactNode;
};
export const AppProvider = ({
  children,
}: AppProviderProps) => {
  return (
<ChakraProvider theme={theme}> <GlobalStyle />
{children}
    </ChakraProvider>
); };
```

```tsx
// src/config/theme.ts
import { extendTheme } from '@chakra-ui/react';
const colors = {
  primary: '#1a365d',
  primaryAccent: '#ffffff',
};
const styles = {
  global: {
    'html, body': {
      height: '100%',
      bg: 'gray.50',
    },
    '#__next': {
      height: '100%',
      bg: 'gray.50',
}, },
};
export const theme = extendTheme({ colors, styles });
```

## Design Patterns

### Provider

Is a component that provides a context to its children. It's useful for providing global state to components that need it. It's also useful for providing configuration to components that need it.

### Higher Order Component

HOC have no side effects, they are pure functions that take a component and return a new component. They are useful for adding functionality to components without changing their implementation. They can be used to add state, props, or other functionality to components.

### Presentational and Container Components

Presentational components are components that are concerned with how things look. They are responsible for rendering UI elements and don't have any business logic. Container components are components that are concerned with how things work. They are responsible for managing state and handling events.

### Hook

Custom hooks are functions that use other hooks to provide functionality to components. They are useful for sharing logic between components. They can be used to create reusable logic that can be used in different components.

### Render Props

Render props are components that take a function as a prop and call that function with data. They are useful for sharing logic between components. They can be used to create reusable logic that can be used in different components.

### Compound Components

Compound components are components that share state and props. They are useful for creating reusable components that can be used in different ways. They can be used to create components that can be used in different ways.

### Server Side Rendering, Static Rendering, Incremental Static Generation

Server Side Rendering is a technique that allows you to render components on the server and send the HTML to the client. This can improve performance by reducing the amount of code that needs to be loaded. Static Rendering is a technique that allows you to render components at build time and send the HTML to the client. This can improve performance by reducing the amount of code that needs to be loaded. Incremental Static Generation is a technique that allows you to render components at build time and send the HTML to the client. This can improve performance by reducing the amount of code that needs to be loaded.

## Diffing Algorithm

1. Start at the root of the tree using breadth-first search
1. Compare the type of the current node
1. Update if changes in attributes or styles

## References

- [React pro](https://github.com/Klerith/react-adv)
- [useContext](https://github.com/Klerith/useContext-TS)
- [React Application Architecture for Production](https://github.com/PacktPublishing/React-Application-Architecture-for-Production)
