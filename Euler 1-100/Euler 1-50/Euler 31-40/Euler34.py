def factorial(num, memo:dict = {}):
    if num in memo.keys():
        return memo[num]
    else:
        prod = 1
        if num == 0:
            return 1
        for i in range(num):
            prod*= (i+1)
        memo[num] = prod
        return prod

def digits(num):
    return [int(dig) for dig in str(num)]

total = 0
for i in range(3,factorial(9)*7):
    digit_list = digits(i)
    fact_list = [factorial(dig) for dig in digit_list]
    sum_dig = sum(fact_list)
    if sum_dig == i:
        total += i

print(total)