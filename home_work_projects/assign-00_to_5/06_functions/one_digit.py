def print_one_digit(num):
    once = num % 10
    print(f"The once digit is {once}")
    
def main():
    num = int(input("Enter number: "))
    print_one_digit(num)
    
main()