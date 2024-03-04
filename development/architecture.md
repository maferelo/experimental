# Architecture

## Clean Architecture

### Dont put business logic in the controllers

The API layer should be as thin as possible. It should only be responsible for parsing the request, calling the appropriate use case, and returning the response. The business logic should be in the use cases.

```typescript
// Bad
class UserController {
  async createUser(req: Request, res: Response) {
    const user = req.body;
    // Business logic
    if (user.age < 18) {
      return res.status(400).send('User must be at least 18 years old');
    }
    // Save user
    await userRepository.save(user);
    res.status(201).send(user);
  }
}

// Good
class CreateUser {
  constructor(private userRepository: UserRepository) {}

  async execute(user: User) {
    if (user.age < 18) {
      throw new Error('User must be at least 18 years old');
    }
    await this.userRepository.save(user);
    return user;
  }
}

class UserController {
  async createUser(req: Request, res: Response) {
    const user = req.body;
    try {
      const createdUser = await createUser.execute(user);
      res.status(201).send(createdUser);
    } catch (error) {
      res.status(400).send(error.message);
    }
  }
}
```

## Refferences

- [Don't put your business logic in the controllers](https://blog.szymonmiks.pl/p/dont-put-your-business-logic-in-the-controllers/)