def average(a:float, b:float):
    sum = a+b
    return sum / 2

def main():
    avg1 = average(4,6)
    avg2 = average(7,9)
    final = average(avg1, avg2)
    print(avg1)
    print(avg2)
    print(final)
main()