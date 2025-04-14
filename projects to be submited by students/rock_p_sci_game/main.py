import random 
choice = ["rock", "paper", "scissor"]
def computer_choice():
    return random.choice(choice)

def user_choice():
    user_choice = input("Enter your choice: rock, paper or scissor: ").lower()
    while user_choice not in choice:
        print("Invalid input. Please choose rock paper or scissor only")
        continue
    return user_choice


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie"
    elif (user_choice == "rock" and computer_choice == "scissor") or \
        (user_choice == "scissor" and computer_choice == "paper") or \
        (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose"
        
        
def play_game():
    print("Welcome to the rock paper scissor game\n")
    while True:
        
     userChoice = user_choice()
     computerChoice = computer_choice()
    
     print(f"Computer choose: {computerChoice}")
     result = determine_winner(userChoice, computerChoice)
     print(result)
     
     playagain = input("Do you want to play again? (yes / no)?").lower()
     if playagain != "yes":
        break
    print("Thanks for playing")
    
play_game()
           
    
    