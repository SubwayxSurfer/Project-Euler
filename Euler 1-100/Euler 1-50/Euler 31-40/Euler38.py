
def multiples(num:int):
    num_str = str(num)
    fact = 1
    temp = num_str
    while len(temp) <= 9:
        num_str = temp
        fact += 1
        temp += str(fact*num)
    
    if len(num_str) > 9: 
        return None
    return num_str

num = ["1","2","3","4","5","6","7","8","9"]
true = True
largest_num = 0
for i in range(1,10**5):
    num_str = multiples(i)
    if num_str is not None:
        if sorted([num for num in num_str], key = int) == num :
            if int(num_str) > largest_num:
                largest_num = int(num_str)

print(largest_num)