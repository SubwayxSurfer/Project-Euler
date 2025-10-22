count = 2
limit = 22
prime_highest = []
number = 1

for i in range(limit):
    prime_highest.append(0)

while count <= limit:
    pl = count
    for a in range(2,count+1):
        total = 0
        while pl%a == 0:
            total += 1
            pl /= a
        if total > prime_highest[a-2]:
            prime_highest[a-2] = total
        if pl == 0:
            break

    count+=1

for i in range(len(prime_highest)):    
    number *= (i+2)**(prime_highest[i])

print(prime_highest)
print(number)