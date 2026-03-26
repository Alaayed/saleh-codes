
---
### Atomicity
- All of it happens or none of it does
---
### Consistency 
- If the DB is in a consistent state (defined by user), it remains in a consistent state after a transaction
---
### Isolation 
- Other transactions should not affect the effect of other transactions
- It should be as if only the transaction was run on the DB by itself
--- 
### Durability
- If a transaction goes through, its effects will persist in the DB