items = input("Введите числа через пробел: ").split()

numbers = []
for item in items:
    numbers.append(int(item))

indices = []
for i in range(len(numbers)):
    if numbers.count(numbers[i]) > 1:
        indices.append(i)

print(indices)