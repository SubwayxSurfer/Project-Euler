total = 0
for i in range (1000):
    if (i%3 and i%5) == 0:
        total+=i
    elif (i%3 or i%5) == 0:
        total+=i
print(total)