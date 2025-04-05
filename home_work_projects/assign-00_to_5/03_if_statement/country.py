PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 25
MAYENGUA_AGE : int = 48

user_age = int(input("How old are you??"))

if user_age >= PETURKSBOUIPO_AGE:
    print("You can vote in Peturksbouipo ")
else:
    print("You can't vote in Peturksbouipo whre the age is 16")
    
if user_age >=STANLAU_AGE:
    print("You can vote in stanlau")
else:
    print("You can't vote in stanlau")
if user_age >= MAYENGUA_AGE:
    print("You can vote in mayengua")
else:
    print("You can't vote in mayengua")
    