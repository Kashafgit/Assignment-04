def in_range(n, low, high):
    if n >= low and n <= high:
        return True
    else:
        return False
    
def main():
    inp = int(input("Enter your number: "))
    print(in_range(inp, 56, 87))
main()