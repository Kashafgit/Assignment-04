def num_in_fruit(fruits):
    inventry = {
        "apple": 200,
        "banana": 120,
        "mango": 230,
        "orange": 0,
        "pineapple":0
    }
    return inventry.get(fruits, 0)

def main():
    fruit = input("Enter fruit name: ").lower()
    stock = num_in_fruit(fruit)
    
    if stock > 0:
        print("This is in stock. here is how many")
        print(stock)
    else:
        print("This is not in stock")
main()