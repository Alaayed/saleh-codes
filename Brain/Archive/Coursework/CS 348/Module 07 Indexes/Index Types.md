### Characteristics of Indexes
- Clustered/Unclustered
	- Clustered: data records are sorted in key search order
	- Unclustered: data records are NOT sorted in key search order
- Dense/Sparse
	- Dense: Every record has a corresponding index
	- Spares: NOT Dense
- Primary/Secondary
	- Primary = On the primary key (not sure if entire primary key, or if candidate key is considered)
	- Secondary = on any attribute
---
### Combos
- Clustered Dense:
	- Exactly how it sounds like
- Clustered Sparse:
	- One key PER data block---corresponding to the highest/lowest value in data block 
- Unclustered:
	- Usually occurs when you are indexing on a secondary attribute
