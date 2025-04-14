def access_element(lst, index):
    if 0 <= index < len(lst):
        return lst[index]
    else:
        return "Index out of range."


def modify_element(lst, index, new_value):
    if 0 <= index < len(lst):
        lst[index] = new_value
        return lst
    else:
        return "Index out of range."

def slice_list(lst, start, end):
    if 0 <= start <= end <= len(lst):
        return lst[start:end]
    else:
        return "Invalid slice range."

my_list = [10, 20, "hello", 40, "world"]


while True:
    print("\nCurrent List:", my_list)
    action = input("Choose an action (access / modify / slice / exit): ").lower()

    if action == "access":
        idx = int(input("Enter the index to access: "))
        print("Result:", access_element(my_list, idx))

    elif action == "modify":
        idx = int(input("Enter the index to modify: "))
        new_val = input("Enter the new value: ")
        print("Updated List:", modify_element(my_list, idx, new_val))

    elif action == "slice":
        start = int(input("Enter the start index: "))
        end = int(input("Enter the end index: "))
        print("Sliced List:", slice_list(my_list, start, end))

    elif action == "exit":
        print("Goodbye!")
        break

    else:
        print("Invalid action. Please try again.")
