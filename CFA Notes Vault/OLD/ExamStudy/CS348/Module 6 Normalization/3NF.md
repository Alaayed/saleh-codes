Everything in [[2NF]] and the following: 
Insure that NO transitive dependencies exist.
For Example, take:

|player_id|skill_level|rating|

if {player_id} -> {skill_level} -> {rating}

rating depends on skill level---a non-key attribute. This is a transitive dependency and is not allowed

Summary:

Everything in the table should depend on the key, the whole key and NOTHING but the key
