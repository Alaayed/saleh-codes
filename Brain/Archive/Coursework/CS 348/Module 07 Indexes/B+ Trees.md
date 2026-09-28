![[Pasted image 20250427141508.png]]

--- 
### Parameters
- d
	- Min number of keys per node (Except Root, including leaves)
- n
	- Max number of key per node  (Except Root, including leaves)
	- Usually 2d, since when you a node reaches n it can split into two nodes---both of which contain d keys

---

### When are B+ Trees helpful
- Exact Queries
	- age = 10
- Range Queries
	- 10 <= age <= 20
- Hash indexes are only good for exact matche

---
### Best value for d?
- 170, why?
-  keys = 4 bytes, pointers = 8 bytes
-  block = 4094, want to store each internal node in one block
- 2d * 4 + (2d+1) * 8 <= 4094
---
### Typical value for d
- 100, with a fill rate of 2/3
- most internal nodes have 130 keys

---

### Alternative 1
Store the data entries in the leaf nodes
Issue with this is that the index basically acts like an organized version of the data, and is very inefficient for larger values.