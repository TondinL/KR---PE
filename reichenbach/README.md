# The Reichenbach Reckoning: Sherlock Holmes’ Mathematical Mysteries
## Written Problems:
### 1. The Seating of the Diogenes Club

Sherlock Holmes investigates a clandestine meeting at the Diogenes Club, where 10 distinct members must sit in a row under strict protocols:
- a. If no rules bind their arrangement, how many ways can the silent gentlemen be seated?
- b. Suppose Mycroft Holmes and his aide, bound by mutual distrust, must sit side-by-side to monitor each other—how many arrangements are possible?
- c. If 5 are seasoned inspectors and 5 are novice constables, and no two of the same rank may sit adjacent (lest rivalries flare), how many seating orders hold?
- d. If the 10 form 5 pairs of informants and handlers, each pair inseparable due to whispered secrets, how many arrangements emerge?
Deduction: Explain your reasoning as if briefing Watson on the club’s hidden hierarchy.

### 1. Solution

- a.  There are 10 different options for the first seat, 9 for the second, 8 for the third, and so on until the last seat where there is only one option left. The solution is given by the permutation rule of n (n = 10) distinct objects <br> 10! = 10 * 9 * 8 * ... * 1 = 3628800
- b. We can consider Mycroft Holmes and his aide as a single element, in this way we can reason as for point a, and we obtain 9! . For each of this distinct arrangements, we need to consider the case where Mycroft Holmes sits on the right and his aide on the left and vice versa, so we need to multiply the obtained result by a factor of 2: <br> 2 * (9!) = 725760
- c. The only way to meet the given constraint is to have the two groups sit alternately. Now for each distinct group we have 5! different arrangements <br> 5! * 5! ( We multiply becouse for each arrangement of group 1 we have 5! different arrangements of group 2) <br> We have to consider now the case where we start with an element of group 1 or group 2, so we need to multiply the obtained result by a factor of 2 <br> 2 * (5! * 5!) = 28800
- d. We can reason as for point b and consider each pair as a single element, in this way we obtain 5! different arrangements. Now we need to calculate all the ways in which the elements of the pair can interchange with each other to form a distinct arrangment, and this is given by 2! , this for each of the 5 pairs, so we multiply 2! five times, and the final result is given by: <br> (2!)^5 * 5! = 3840

### 2. The Cipher Arrays of Irene Adler
Irene Adler hides messages in sorted arrays of k distinct integers, each from 1 to n (e.g., 1 ≤ x[0] < x[1] < … < x[k-1] ≤ n). How many such arrays can she devise, as if concealing clues in a locked box?

### 2. Solution
We can consider the permutations of all n integers, then select the first k, and divide the result for the permutation of the k selected integers and the (n - k) unselected integers, this becouse we do not care about the order of them. This gives us <br> n! / ((k! * (n - k)!) <br> this is the combinations formula of ( n choose k )

### 3. The Paths of the Hound
A mechanical hound roams an n × m grid from (1,1) to (n,m), moving only right or down:
- a. With no bounds, how many trails can it leave?
- b. If it must first lurch right (a faulty gear), how many paths remain?
- c. If it switches direction exactly thrice (right-to-down or down-to-right), how many routes obey?
Deduction: Track its steps as if hunting it across the moors.

### 3. Solution

 <img src="https://raw.githubusercontent.com/TondinL/KR---PE/main/reichenbach/Images/photo_2025-03-19_12-34-06.jpg" width="400"/>

<br> this is an example with n = 5 and m = 4
- a. As it can be seen from the above image, starting from the (1,1) cell , given the constraints, the mechanical hound is required to take  (n - 1) steps on the right (Rs) and (m -1) steps downward (Ds) to get to the (n,m) cell of the grid. So a total of (n + m -2) steps will be required for each possible trail, from which we need to understand where to put the Right steps and the downward ones. We can obtain the final result of all the possible trails by considering all the steps as distinct, taking the permutation of them and then dividing by the repetitions (Ds and Rs) <br> (n + m - 2)! / ((n - 1)! * (m - 1)!) <br> this is the same as ((n + m - 2) choose (n - 1)) = ((n + m - 2) choose (m -1)) <br> for the example given above of n = 5 and m = 4 , this gives us 35 different tails.
- b. Given that the first step must always be on the rigt, We can intepret the constraint as if the hound starts from the (1,2) cell, and count the possible trails from there. In this way, reasoning as in point a, there will be needed (n - 2) steps on the right and (m - 1) steps downwards, with a total of (n + m - 3) steps. <br> the solution in given by the formula ((n + m - 3) choose (n - 2)) = ((n + m - 3) choose (m - 1))  <br> for the example given above of n = 5 and m = 4 , this gives us 20 different tails.
- c. Given that we can change direction exactly three times, we can have trails in the form of Rs...|Ds...|Rs...|Ds... or Ds...|Rs...|Ds...|Rs... where Rs... and Ds... are groups of steps in the same direction, each >= 1, and | indicates the direction switch. To resolve this problem we can consider changes of direction ("|") as additional elememnts to the steps, so we will have (n + m - 1) total steps and 3 change-of-direction elements, with a total of (n + m + 1). We need to calculate where to put the change-of-direction elements and this can be done by the combination formula ((n + m + 1) choose 3) that will give us 3 distinct positions for the change of direction. We need to subtraact the illegal trails, where we have change of direction in the form of  Ds...|Rs...||Ds.. (a) or  Ds...|||Rs... (b) . This can be done considering the three ||| consecutive change of directions as a single element instead of three distinct elements and the two ||...| consecutive change of directions as two elements instead of three. We also need to multiply all for a factoer of two, considering the fact we start with a Rs step or a Ds step :
 <img src="https://raw.githubusercontent.com/TondinL/KR---PE/main/reichenbach/Images/es_3cc.jpg" width="400"/>


### 4. The Poker Game at Reichenbach
Holmes faces Moriarty at a poker table, where all 5-card hands from a 52-card deck are equally likely:
- a. What’s the chance of a flush (all same suit), including straight flushes?
- b. What’s the chance of two pairs (a, a, b, b, c, distinct values)?
- c. What’s the chance of four of a kind (a, a, a, a, b, distinct)?
Deduction: Compute the odds as if spotting Moriarty’s bluff.
 
### 4. Solution

The solutions of this question will be computed through the frequentist approach, where we will divide the favorable cases for the total cases. The total cases are given by all the possible hand of 5 cards from a deck of 52: <br>
(52 choose 5) = 2598960
- a. For computing the chances of having a flush, we can consider that there are 4 different suits, each composed of 13 different cards: <br> 4 * (13 choose 5) = 5148 <br> dividing for the total cases we get 0.00198
- b. For computing the chances of having two pairs (aabbc), for choosing the first card of the first pair (a) there are (13 choose 1) = 13 different options. For the (b) card, the first card of the second pair we have (12 choose 1) options, becouse it needs to be different from a. Now, for choosing the two cards of both pair we have (4 choose 2) different options. The last card (c) can be any card of the remaining 52 - 8 = 44 so we get the c card different from a or b. We also need to divide this for 2!, becouse we are overcounting the cases where we choose for example K for a and J for b and the vice versa, J for a and K for b. <br> 13 * 12 * (4 choose 2) * (4 choose 2) * 44 * 1/2 = 123552 <br>  dividing for the total cases we get 0.04754.
- c. To calculate the chances of having four of a kind (aaaab), we need to consider that there are 13 different possible pokers in the deck, one for each different card (without taking in consideration the last card). Once we choose one of the 13 cards we need to select all 4 of the different suits of that card, (13 choose 1) * (4 choose 4). For the b card we have 48 different options. <br> 13 * 48 = 624 <br> dividing for the total cases we get 0.00024

### 5. The Binary Telegram of Baskerville
A telegraph sends M 0’s and N 1’s in random order. What’s the chance the first r bits hold exactly k 1’s, as if decoding a hound’s howl?
Deduction: Reason through the static as if time is running out.

### 5. Solution

Given the problem, we have N + M total symbols, M 0's and N 1's. The probability of a symbol beeing a 1 can be otained by dividing the number of 1's by the total number of symbols <br> N / (N + M) <br> same for the 0's: <br> M/ (N + M) <br> We are trying to compute the probability of having k 1's in the firts r bits and k-r 0's. Each bit can be a 0 or a 1 with the probability given above. So the probability of having k 1's is (N / (N + M))^k and r-k 0's is (M / (N * M))^(r-k). We also need to consider al the possible different arrangement of 0's and 1's in the first r bits. This can be done using the formula (r choose k). the final formula is: <br>
 <img src="https://raw.githubusercontent.com/TondinL/KR---PE/main/reichenbach/Images/es_5.jpg" width="400"/>

### 6. The Menagerie of Moriarty
Holmes uncovers Professor Moriarty’s scheme to display 3 bird species and 3 reptile species, selected from 8 birds and 6 reptiles, in a sinister zoo:
- a. If Moriarty chooses freely, how many exhibits can he craft?
- b. Two birds—one a hawk with a piercing cry, the other a raven with a deadly glare—cannot coexist without chaos. How many exhibits avoid this peril?
- c. A venomous parrot and a cobra, when paired, unleash a toxic fog. How many exhibits dodge this trap?
Deduction: Justify your counts as if tracing Moriarty’s twisted logic.

### 6. Solution

- a. Moriarty has to choose 3 birds out of 8 and 3 reptile out of 6 to display. it means that he can craft (8 choose 3) * (6 choose 3) = 1120 different exhibits.
- b. For computing the new constraint, we can start from the previous result (total possible exhubuts) and subtract the illegal ones. <br> The illegal exhibits can be computed fixing the 2 birds that can not coexist together and computing all the possible combination with this two fixed. this can be obtained by: <br> (6 choose 1) * (6 choose 3) <br> the final formula is: <br> (8 choose 3) * (6 choose 3) -  (6 choose 1) * (6 choose 3) = 1000
- c. For this point we can reason as for point b, subtracting the illegal exhibits. In this case the illegal exhibits are given by <br> (7 choose 2) * (5 choose 2) <br> obtained fixing the 2 animals that can not coexist together. The final formula is: <br>  (8 choose 3) * (6 choose 3) -  (7 choose 2) * (5 choose 2) = 910

### 7. The Investments of Baker Street
Holmes secures £20 million to fund 4 shadowy enterprises, investing in £1 million units, each with a minimum stake: £1M, £2M, £3M, £4M.
- a. If all 4 must be funded to foil Moriarty’s network, how many strategies exist?
- b. If at least 3 must be backed (to keep the web intact), how many plans work?
Deduction: Argue your totals as if pitching to a wary Watson.

### 7. Solution

- a. If we consider that 10M are fixed among the 4 enterprises, we remain with 10M to invest. For each million we can choose each of the 4 different options, so we have 4^10 = 1048576 different strategies.
- b. Given the assumption that at least 3 must be backed, but onche we invest in one of the 4, we need to respect the minimum stake constraint,  we have 4 different outcomes, where al 4 are backed, the 1 with minimum stake at 1M remains uncovered, and same for the 2M, 3M and 4M. For each of this we can can reason as above and consider the minimum stakes as fixed and reason only on the other millions. We get: <br> 4^10 + 3^11 + 3^12 + 3^13 + 3^14 = 8134456 different strategies.

### 8. The Coding Conundrum of Scotland Yard
Holmes probes a cryptography school where 100 agents study 3 courses—Java, C++, Python—under Lestrade’s watch:
Java: 27 agents; C++: 28; Python: 20.
12 crack Java and C++; 5 master Java and Python; 8 excel in C++ and Python.
2 prodigies conquer all three.
- a. What’s the chance a random agent has evaded all courses, lurking in the shadows?
- b. What’s the chance an agent studies exactly one, avoiding the others’ scrutiny?
- c. If two agents are nabbed, what’s the odds at least one knows a course? Give a final number.
Deduction: Map the overlaps as if decoding a Yard cipher—explain each step.

### 8. Solution

### 9. The Passwords of the Naval Treaty
A spy tackles n distinct passwords, one unlocking a treaty:
- a. Trying randomly and discarding failures, what’s the chance the k-th attempt succeeds?
- b. Trying randomly without discarding, stopping at success, what’s the chance the k-th try wins?
Deduction: Think like the spy—explain as if Holmes is one step ahead.

### 9. Solution

- a. We need to select one among the wrong password (n - 1) out of n, with at each step reducing by one becouse we are discarding failures. so the chance that the k-th attempt succeds is given by: <br> <img src="https://raw.githubusercontent.com/TondinL/KR---PE/main/reichenbach/Images/es_9a.JPG" width="400"/> <br> Where 1/(n-k+1) is the probability of selecting the right password at the k-th attempt. We can notice that the fractions simplify each other in to 1/n.
- b. Without discarding, with the possibility of trying the same password multiple times, for each of the k-1 steps the probability of not choosing the correct password is (n-1)/n and the probablilty of choosing the correct at each step (also at the k-th one) is 1/n. <br> So the chances that the k-th try wins are given by (n-1)/n)^(k-1)*1/n .

### 10. The Dice of the Speckled Band
Holmes rolls a six-sided die six times to crack a gypsy code:
- a. What’s the chance two numbers appear thrice each (e.g., three 4s, three 6s)?
- b. What’s the chance exactly one number hits thrice, no more, no less?
Deduction: Interpret the rolls as if they spell a fatal clue—mind the overlaps.

### 10. Solution

- a. For the first we have 6/6 options. The second and the third die needs to be the same value of the first one, so 1/6 * 1/6. For choosing the fourth one, the first of the second triad, we have 5/6 options, becouse in need to be different from the first triad. The fifth and the sixth also can be 1/6 numbers. <br> We have (1/6) * (1/6) * (5/6) * (1/6) * (1/6), we also need to multiply for (6!/(3!*3!)) to consider all the different orders of rolls and to divide for 2!, becouse we are overcounting the cases where we get for example 3 as the number of the first triad and for example 4 as the number of the second one, and vice versa. <br> The final probability is given by 0.0064. 
- b. For this point we will compute the probability with the frequentist approach. We have 6 different options for the triad and (6 choose 3) different arrangement of position for the rolls to give the triad number. For choosing the remaining three number we split in two cases, one where whe have three distinct numbers and one where we have a couple and a distinct number (both from the couple and from the triad). For the first case we have 5 options for the first, 4 for the second and 3 for the third, all divided for 3! (different arrangements), for the second case we have 5 different options for the number of the couple, and (3 choose 2) ways to arrange it in the remaining three positions. For the last number we have 4 options. The total number of possibile outcomes is given by 6^6. <br> the chanche of having a number hit exaclty thrice is 0.051.

### 11. The Letters of the Red-Headed League
Holmes dispatches 20 distinct letters to 12 unique informants, each landing randomly. What’s the chance 4 get exactly 2 letters and 3 get exactly 4, the rest empty-handed?
Deduction: Trace the mail as if thwarting a league plot.

### 11. Solution

We will start computing all the way we can choose the 3 distinct groups from the 12 informants, the group of 4 with 2 letters, the group of 3 with 4 and the 5 with none. Considering each informant of the group as indistinguable becouse they belong to the same group, there are 12!/(5! * 4! * 3!) differents splits of the 12 informants in this 3 groups. We now need to artition 20 letters into groups of sizes 2, 2, 2, 2, 4, 4, 4 , and this is given by 20!/((2!)^4 * (4!)^3). We will divide by the total different possible partition of the 20 letters, given by 12^20. The final formula is: <br>

<img src="https://raw.githubusercontent.com/TondinL/KR---PE/main/reichenbach/Images/es_11.jpg" width="400"/>


### 12. The Buckets of Bohemia
m clues are hashed into N buckets by a rogue algorithm, all N^m outcomes equal. What’s the chance exactly k land in the first bucket?
Deduction: Model the scatter as if piecing together a broken photograph.

### 12. Solution




### Additional Comments:
