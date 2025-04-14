import random
def guess_num():
    print("I am thinking of a number between 0 and 99")
    num = random.randint(0, 99)
    
    while True:
        user_guess = input("Enter your guess: ")
        if user_guess == "":
            break
        guess = int(user_guess)
        if num > guess:
            print("Your guess is too low!")
        elif num < guess:
           print("Your guess is too high")
        else:
            print(f"congrtultions. The guess was, {num}")
            break
        
guess_num()