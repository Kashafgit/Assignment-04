# import random
# NUM_ROUNDS = 5

# def main():
#     print("\n\t🎲 Welcome to the High-Low Game!\t")
#     print("\t-------------------------------\t")

#     your_score = 0

#     for i in range(NUM_ROUNDS):
#         print("Round", i + 1)
#         computer_num = random.randint(1, 100)
#         your_num = random.randint(1, 100)
#         print("Your number is", your_num)
                                        
#         choice = input("Do you think your number is higher or lower than the computer's? ")
        
#         while choice not in ["higher", "lower"]:
#             choice = input("Please enter either 'higher' or 'lower': ").lower()
        
#         higher_and_correct = choice == "higher" and your_num > computer_num
#         lower_and_correct = choice == "lower" and your_num < computer_num
        
#         if higher_and_correct or lower_and_correct:
#             print("You were right! The computer's number was", computer_num)
#             your_score += 1
#         else:
#             print("Aww, that's incorrect! The computer's number was", computer_num)

#         print("Your score is now", your_score)
#         print()
    
#     print("Thanks for playing!")
#     print("Your final score is", your_score)

#     if your_score == NUM_ROUNDS:
#         print("🎉 Wow! You played perfectly!")
#     elif your_score >= NUM_ROUNDS // 2:
#         print("👏 Good job! You played well!")
#     else:
#         print("🙃 Better luck next time!")


# if __name__ == "__main__":
#     main()


import random

CHANCE = 5

def main():
    your_score = 0
    for i in range(CHANCE):
        print("Round", i+1)
        your_num = random.randint(1,100)
        computer_num = random.randint(1,100)
        print("Your number is", your_num)
        choice = input("Do you think your number is higher or lower than the computer's?")
        while choice not in ["higher", "lower"]:
            choice = input("Please enter either higher or lower. ")
        higher_and_correct = choice == "higher" and your_num > computer_num
        lower_and_correct = choice == "lower" and your_num < computer_num
        
        if higher_and_correct or lower_and_correct:
            print("You're right. computer number was", computer_num)
            your_score +=1
        else:
            print("Incorrect")
        print("Your score is", your_score)
        print()
    
    print("Thanks for playing")
    print("Your total score is ", your_score)
    
    if your_score == CHANCE:
        print("Wow! your played very well ")
    elif your_score >= CHANCE // 2:
        print("You played very well")
    else:
        print("Better luck next time!")
        
main()