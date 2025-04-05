import random
secret = random.randint(1,99)

print("I am thinking a guess number between 1 to 99")

guess = int(input("Enter your guess: "))
while guess != secret:
    if guess < secret:
        print("Your guess is too low!")
    else:
        print("Your guess is too high")
    print()
    guess = int(input("Enter your guess: "))
print(f"Congratulations! the number was {guess}")