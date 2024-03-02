# React Application Architecture for Production

## Application Requirements

- Functional Requirements: What the app do
- Non-Functional Requirements:
  - Performance
  - Usability
  - SEO

## Technical Decisions

- Project Structure: Feature-based, Domain-based, or Layer-based
- Rendering Strategy: SSR, CSR, or static site gqenerator
- State Management: Local, Global, Server, Form and URL state
- Styling: Component library
- Authentication: cookies, JWT, OAuth, or OpenID
- Testing: Unit, Integration, E2E, or Visual Regression

## Project Structure

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

## Quality Assurance

- Typecheck: TypeScript
- Lint: ESLint
- Format: Prettier
- Pre-commit: Husky, lint-staged
- Components: Chakra UI, Storybook

### Prettier

```json
{
  "scripts": {
    "prettier": "prettier \"**/*.+(json|ts|tsx)\"",
    "format:check": "npm run prettier -- --check",
    "format:fix": "npm run prettier -- --write",
  }
}
```

### Husky

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

### Eslint

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

### Chakra UI

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

## References

- [React Application Architecture for Production](https://github.com/PacktPublishing/React-Application-Architecture-for-Production)
