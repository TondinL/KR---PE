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
- a. Our belief about the distance D before the reading is given, as stated in the problem, by  D ∼ N(µ = 98, σ^2 = 16). <br> we know that the PDF of RV that follows a Normal distribution is given by: <br>  <img src="https://raw.githubusercontent.com/TondinL/KR---PE/main/harry/images/es_1a1.png" width="160"/> <br> sobstituting the values µ = 98, σ^2 = 16 we obtain the following distribution : <br> <img src="https://raw.githubusercontent.com/TondinL/KR---PE/main/harry/images/es_1a2.png" width="400"/> <br>
- b. Since the instrument's noise follows N(0,4), the reading R given true distance t is distributed as N(t,4). We are looking to find P(R = 100|t). Sobstituting the values µ = t, σ^2 = 4 and x = 100 we get <br> <img src="https://raw.githubusercontent.com/TondinL/KR---PE/main/harry/images/es_1b1.png" width="240"/>

## n.2
2. On average, 5.5 owls arrive at the Owlery per minute. What is the probability that:
- a. More than 7 owls will arrive in the next minute?
- b. More than 13 owls will arrive in the next 2 minutes?
- c. More than 15 owls will arrive in the next 3 minutes?

## Solution 2

For resolving this problem we can parametrize it with the Poisson distribution, where the Poisson random variable (discrete) gives the probability of a given number of events in a fixed interval, given the fact that we know the constant mean rate, in our case 5.5 owls per minute ( 11 for the case of two minutes and 16.5 for the case of three). For solving the computation of the probabiliy for the three points of the problem, i used the function poisson.cdf from the SciPy library.


## Owl Arrival Probability Analysis

To resolve this problem, we model it using the **Poisson distribution**. The Poisson distribution is used to estimate the probability of a given number of discrete events occurring in a fixed time interval, assuming we know the constant mean rate.

In our case, the mean arrival rate is 5.5 owls per minute. Therefore:
- For 1 minute: λ = 5.5  
- For 2 minutes: λ = 11  
- For 3 minutes: λ = 16.5  

To compute the probabilities for the three parts of the problem, we use the `poisson.cdf` function from the **SciPy** library, which returns the cumulative distribution function (CDF):

\[
P(X \leq k) = \sum_{i=0}^{k} \frac{e^{-\lambda} \cdot \lambda^i}{i!}
\]

Since the question asks for the probability that **more than** a certain number of owls arrive, we compute:

\[
P(X > k) = 1 - P(X \leq k)
\]

Here is the Python code used:

```python
from scipy.stats import poisson

# a. More than 7 owls in 1 minute (λ = 5.5)
lambda_1 = 5.5
P_a = 1 - poisson.cdf(7, lambda_1)

# b. More than 13 owls in 2 minutes (λ = 11)
lambda_2 = 11
P_b = 1 - poisson.cdf(13, lambda_2)

# c. More than 15 owls in 3 minutes (λ = 16.5)
lambda_3 = 16.5
P_c = 1 - poisson.cdf(15, lambda_3)

print("a. P(X > 7) =", round(P_a, 3))
print("b. P(X > 13) =", round(P_b, 3))
print("c. P(X > 15) =", round(P_c, 3))
