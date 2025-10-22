import math

def get_dig(num):
    return[int(dig) for dig in str(num)]


def prime_gen(limit):
    sieve = {i:True for i in range(limit+1)}
    sieve[0] = sieve[1] = False
    for i in range(2,int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i**2,limit + 1,i):
                sieve[j] = False
    return sieve

def rotation(num):
    num = str(num)
    rotate_list:set = {num}
    rot = num
    true = True
    while true:
        rot = rot[-1] + rot[:-1]
        if rot == num:
            true = False
        else:
            rotate_list.add(rot)
            #print("Rotation: ",rot,num)
    return list(rotate_list)


count = 0
prime_dict = prime_gen(1000000)
primes = [prime for prime,value in prime_dict.items() if value]
for prime in primes:
    circ_list = rotation(prime)
    new_list = []
    for item in circ_list:
        new_list.append(int(item))
    #print("Prime: ",prime)
    if all([prime_dict[num] for num in new_list]):
        count+=1

print(count)