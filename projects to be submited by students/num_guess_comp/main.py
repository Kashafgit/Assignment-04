import random
print("Welcome to the Number Guessing Game (Computer version)")

print("I'm thinking of a number between 1 to 100, You have only 5 tries\n")

def main():
    computer_num = random.randint(1, 100)
    
    max_tries = 5
    tries = 0
    
    while tries < max_tries:
        guess = int(input(f"Attemp {tries + 1}: Take a guess: "))
        tries +=1
        if guess < computer_num:
            print("Your guess is too low")
        elif guess > computer_num:
            print("Your guess is too high")
        else:
            print(f"Congratulations! you guessed it in {tries} tries")
            break
    else:
        print(f"Sorry you've used all your tries. The computer number was {computer_num}")
        
main()