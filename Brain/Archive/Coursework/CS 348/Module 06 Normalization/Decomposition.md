### Dependency Preservation
- This is an issue with decomposition when ( X -> Y -> Z)
- If you split into tables X,Y and Y,Z we lose the transitive FD X -> Z, so we need to include the relation X,Z.
---
### Lossless
- If a natural join reproduces the original table 
- *Guaranteed* if the attributes in common between two relations are keys, the decomposition is lose less
--- 
