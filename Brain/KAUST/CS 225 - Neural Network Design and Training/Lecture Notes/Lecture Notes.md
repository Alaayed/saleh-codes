

# Lec 2

##### Terms

Training set:
- Fits the model params
Validation set: 
- Determine hyper params
Test Set:
- Final evaluation of performance 

##### Error Function
Error function quantifies the difference between the predicated output vs actual output

$$E(W) =\frac{1}{2} \sum_{n=1}^N \{y(x_n,\mathbb{w})-t_n\}^2$$


##### Model Complexity
Goal: making accurate predictions for **unseen** test data instead of **training** data.

Root-mean-square (RMS) loss

$$E_{RMS} = \sqrt{\frac{1}{N} \sum_{n=1}^N \{y(x_n,\mathbb{w})-t_n\}^2}$$

Overfitting becomes less of an issue as the size of the data set $N$ increases

**Classical ML**: Data points should be at least 5/10 times more than model parameters
**DL:** Often great results with more network parameters rather than training samples

##### Regularization
As $M$ increase, the magnitude of the coefficients typically gets bigger.

![[Pasted image 20260902150548.png]]


Regularization: discourage the coefficients from having large magnitudes.
![[Pasted image 20260902150602.png]]


![[Pasted image 20260902150934.png]]

Early stopping is really popular, stop before the model gets crazy. Popular in both classic ML and DL 

![[Pasted image 20260902151123.png]]

This figure is the behaviour for classical ml

In DL, often the test error doesn't go up, but just stagnates/stays the same.

It is possible for training dynamics to emerge, it could stagnate, then after a while completely explodes.

# Tensor, Lec 2