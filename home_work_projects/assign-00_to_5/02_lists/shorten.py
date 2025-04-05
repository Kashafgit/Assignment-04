
# MAX_LENGTH = 3
# def shorten(lst):
#     while len(lst) > MAX_LENGTH:
#         remove_element = lst.pop()
#         print(remove_element)
        
# def main(): 
#     n = int(input("Enter the number of elements: "))
#     lst = []
#     for i in range(n):
#         element = input(f"Enter the element: {i + 1}")
#         lst.append(element)
        
#     print("Removing extra element...")
#     shorten(lst)
#     print(f"Final list: {lst}")
    
# main()
    
MAX_LENGTH = 4

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        remove_ele = lst.pop()
        print(remove_ele)
        
def main():
    n = int(input("Enter the number of elements: "))
    lst = []
    for i in range(n):
        element = input(f"Enter element {i + 1}: ")
        lst.append(element)
    print("Removing elements....")
    shorten(lst)
    print(f"Final list: {lst}")
    
main()