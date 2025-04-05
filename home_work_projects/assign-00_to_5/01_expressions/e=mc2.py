C = 299792458 
while True:
    try:
        user_input = input("Enter kilos of mass: (or type 'exit' to quite)")
        if user_input.lower() == "exit":
            print("Programe terminated, Goodbye!")
            break
        
        mass = float(user_input)
        energy = mass * C**2
        print("\n Formula: \ne= m*c**2")
        print(f"Mass: {mass}")
        print(f"C = {C}")
        print(f"Energy: {energy}")
    except ValueError:
        print("Invalid input. Please enter vlid numbers. ")
            
        
        