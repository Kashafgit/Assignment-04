AFFIRMATION = "i am capable of doing anything. I put my mind to"

def main():
    print(f"Please type the following affirmation, '{AFFIRMATION}'")
    user_feedback = input()
    while user_feedback != AFFIRMATION:
        print("That's was not the affirmation")
        print(f"Please type the following affirmation, '{AFFIRMATION}'")
        user_feedback = input()
    print("That's right!")
         
main()
    
    