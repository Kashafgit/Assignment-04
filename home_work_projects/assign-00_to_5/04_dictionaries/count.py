def get_user_input():
    user_lists = []
    while True:
        user_input = input("Enter a number: ")
        if user_input == "":
            break
        num = int(user_input)
        user_lists.append(num)
    return user_lists
    
def user_dict(user_list):
    num_dict = {}
    for num in user_list:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    return num_dict

def print_count(user_count):
    for num, count in user_count.items():
        print(f"{num} appears {count} times")
        
def main():
    user_input = get_user_input()
    num_dic = user_dict(user_input)
    print_count(num_dic)
    
main()
