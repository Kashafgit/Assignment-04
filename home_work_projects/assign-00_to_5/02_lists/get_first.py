def get_first(lst):
    print(lst[0])
    
n = int(input("Enter the number of elements: "))
lst = []
for i in range(n):
    elements = input(f'Enter {i + 1} elements: ')
    lst.append(elements)
get_first(lst)