# import hashlib

# def password_hash(password):
#     return hashlib.sha256(password.encode()).hexdigest()

# stored_logins={
#     "kashaf@gmail.com": password_hash("kashaf123"),
#     "rabia@gmail.com": password_hash("rabia123"),
#     "noor2gmail.com": password_hash("noor123")
    
# }

# def login(email, check_password, stored_logins):
#     if email not in stored_logins:
#         return False
#     hash_input = password_hash(check_password)
#     return stored_logins[email] == hash_input

# print(login("kashaf@gmail.com", "kashaf123", stored_logins))
    
import hashlib
def password_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()

stored_value = {
    "kashafakram@gmail.com": password_hash("12345"),
    "sofiaakram@gmail.com": password_hash("45678"),
    "salmanakram@gmail.com": password_hash("6789"),
}

def login(email, check_password, stored_value):
    if email not in stored_value:
        return False
    hashed_value = password_hash(check_password)
    return stored_value[email] == hashed_value

print(login("kashafakram@gmail.com", "12345", stored_value))