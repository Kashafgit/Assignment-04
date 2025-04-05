def count_event(lst):
    count = 0
    for i in lst:
        if i % 2 == 0:
            count +=1
    print(count)
def get_count_even():
    lst = []
    user_input = input("Enter list of number or press enter to close")
    while user_input != "":
        lst.append(int(user_input))
        user_input = input("Enter a number")
            
def main():
    user = get_count_even()
    count_event(user)
    
main()