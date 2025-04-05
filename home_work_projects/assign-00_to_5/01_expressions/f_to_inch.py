# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

while True:
    try:
        user_input = input("Enter feet: (or type exit to quite) ")
        if user_input.lower() == "exit":
            print("Program terminated. Goodbye!")
            break
        feet = float(user_input)
        inches = feet * 12
        print(f"{feet} feet is equal to {inches} inches.")
    except ValueError:
        print("Invalid input please enter a number:")