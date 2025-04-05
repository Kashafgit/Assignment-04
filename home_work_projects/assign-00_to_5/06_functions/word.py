def make_sentence(word, part_of_speach):
    if part_of_speach == 0:
        print(f"I am excited to add this {word} to my vast collection of them!")
    elif part_of_speach == 1:
        print(f"It's so nice outside today it makes me want to {word}!")
    elif part_of_speach == 2:
         print(f"Looking out my window, the sky is big and {word}!")
    else:
        print("Invalid part of speach")
        
def main():
    word = input("Please enter a noun, verb, or adjective: ")
    part_of_speach = int(input("Enter noun, verb, or adjective type 0 for noun, 1 for verb and 2 for adjective "))
    make_sentence(word, part_of_speach)
    
main()
