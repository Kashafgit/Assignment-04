

import random
def user_guess():
    print("Think of a number between 1, 100 and i will try to guess it")
    low = 1
    high = 100
    feedback = ""
    while feedback != "c":
        guess = random.randint(low,high)
        print(f"My guess is {guess}")
        feedback = input("Is it too high (h), too low (l), or correct(c) ?").lower()
        if feedback == "h":
            high = guess -1
        elif feedback == "l":
            low = guess + 1
        elif feedback != 'c':
            print("Please enter only h, l, c")
    print(f"Yay i guessed your number {guess}")
user_guess()
            