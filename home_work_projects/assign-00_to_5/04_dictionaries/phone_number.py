# def get_phonebook():
#     phone_book = {}
#     while True:
#         name = input("Enter a name: ")
#         if name == "":
#             break
#         number = input("Enter a number")
#         if number == "":
#             break
#         else:
#             phone_book[name] = number
#     return phone_book
    
# def print_phonebook(phonebook):
#     for name in phonebook:
#         print(name, phonebook[name])
        
# def lookup_num(phonebook):
#     while True:
#         name = input("Enter a name")
#         if name == "":
#             break
#         if name not in phonebook:
#             print(name, "not in phonebook")
#         else:
#             print(phonebook[name])

# def main():
#     phonebook = get_phonebook()
#     print_phonebook(phonebook)
#     lookup_num(phonebook)
    
# main()

def get_phonebook():
    user_phonebook = {}
    while True:
        name = input("Enter name: ")
        if name == "":
            break
        number = input("Enter a number: ")
        if number == "":
            break
        else:
            user_phonebook[name] = number
    return user_phonebook

def print_phonebook(phonebook):
    for name in phonebook:
        print(name, phonebook[name])
        
        
def lookup_phonebook(phonebook):
    while True:
        name = input("Enter name: ")
        if name == "":
            break
        if name not in phonebook:
            print(f"{name} not in phonebook")
        else:
            print(phonebook[name])        
    
def main():
    get_phone = get_phonebook()
    print_phonebook(get_phone)
    lookup_phonebook(get_phone)