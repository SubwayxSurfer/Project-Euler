import math

def prime_gen(limit):
    sieve = {i:True for i in range(limit+1)}
    sieve[0] = sieve[1] = False
    for i in range(2,int(math.sqrt(limit)) + 1):            
        if sieve[i]:
            for j in range(i**2,limit + 1,i):
                sieve[j] = False
    return sieve

def shorten_left(num:str):
    short_list = []
    short_num = num
    for i in range(len(num)):
        short_list.append(int(short_num))
        short_num = short_num[1:]

    return short_list

def shorten_right(num:str):
    short_list = []
    short_num = num
    for i in range(len(num)):
        short_list.append(int(short_num))
        short_num = short_num[:-1]

    return short_list

prime_dict = prime_gen(2000000)
primes = [prime for prime,valid in  prime_dict.items() if valid]

total = 0
count = 0
for prime in primes:
    short_left = shorten_left(str(prime))
    short_right = shorten_right(str(prime))
    true = True

        
    if all([prime_dict[num] for num in short_left]) and all(prime_dict[num] for num in short_right):
        total += prime
        print(short_left,short_right)
        print(prime)
        count+=1

print(total,count)