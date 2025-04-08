# Hogwarts Quests - Assignment 2

## n.1
1. You are tracking the distance to the Hogwarts Express. A magical instrument reports it’s 100 leagues away. Before the reading, your belief about
the distance D was a Gaussian D ∼ N(µ = 98, σ^2 = 16). The instrument’s
reading is the true distance plus Gaussian noise (N(0, 4)).
- a. What is the PDF of your prior belief of the train’s true distance?
- b. What is the probability density of seeing a reading of 100 leagues, given
the true distance is t?
- c. What is the PDF of your posterior belief (after the reading) of the
train’s true distance? (You can leave a constant and don’t need to
simplify).

## Solution 1
- a. Our belief about the distance D before the reading is given, as stated in the problem, by  D ∼ N(µ = 98, σ^2 = 16). <br> we know that the PDF of RV that follows a Normal distribution is given by: <br> <br> <img src="https://raw.githubusercontent.com/TondinL/KR---PE/main/harry/images/es_1a1.png" width="160"/> <br> sobstituting the values µ = 98, σ^2 = 16 we obtain the following distribution : <br> <br> <img src="https://raw.githubusercontent.com/TondinL/KR---PE/main/harry/images/es_1a2.png" width="400"/> <br>
- b. Since the instrument's noise follows N(0,4), the reading R given true distance t is distributed as N(t,4). We are looking to find P(R = 100|t). Sobstituting the values µ = t, σ^2 = 4 and x = 100 we get: <br> <br> <img src="https://raw.githubusercontent.com/TondinL/KR---PE/main/harry/images/es_1b1.png" width="270"/>
- c. 

## n.2
2. On average, 5.5 owls arrive at the Owlery per minute. What is the probability that:
- a. More than 7 owls will arrive in the next minute?
- b. More than 13 owls will arrive in the next 2 minutes?
- c. More than 15 owls will arrive in the next 3 minutes?

## Solution 2

For resolving this problem we can parametrize it with the Poisson distribution, where the Poisson random variable (discrete) gives the probability of a given number of events in a fixed interval, given the fact that we know the constant mean rate, in our case 5.5 owls per minute ( 11 for the case of two minutes and 16.5 for the case of three). For solving the computation of the probabiliy for the three points of the problem, i used the function poisson.cdf from the SciPy library. With the CDF F(x) we can calculate the cumulative probability  that a random variable takes on a value less than a number, so we will compute 1 - F(x) ,given the fact that we are computing the probability that it takes on a value greather than a number. The poisson.cdf function takes two parameters (integers), the number we computing the probability for and the lambda ( the constant mean rate ) of the distribution.

```python
from scipy.stats import poisson


lambda_1 = 5.5
P_a = 1 - poisson.cdf(7, lambda_1)


lambda_2 = lambda_1*2
P_b = 1 - poisson.cdf(13, lambda_2)


lambda_3 = lambda_1*3
P_c = 1 - poisson.cdf(15, lambda_3)

print("a. P(X > 7) =", round(P_a, 3))
print("b. P(X > 13) =", round(P_b, 3))
print("c. P(X > 15) =", round(P_c, 3))
```
The output is :

- a. P(X > 7) = 0.191
- b. P(X > 13) = 0.219
- c. P(X > 15) = 0.582

## n.3
3. The median of a continuous random variable (like the height of a gnome)
having cumulative distribution function F is the value m such that F(m) =
0.5. Find the median of X (in terms of distribution parameters) if:
- a. X ∼ Uni(a, b) (Uniform distribution, like the spread of Floo powder).
- b. X ∼ N(µ, σ2) (Normal distribution, like scores on the O.W.L.s).

## Solution 3

- a. given that  X ∼ Uni(a, b), we know that the PDF is f(x) = 1/(b-a) when a =< x =< b and 0 otherwise. We also know the CDF of the uniform distribution, F(x) = 0 for x < a , F(x) = (x-a)/(b-a) for a =< x =< b, and F(x) = 1 for x > b. We are looking for m such that F(m) = 5; <br> (m-a)/(b-a) = 0.5 <br> m-a = (b-a)/2 <br> m = a + (b-a)/2 = (b+a)/2 , this is equal to the mean of the distribution, m = µ .
- b. in a normal distribution, X ∼ N(µ, σ^2), the mean and the median are equal (same for the uniform distribution),<br> m = µ,<br> this is given from the simmetry of the distribution with respect to its center ( µ ).

## n.4
4. Let Xi be the number of students visiting the Hogwarts library in week i,
where Xi ∼ N(2200, 52900). Assume weekly visits Xi are independent.
- a. What is the probability that the total number of visitors in the next
two weeks exceeds 5000?
- b. What is the probability that the weekly number of visitors exceeds 2000
in at least 2 of the next 3 weeks?

# Solution 4

- a. The total number of visitors in the next two weeks is the sum of two independent random variables X1 and X2 <br> S = X1 + X2 <br> Since X1 and X2 are both normally distributed, their sum S will also be normally distributed, with µ<sub>s</sub> = µ<sub>X1</sub> + µ<sub>X2</sub> = 4400 and σ<sup>2</sup><sub>s</sub> = σ<sup>2</sup><sub>X1</sub> + σ<sup>2</sup><sub>X2</sub> = 105800 <br> S ∼ N(4400, 105800) <br> Given that there is no closed form for the integral of the Normal PDF, and as such there is no closed form CDF, we will use the precomputed function Ω that represents that CDF of the Standard Normal. For this we will need to find a linear transform from S to the standard normal Z ∼ N(0,1). <br> This standardization is given by Z = (x -  µ<sub>s</sub>)/σ<sub>S</sub> = (x - 4400)/325 <br> - a. The total number of visitors in the next two weeks is the sum of two independent random variables \( X_1 \) and \( X_2 \)  
  \( S = X_1 + X_2 \)  
  Since \( X_1 \) and \( X_2 \) are both normally distributed, their sum \( S \) will also be normally distributed, with  
  \( \mu_S = \mu_{X_1} + \mu_{X_2} = 4400 \) and \( \sigma_S^2 = \sigma_{X_1}^2 + \sigma_{X_2}^2 = 105800 \)  
  \( S \sim \mathcal{N}(4400, 105800) \)  
  Given that there is no closed form for the integral of the Normal PDF, and as such there is no closed form CDF, we will use the precomputed function \( \Omega \) that represents the CDF of the Standard Normal. For this, we will need to find a linear transform from \( S \) to the standard normal \( Z \sim \mathcal{N}(0,1) \).  
  This standardization is given by:  
  \[
  Z = \frac{S - \mu_S}{\sigma_S} = \frac{S - 4400}{325}
  \]


