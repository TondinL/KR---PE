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

## Solution 4

- a. The total number of visitors in the next two weeks is the sum of two independent random variables X1 and X2 <br> S = X1 + X2 <br> Since X1 and X2 are both normally distributed, their sum S will also be normally distributed, with µ<sub>s</sub> = µ<sub>X1</sub> + µ<sub>X2</sub> = 4400 and σ<sup>2</sup><sub>s</sub> = σ<sup>2</sup><sub>X1</sub> + σ<sup>2</sup><sub>X2</sub> = 105800 <br> S ∼ N(4400, 105800) <br> Given that there is no closed form for the integral of the Normal PDF, and as such there is no closed form CDF, we will use the precomputed function Ω that represents that CDF of the Standard Normal. For this we will need to find a linear transform from S to the standard normal Z ∼ N(0,1). <br> This standardization is given by Z = (x - µ<sub>s</sub>)/σ<sub>S</sub> = (x - 4400)/325 <br> P(x > 5000) = P(Z > (5000 - 4400) / 325) = P(Z > 600 / 325) = P(Z > 1.846) <br> To compute P(Z > 1.846) we use the standard normal distribution table: <br> [Standard Normal Distribution Table - University of Arizona](https://math.arizona.edu/~rsims/ma464/standardnormaltable.pdf)
<br> Given that  P(Z > 1.846) = 1 -  P(Z =< 1.846). <br> 1 − 0.967 = 0.033 . Thats the probability that the total number of visitors in the next two weeks exceeds 5000.
- b. For resolving this problem we will proced in two steps. Initialy we need to compute the probability that the number of visitors exceeds 2000 in one week. Then, given the fact that each week is indipendent from the other we will modell the problem as a binomial random variable with p equal to the probability computed in the first step. <br> For the firts step we will proceed in the same way as in the point a. We need to normalize the distribution and then use the precomputed function Ω that represents that CDF of the Standard Normal. <br> Here Z =  (x - µ<sub>s</sub>)/σ<sub>S</sub> = (x - 2200)/230 <br> P(x > 2000) = P(Z > (2000 - 2200) / 230) = P(Z > -0.87) <br> To compute P(Z > -0.87) we use the standard normal distribution table : <br> 1 - 0.192 = 0.808 <br> So the probability that in one week visitors exceeds 2000 is 0.808. <br> Now we model the problem as a Binomial random variable X ~ Bin(n,p) with p = 0.808 and n = 3. We need to compute P(X => 2) = P(X = 2) + P(X = 3). <br> Using the formula of the binomial P(X = k) = (3 choose k)p<sup>k</sup>(1-p)<sup>3-k</sup> <br>
- P(X = 2) = (3 choose 2) · (0.808)<sup>2</sup> · (1 - 0.808)<sup>1</sup> = 3 · 0.653 · 0.192 ≈ 0.376
- P(X = 3) = (3 choose 3) · (0.808)<sup>3</sup> = 1 · 0.527 ≈ 0.527
- P(X ≥ 2) = P(X = 2) + P(X = 3) = 0.376 + 0.527 = 0.903


## n.5
5. Let X, Y , and Z be independent random variables representing the magical power levels of three Hogwarts students, where X ∼ N(µ1, σ1^2) (Gryffindor), Y ∼ N(µ2, σ2^2) (Hufflepuff), and Z ∼ N(µ3, σ3^2) (Ravenclaw).
- a. Let A = X + Y . What is the distribution of the combined power A?
- b. Let B = 5X + 2. What is the distribution of B (perhaps after a powerenhancing charm)?
- c. Let C = aX − bY + c2Z, where a, b, and c are real-valued constants representing spell modifiers. What is the distribution (and parameters) for C? Show how you derived your answer.

## Solution 5
- a. Since the sum of independent normal random variables is also normally distributed, the combined variable
A = X + Y follows a normal distribution with µ<sub>A</sub> = µ<sub>X</sub> + µ<sub>Y</sub> and σ<sup>2</sup><sub>A</sub> = σ<sup>2</sup><sub>X</sub> + σ<sup>2</sup><sub>Y</sub>. This is a well-known property of the normal distribution.<br> *[From the CS109 Coursebook](https://chrispiech.github.io/probabilityForComputerScientists/en/)* <br> 
So the distribution is A ~ N(µ<sub>X</sub> + µ<sub>Y</sub>, σ<sup>2</sup><sub>X</sub> + σ<sup>2</sup><sub>Y</sub>).
- b. If X is a Normal such that X ~ N(µ, σ<sup>2</sup>) and Y is a linear trasform of X such that Y = aX + b then Y is also a Normal where: <br> Y ~ N(aµ + b, a<sup>2</sup>σ<sup>2</sup>). <br> In our case B ~ N(5µ + 2, 25σ<sup>2</sup>).
- c. Given the proprieties used in point a and b, becouse the variables are independent: <br> µ<sub>C</sub> = aµ<sub>X</sub> - bµ<sub>Y</sub> + c<sup>2</sup>µ<sub>A</sub> <br> σ<sup>2</sup><sub>C</sub> = a<sup>2</sup>σ<sup>2</sup><sub>X</sub> - b<sup>2</sup>σ<sup>2</sup><sub>Y</sub> + c<sup>4</sup>σ<sup>2</sup><sub>Z</sub>

## n.6

6. The joint probability density function of continuous random variables X
(skill in Potions) and Y (skill in Charms) is given by fX,Y (x, y) = c y/x
where 0 < y < x < 1.
- a. What is the value of c for this to be a valid probability density function?
- b. Are Potion skill (X) and Charm skill (Y) independent? Explain.
- c. What is the marginal density function of X?
- d. What is the marginal density function of Y?

## Solution 6

- a. <br> <br> <img src="https://raw.githubusercontent.com/TondinL/KR---PE/main/harry/images/es_6a.png" width="400"/> <br>
- b. Intuitively we can see that the costraint about the domain y < x imposes a dendence; once you  know the value of x, the value of y must be less than. Further more, two discrete random variables X and Y are called indipendent if f<sub>X,Y</sub>(x,y) = f<sub>X</sub>(x)*f<sub>Y</sub>(y), and from the point c and d where sono rappresentati i marginali di X e Y we see that the joint density function can not be factored in f<sub>X</sub>(x)*f<sub>Y</sub>(y)
- c. for computing the marginal density function of X, we need to integrate the joint density function over y, obtaining 2x , 0 < x < 1
- same as in the last point but we need to integrate over x, to obtain the marginal density function of y, wich is -4yln(y) ,  0 < y < 1

## n.7

7. Choose a number X at random from the set of house points {1, 2, 3, 4, 5, 6}
awarded by Professor McGonagall. Now choose a number Y at random
from the subset of points no larger than X, {1, . . . , X}.
- a. Determine the joint probability mass function of X (initial points) and
Y (second random selection).
- b. Determine the conditional mass function P(X = j|Y = i) as a function
of i and j.
- c. Are X and Y independent? Explain.

## Solution 7

- a. X and Y are discrete random variables, we want to compute the PMF P(x,y), with P(X = x) = 1/6 (uniform over {1, ... ,6} and P(Y = y|X = x) = 1/x if 1 =< y =< x and 0 otherwise. We can compute the joint probability P(x and y) with the product rule P(x,y) = P(x)*P(y|x) = 1/6x if 1 =< y =< x =< 6 and 0 otherwise.
- P(X = j | Y = i) = 
  {
    1 / j &div; (&#8721;<sub>k=i</sub><sup>6</sup> 1 / k),  if j &ge; i  
    0, otherwise
  }
