def get_first(lst):
    print(lst[-1])
    
n = int(input("Enter the number of the elements"))
lst = []
for i in range(n):
    elements = input(f"Enter elements: {i + 1}: ")
    lst.append(elements)
    
get_first(lst)
    