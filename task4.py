"""
Name: Benedita Victor Sarmento
Student NO: 24802248
Date: 04/11/2024

Task 4: Monte Carlo Simulation

this code simulates the monty hall problem using a monte carlo approach, where a contestant must choose one of three doors, behind one of which is a car (the prize).

logic design:
1. initialize constants and counters for the simulation.
2. run a loop to simulate each round of the game:
   - randomly select a winning door and a contestant's choice.
   - check if the contestant's choice matches the winning door and update the win counter if true.
3. calculate the winning percentage based on the total wins.
4. display the winning percentage after all simulations are complete.

the winning percentage should be close to 33.3%, demonstrating the game's counterintuitive nature.
"""

import random

# constant
NUM_SIMULATIONS = 100000  # total number of trials to simulate

# initialize counters
wins = 0  # counter for the number of wins

# run the monte carlo simulation
for i in range(NUM_SIMULATIONS):
    # randomly select the winning door and the contestant's initial choice
    winningDoor = random.randint(1, 3)
    contestantChoice = random.randint(1, 3)
    
    # increment the win counter if the contestant's choice matches the winning door
    if contestantChoice == winningDoor:
        wins += 1

# calculate the winning percentage
winningPercentage = (wins / NUM_SIMULATIONS) * 100

# display the winning percentage
print(f"winning percentage after {NUM_SIMULATIONS} simulations: {winningPercentage:.2f}%")