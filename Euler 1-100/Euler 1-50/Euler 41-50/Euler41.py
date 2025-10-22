import math
from itertools import permutations

def gen_primes(limit):
    sieve = {i:True for i in range(limit+1)}
    sieve[0] = sieve[1] = False
    for i in range(2,int(math.sqrt(limit)) + 1):            
        if sieve[i]:
            for j in range(i**2,limit + 1,i):
                sieve[j] = False
    return sieve

def gen_pandigital(string):
    nums = "123456789"
    string_list = [char for char in string]
    perms = list(permutations(string_list,len(string_list)))
    temp_string = ""
    perm_string = set()
    for perm in perms:
        temp_string = ""
        for char in perm:
            temp_string += char
        perm_string.add(temp_string)
    print(perm_string)
        
def is_pandigital(num:str) :
    alpha = "123456789"
    sorted_str = "".join(sorted(num))
    if sorted_str == alpha[:len(sorted_str)]:
        return True
    return False

prime_dict = gen_primes(10_000_000)
primes = [prime for prime,valid in prime_dict.items() if valid]
total = 0
for prime in primes:
    if is_pandigital(str(prime)) and prime > total:
        total = prime

print(total)


