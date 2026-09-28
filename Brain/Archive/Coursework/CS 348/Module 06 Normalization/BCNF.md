Everything in [[3NF]] with a little extra:

Every FD in the table must be a dependency on a candidate key (or super set of a candidate key)
Unless the FD is trivial, then it doesn't matter. 

Another way:
- For any FD ( X -> Y ) X must be a superkey
- Everything relies on a superkey 

