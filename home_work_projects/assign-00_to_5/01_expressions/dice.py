
# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.
import random
roll_count = 0

def roll_dice():
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    
    global roll_count
    roll_count += 1
    print(f"Roll {roll_count} Dice1 = {die1}, Dice2 = {die2}")
    
for _ in range(3):
    roll_dice()
    
print(f"Total dice: {roll_count}")
