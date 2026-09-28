### Functional Dependency

- Given attributes \( X \) and \( Y \), \( X -> Y \) means:  
  *for any two tuples, if they agree on \( X \), they must agree on \( Y \).*  
  We say **\( Y \) is functionally dependent on \( X \)**.
---
### Trivial Functional Dependency
-  Any dependency ( X -> Y ) where Y \in X
---

### Troublesome Functional Dependency

- A functional dependency \( X -> Y \) is considered **troublesome** when:
  - \( X -> Y \),
  - and **\( X \) is not a superkey**.

---
Refer to [[Key]] for the definition of superkey


***Note:***
- Y can also be a candidate key in an FD. Not sure if this is gonna come, but it can happen.
- 