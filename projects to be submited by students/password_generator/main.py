import random
import string

# Step 1: User se input lein
num_passwords = int(input("How many passwords do you want to generate? "))
password_length = int(input("Enter the length of each password: "))

# Step 2: Characters define karo (uppercase, lowercase, digits, punctuation)
characters = string.ascii_letters + string.digits + string.punctuation

# Step 3: Passwords generate karna
print("\nHere are your passwords:")

for i in range(num_passwords):
    password = ""  # Har new password ke liye khali string banao

    # Step 3.1: Har character ko random choose karo aur password mein add karo
    for j in range(password_length):
        random_char = random.choice(characters)
        password += random_char

    # Step 3.2: Password ko show karo
    print(f"{i+1}: {password}")
