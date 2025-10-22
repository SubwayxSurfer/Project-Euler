limit = 6*9**5

total = 0
for i in range(2,limit):
    digit_list = [int(digit) for digit in str(i)]
    if sum([d**5 for d in digit_list]) == i:
        total += i
        


print(total)

