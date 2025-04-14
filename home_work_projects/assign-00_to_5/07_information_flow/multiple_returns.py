def get_users_data():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    
    return first_name, last_name,email

def main():
    data = get_users_data()
    print(f"Recived the following data, {data}")
    
main()