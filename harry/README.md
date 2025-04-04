# Hogwarts Quests - Assignment 2
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
- b. Since the instrument's noise follows N(0,4), the reading R given true distance t is distributed as N(t,4). We are looking to find P(R = 100|t). 
