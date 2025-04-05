def check_temp():
    check = float(input("Enter tempreture in fehrenheit: "))
    c = (check - 32) * 5.0/9.0
    return print(f"Converted value: {round(c,2)}°C")
check_temp()