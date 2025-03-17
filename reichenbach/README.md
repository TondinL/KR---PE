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

a. 10! 10 ways to chose first, 9 second, 8 third .... 10 * 9 * 8 * ..... * 1 = 10! <br>
b. We can consider i due signori legati da vincolo come un elemento unico, quindi ragionando come sopra 9!. Bisogna però considerare il caso in cui signore A siede a destra e signore B a sinistra e viceversa, ci sono 9! arrangement nel caso 1 e 9! arrengement nel caso 2 -> 2 * 9! <br>
c. L'unico modo per rispettare il constraint dato è fare in modo che i due gruppi si siedano uno si e uno no. Ora considerando i due gruppi distinti, per oguno ci sono 5! arrangement. quindi 5! * 5! (per ogni arrangment del gruppo 1 ci sono 5! arangement del gruppo 2, per questo moltiplicazione) Bisogna considerare ora il caso in cui si inizia con un elemento del gruppo 1 o gruppo 2, quindi il tutto va moltiplicato per 2 -> 2* (5! * 5!)
d. ragionando come nel punto b, consideriamo ogni coppia come un elemento singolo -> 5!, ora bisogna calcolare tutti i modi in cui gli elementi della coppia si possono scambiare tra loro per formare un gruppo distinto: 2! per ogni, 5 casi indipendenti tra loro -> 2! * 2! * 2! * 2! * 2! = (2!)^5 -> 5! * (2!)^5 


### 2. The Cipher Arrays of Irene Adler
Irene Adler hides messages in sorted arrays of k distinct integers, each from 1 to n (e.g., 1 ≤ x[0] < x[1] < … < x[k-1] ≤ n). How many such arrays can she devise, as if concealing clues in a locked box?

### 2. Solution
coefficiente binomiale (n , k) -> come ricavarlo? come arrivare ad esso ? (aka perché)

### 3. The Paths of the Hound
A mechanical hound roams an n × m grid from (1,1) to (n,m), moving only right or down:
- a. With no bounds, how many trails can it leave?
- b. If it must first lurch right (a faulty gear), how many paths remain?
- c. If it switches direction exactly thrice (right-to-down or down-to-right), how many routes obey?
Deduction: Track its steps as if hunting it across the moors.

### 3. Solution





### Additional Comments:
