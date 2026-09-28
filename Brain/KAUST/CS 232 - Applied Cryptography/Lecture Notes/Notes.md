

# Lecture 1

Investigate: Selective repudiability, Traitor Tracing, group signature, AES

crypto goals:
- **Prevention:** Prevent disclosure of sensitive info.
- **Deterrence:** Visibly strong defense or penalties to attack. Rate limiting or response staggering (200ms delay, nothing for a normal user but painful for an attacker). 
- **Detection:** Detect an attack, provide proof
- **Assumption:** Attackers are rational and will not attack a system if loses exceed gains.


Cybersecurity Generic Goals: 
- **Confidentiality:** Disallows an attacker disclosing info defined as confidential
	- **Encryption**
- **Integrity** (Detect that an adversary has modified an asset)
	- **Blockchain, accumulators hash functions**
- **Authenticity** you know who sent what
	- **MAC**
	- **Dig. Sig.**
- **Availability** the resource you want to access is there when you want it
	- **POW**

##### Security 
Security should be defined against the attackers capabilities, not his strategy.

Must precisely articulate an attack model and security requirements.
**The attacker model principle:** ASSUME CAPABILITIES, NOT STRATEGY

##### Principles
**P1** formulate rigorous and precise definition of security
**P2** If an assumption is unproven, it must be defined and be as minimal as possible.
**P3** Crypto constructs should be accompanied with a security proof. (Reality is a mess, often not provided as this requires rigorous mathematical proofs. )
##### Assumptions
Most crypto requires compute assumptions 
Assumptions must be explicit

Allows reseachers to validate them.
Allows meaningful comparision, allowing you to reach a better objective
Practical implications if assumptions are wrong

##### Proofs of security
Proofs are crucial in cryptography where attackers are trying to break the scheme. 

Thats why crypto is still an art, many crypto schemes cannot be modeled using math, and even proofs may be broken if their assumptions are violated.

good adversaries need to compromise time, as the system loses coherence. Always attempts to falsify assumptions. Timing attacks are the first assumptions to be violated.

# Lec 2, Classical Cryptography

initially, private key cryptography was king until the 1970s.

Private key encryption shceme is defined by algos (Gen, Enc, Dec).
**Gen:** How to gen the key


##### Kerckhoff's principle 

The Encryption scheme is not a secret.
- the attacker knows the enc scheme.
- the only secret is key
- the key must be random AND kept secret.
  
Arguments in favor of this principle:
- Easier to keep the key secret
- Easier to change the key rather than algo
- Stadardization
	- ease of deployment
	- public scrutiy
	  
	  
**Computational Security** Given limited compute, the cipher cannot be broken
**Unconditional Security** The cypher cannot be broken because he does not have sufficient information.

##### Cryptosystem

5 Tuple (E,D,M,K,C):
- M set of plain text
- K set of keys
- C set of cyphertext
- E set of enc functions
- D set of dec functions

# Lec 3 
The cypher is considered broken if the adversary can compute any function on the plain text. For example f is the number of 0's in the message.
$$f(m)$$