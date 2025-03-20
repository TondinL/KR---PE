import random

def simulate_game(rounds=100000):
    m_wins = 0
    
    for _ in range(rounds):
        S = 0  # Initialize sum
        
        # Adds random numbers until S > 100
        while S <= 100:
            x = random.randint(1, 100)
            S += x
        h_last = x  # Store last number added by Holmes
        
        # Continues until S > 200
        while S <= 200:
            y = random.randint(1, 100)
            S += y
        m_last = y  # Store last number added by Moriarty
        
       
        if m_last > h_last:
            m_wins += 1
    
    # Compute probability of Moriarty winning
    return m_wins / rounds


win_prob = simulate_game()
print(f"Estimated probability of Moriarty's victory: {win_prob:.4f}")
