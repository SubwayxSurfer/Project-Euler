def factorial(number):
    total = 1
    for i in range(1,number+1):
        total *= i
    return total

fact = factorial(100)
total = 0
for number in str(fact):
    total += int(number)

print(total)