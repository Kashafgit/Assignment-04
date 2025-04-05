ADULT_AGE = 18

def age_count(user_age):
    
    if user_age >= ADULT_AGE:
        return True
    else:
        return False
    
def main():
    user_input = int(input("HOw old is that person: ")) 
    print(age_count(user_input))
    
    
main()