number1 = 1
number2 = 2
true = True
total = 2

while true:
    pl1 = number1+number2
    number1 = number2
    number2 = pl1
    if number2 > 4000000:
        true = False
    else: 
        if number2 % 2 == 0:
            total+=number2

print(total)