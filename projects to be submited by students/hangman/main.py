
import random

words = ["apple", "banana", "orange"]
word = random.choice(words)
guessed_word = []
chances = 6

while chances > 0:
    displayed_word = ""
    for letter in word:
        if letter in guessed_word:
            displayed_word += letter
        else:
            displayed_word += " _ "
    print("word", displayed_word)
    
    if displayed_word == word:
        print("Congratulations you won")
        break
    
    guess = input("Enter a guess: ").lower()
    
    if guess in guessed_word:
        print("You already guess this word")
        continue
    guessed_word.append(guess)
    if guess not in word:
        chances -= 1
        print(f"Wrong guessed you have {chances} chances left")  
        
    if chances == 0:
        print("Game over") 