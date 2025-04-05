import random

NUM_SIDES = 6
def main():
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    print(f"Dice have {NUM_SIDES}, 'side each'")
    print(f"The value of die1 is {die1}")
    print(f"The value of die2 is {die2}")
    print(f"Total dice is {total}")
    
main()