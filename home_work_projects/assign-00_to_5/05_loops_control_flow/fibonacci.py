MAX_FIBONACCI = 10000

def main():
    fib0 = 0
    fib1 = 1
    while fib0 <= MAX_FIBONACCI:
        print(fib0)
        next_term = fib0 + fib1
        fib0 = fib1
        fib1 = next_term
        
main()
