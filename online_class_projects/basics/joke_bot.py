SORRY = "sorry, i only tells joke."
PROMPT = "What do you want? "
JOKE = "Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs"

def main():
    user_input = input(PROMPT).strip().lower()
    if "joke" in user_input:
        print(JOKE) 
    else:
        print(SORRY) 
        
    
    
main()