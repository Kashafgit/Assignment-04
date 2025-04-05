import random
DONE_LIKED = 0.3
def done():
    return random.random() < DONE_LIKED

def chaotic_counting():
    for _ in range(1,11):
        if done():
            return
        print(_, end=" ")
        
def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first")
    chaotic_counting()
    print("I am done")
    
main()