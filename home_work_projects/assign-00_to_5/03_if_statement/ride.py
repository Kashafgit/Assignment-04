
def ride():
    MINIMUM_HEIGHT = 50
    
    while True:
        user_input = input("Enter your height")
        if user_input == "":
            print("Good bye")
            break
        user_height = int(user_input)
        
        if user_height >= MINIMUM_HEIGHT:
            print("You're tall enough to ride.")
        else:
            print("You're not tall enough to ride but may be next year")
        
        
ride() 
            
