numbers = []
for number in range(0, 200):
    if number % 3 == 0:
        numbers.append(number)
x = 0
for number in numbers:
    print(numbers[x-1])
    x -= 1
    #This whole thing was kinda unnecessary, BUT IT WORKS!!!!!
