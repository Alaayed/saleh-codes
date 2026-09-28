File -> 1...m Page
Page -> 1...m Record
Record  -> 1 Row

IO operations occur in blocks. If you want something in a block, you bring the whole block. If you want to write something to a block, you overwrite the whole block.

---
### Files
- **Data File**
	- Has data corresponding to a relation 
- **Index File**
	- File containing the indexes
- All files consist of blocks/pages
- /# index files < /# data files