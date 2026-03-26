$r = \text{annulized rate of return}$
### Zero Coupon Bonds
$$ PV = FV (1 + r)^{-N}$$
### Annual Coupon Bonds
In human, sum all the coupon payments and consider them as mini zero coupon bonds. Depending on the $r_y,r_c$ relationship the bond is sold at these levels:
$$\begin{cases} 
\text{premium}& \text{if } r_y< r_c\\
\text{face value}& \text{if } r_y \equiv r_c \\
\text{discount}& \text{if } r_y > r_c
\end{cases}$$
$$PV = \sum _ {i = 1} ^ {N}\frac{FV* r_c}{(1+r_y)^{i}} \;\; + FV *(1+r_y)^{-N} $$
$$PV = FV(r_c * \frac{1-(1+r_y)^{-N}}{r_y} + (1+r_y)^{-N})$$
$$PV = FV(r_c * \frac{1 - (1+r_y)^{-N} + r_y(1+r_y)^{-N}}{r_y})$$
$$PV = FV(r_c * \frac{1 + (r_y- 1)(1+r_y)^{-N}}{r_y})$$
### Perpetual Bonds
Bonds that payout coupons forever
$$PV = \frac{\text{payment}}{r}$$
### Amortizing bonds
Bonds that pay off the principle over the coupon payments.
$$\text{annuity payments} = \frac{r \cdot PV}{1- (1+r)^{-t}}$$

