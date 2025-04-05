def main():
    fruits = {"apple": 22, "banana": 20, "mango":25, "cherry": 40, "strawberry": 23}
    total_price = 0
    for fruit_name in fruits:
        price = fruits[fruit_name]
        amount_bought = int(input("How many " + fruit_name + " do you want to buy? "))
        total_price += (price * amount_bought)
    print(f"Total_price {total_price}")
        
        
main()