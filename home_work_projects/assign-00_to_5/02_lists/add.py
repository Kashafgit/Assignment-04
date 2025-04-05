def add(numbers) -> int:
    total = 0
    for i in numbers:
        total += i
    return total
print(add([2,5,7,8,9]))