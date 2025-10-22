def expo(a,b):
    return a**b


nums = []
for a in range(2,101):
    for b in range(2,101):
        nums.append(expo(a,b))

print(len(set(nums)))