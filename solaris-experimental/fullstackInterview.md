### How does javascript handle asynchronous code?

Javascript is a single threaded language, meaning it can only do one thing at a time. This is why asynchronous code is so important. Asynchronous code allows us to do multiple things at once. Javascript handles asynchronous code by using the event loop. The event loop is a queue of functions that are waiting to be executed. When an asynchronous function is called, it is added to the event loop. When the function is finished, it is removed from the event loop and the next function is executed.

### What is the difference between observable and promise?

A promise is a one time operation that can be resolved or rejected. An observable is a stream of data that can be subscribed to. Observables are more powerful than promises because they can be cancelled, they can emit multiple values, and they can be combined with other observables.

### Difference between old react lifecycle methods and new react lifecycle methods?

The old react lifecycle methods are componentWillMount, componentDidMount, componentWillReceiveProps, shouldComponentUpdate, componentWillUpdate, componentDidUpdate, and componentWillUnmount. The new react lifecycle methods are getDerivedStateFromProps, getSnapshotBeforeUpdate, and componentDidCatch. The old lifecycle methods are deprecated and should not be used. The new lifecycle methods are more powerful and should be used instead.

### How does react virtual dom work?

React virtual dom is a lightweight representation of the actual dom. It is used to speed up rendering by only updating the parts of the dom that have changed. React virtual dom is a tree of React elements. Each React element is a lightweight representation of a dom node. When a React element is rendered, it is converted into a dom node and added to the dom. When a React element is updated, it is converted into a new dom node and the old dom node is replaced with the new dom node.

### HTTP Methods

GET - Retrieves data from the server
POST - Sends data to the server
PUT - Updates data on the server
DELETE - Deletes data from the server
PATCH - Updates data on the server
HEAD - Retrieves headers from the server
OPTIONS - Retrieves options from the server
TRACE - Retrieves the request from the server

### Difference between hexagonal and clean architecture?

Hexagonal architecture is a software architecture that separates the application into layers. The layers are the domain layer, the application layer, the infrastructure layer, and the presentation layer. The domain layer contains the business logic. The application layer contains the application logic. The infrastructure layer contains the database and other external dependencies. The presentation layer contains the user interface. The layers are separated by interfaces. The interfaces are implemented by adapters. The adapters are responsible for translating the data between the layers. The hexagonal architecture is a good choice for large applications because it allows for easy testing and refactoring. The difference between hexagonal and clean architecture is that hexagonal architecture is a software architecture and clean architecture is a software design pattern. The hexagonal architecture is a good choice for large applications because it allows for easy testing and refactoring. The clean architecture is a good choice for small applications because it is simple and easy to understand.

Software architecture is the blueprint and a design pattern is the implementation.

### What is the difference between local storage and session storage?

the difference is that while data in localStorage doesn't expire, data in sessionStorage is cleared when the page session ends.

### React folder structure

```text
├── config
├── public
├── src
│   ├── components
│   ├── containers
│   ├── hooks
│   ├── pages
│   ├── services
│   ├── store
│   ├── styles
│   ├── types
│   ├── utils
│   ├── App.tsx
│   ├── index.tsx
│   └── react-app-env.d.ts
├── .gitignore
├── package.json
├── README.md
├── tsconfig.json
└── yarn.lock
```

### How does redux works

Redux is a state management library that allows you to manage the state of your application in a predefined way. It is a single source of truth that is shared between all components. It is a predictable state container that is immutable and can only be changed by dispatching actions. It is a functional programming paradigm that is based on the idea of pure functions. It is a declarative programming paradigm that is based on the idea of declarative programming. It is a declarative programming paradigm that is based on the idea of declarative programming. It is a declarative programming paradigm that is based on the idea of declarative programming. It is a declarative programming paradigm that is based on the idea of declarative programming. It is a declarative programming paradigm that is based on the idea of declarative programming. It is a declarative programming paradigm that is based on the idea of declarative programming. It is a declarative programming paradigm that is based on the idea of declarative programming. It is a declarative programming paradigm that is based on the idea of declarative programming.

### Programming Paradigms

#### Imperative Programming

Imperative programming is a program

#### Declarative Programming

Declarative programming is a program

#### Functional Programming

Functional programming is a program

#### Object Oriented Programming

Object oriented programming is a program

### Difference between types and interfaces

From the documentation for public exposed types you should use interfaces and mostly also it is recomended tu use interfaces over types because of the extensibility and the ability to merge interfaces. For private types you can use types. And interfaces also provide better error messages.

### What is a js closure?

A closure is a function that has access to the variables in its lexical scope even when the function is executed outside its lexical scope. A closure is created when a function is defined inside another function. The inner function has access to the variables in the outer function even when the outer function is executed outside its lexical scope.

### Difference between var, let and const

Var is function scoped, let and const are block scoped. Var can be redeclared and reassigned, let can be reassigned but not redeclared, and const can neither be reassigned nor redeclared. Var is hoisted, let and const are not hoisted. Var is initialized with undefined, let and const are not initialized.

### What is the difference between a promise and an observable?

A promise is a one time operation that can be resolved or rejected. An observable is a stream of data that can be subscribed to. Observables are more powerful than promises because they can be cancelled, they can emit multiple values, and they can be combined with other observables.

### What is the difference between a promise and a callback?

A promise is a one time operation that can be resolved or rejected. A callback is a function that is called when an asynchronous operation is completed. A promise is a better choice than a callback because it is easier to read and understand.

### What is the difference between a promise and an async/await?

A promise is a one time operation that can be resolved or rejected. An async/await is a syntactic sugar for promises. An async/await is a better choice than a promise because it is easier to read an^d understand.

### Map, filter, reduce

Map is a function that takes an array and returns a new array with the same length as the original array. Filter is a function that takes an array and returns a new array with the same length as the original array. Reduce is a function that takes an array and returns a single value.

### Map and forEach

Map is a function that takes an array and returns a new array with the same length as the original array. ForEach is a function that takes an array and returns undefined.

### When should you use redux?

Redux is a state management library that allows you to manage the state of your application in a predefined way. It is a single source of truth that is shared between all components. It is a predictable state container that is immutable and can only be changed by dispatching actions. It is a functional programming paradigm that is based on the idea of pure functions. It is a declarative programming paradigm that is based on the idea of declarative programming. It is a declarative programming paradigm that is based on the idea of declarative programming. It is a declarative programming paradigm that is based on the idea of declarative programming.
