def multiple_prints(message,repeat):
    for i in range(repeat):
        print(message)
        
def main():
    message = input("Enter your message: ")
    repeat = int(input("Enter the number to repeat your message: "))
    multiple_prints(message, repeat)
    
main()