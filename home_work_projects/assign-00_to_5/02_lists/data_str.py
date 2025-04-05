def copies(my_list, data):
    my_list.append(data)
    my_list.append(data)
    my_list.append(data)

message = input("Enter your message to copy: ")
my_list = []
print(f"Before list: {my_list}")
copies(my_list, message)
print(f"After: {my_list}")