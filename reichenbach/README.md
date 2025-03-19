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

- a.  There are 10 different options for the first seat, 9 for the second, 8 for the third, and so on until the last seat where there is only one option left. The solution is given by the permutation rule of n (n = 10) distinct objects
- b. We can consider i due signori legati da vincolo come un elemento unico, quindi ragionando come sopra 9!. Bisogna però considerare il caso in cui signore A siede a destra e signore B a sinistra e viceversa, ci sono 9! arrangement nel caso 1 e 9! arrengement nel caso 2 -> 2 * 9! <br>
- c. L'unico modo per rispettare il constraint dato è fare in modo che i due gruppi si siedano uno si e uno no. Ora considerando i due gruppi distinti, per oguno ci sono 5! arrangement. quindi 5! * 5! (per ogni arrangment del gruppo 1 ci sono 5! arangement del gruppo 2, per questo moltiplicazione) Bisogna considerare ora il caso in cui si inizia con un elemento del gruppo 1 o gruppo 2, quindi il tutto va moltiplicato per 2 -> 2* (5! * 5!)
- d. ragionando come nel punto b, consideriamo ogni coppia come un elemento singolo -> 5!, ora bisogna calcolare tutti i modi in cui gli elementi della coppia si possono scambiare tra loro per formare un gruppo distinto: 2! per ogni, 5 casi indipendenti tra loro -> 2! * 2! * 2! * 2! * 2! = (2!)^5 -> 5! * (2!)^5 


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

* *disegnino* *
- a. deve fare per forza (n-1) passi a destra e (m-1) passi verso il basso. ora bisogna solo trovare tutte le combinazioni di essi, quindi tutti i percorsi possibili. Il totale di passi da eseguire sarà (n-1) + (m-1) = n + m - 2 . Se consideriamo ogni passo come elemento distinto ci sarebbero (n + m - 2) combinazioni possibili, ma i passi verso destra e verso il basso sono indistinguibili, quindi bisogna dividere per le ripetizioni : (n + m - 2)! / (n - 1)! * (m - 1)! , che è la stessa formula che si ottiene considerando il coefficiente binomiale ( ( n + m - 2) (n - 1) ) = ( ( n + m - 2) (m - 1) )
- b. il vincolo può essere interpretato come se il cosetto partisse dalla cella (1,2) e ragionare allo stesso modo di prima con (n - 2) passi a dx e (m - 1) passi verso il basso. ....
- c.

### 4. The Poker Game at Reichenbach
Holmes faces Moriarty at a poker table, where all 5-card hands from a 52-card deck are equally likely:
- a. What’s the chance of a flush (all same suit), including straight flushes?
- b. What’s the chance of two pairs (a, a, b, b, c, distinct values)?
- c. What’s the chance of four of a kind (a, a, a, a, b, distinct)?
Deduction: Compute the odds as if spotting Moriarty’s bluff.
 
### 4. Solution

### 5. The Binary Telegram of Baskerville
A telegraph sends M 0’s and N 1’s in random order. What’s the chance the first r bits hold exactly k 1’s, as if decoding a hound’s howl?
Deduction: Reason through the static as if time is running out.

### 5. Solution

### 6. The Menagerie of Moriarty
Holmes uncovers Professor Moriarty’s scheme to display 3 bird species and 3 reptile species, selected from 8 birds and 6 reptiles, in a sinister zoo:
- a. If Moriarty chooses freely, how many exhibits can he craft?
- b. Two birds—one a hawk with a piercing cry, the other a raven with a deadly glare—cannot coexist without chaos. How many exhibits avoid this peril?
- c. A venomous parrot and a cobra, when paired, unleash a toxic fog. How many exhibits dodge this trap?
Deduction: Justify your counts as if tracing Moriarty’s twisted logic.

### 6. Solution

### 7. The Investments of Baker Street
Holmes secures £20 million to fund 4 shadowy enterprises, investing in £1 million units, each with a minimum stake: £1M, £2M, £3M, £4M.
- a. If all 4 must be funded to foil Moriarty’s network, how many strategies exist?
- b. If at least 3 must be backed (to keep the web intact), how many plans work?
Deduction: Argue your totals as if pitching to a wary Watson.

### 7. Solution

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

### 10. The Dice of the Speckled Band
Holmes rolls a six-sided die six times to crack a gypsy code:
- a. What’s the chance two numbers appear thrice each (e.g., three 4s, three 6s)?
- b. What’s the chance exactly one number hits thrice, no more, no less?
Deduction: Interpret the rolls as if they spell a fatal clue—mind the overlaps.

### 10. Solution

### 11. The Letters of the Red-Headed League
Holmes dispatches 20 distinct letters to 12 unique informants, each landing randomly. What’s the chance 4 get exactly 2 letters and 3 get exactly 4, the rest empty-handed?
Deduction: Trace the mail as if thwarting a league plot.

### 11. Solution

### 12. The Buckets of Bohemia
m clues are hashed into N buckets by a rogue algorithm, all N^m outcomes equal. What’s the chance exactly k land in the first bucket?
Deduction: Model the scatter as if piecing together a broken photograph.


### 12. Solution




### Additional Comments:
