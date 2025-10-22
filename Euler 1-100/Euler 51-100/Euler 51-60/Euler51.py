import itertools
"""
- Get list of primes
- replace specific digits in a string
"""

def gen_primes(limit:int):
    sieve = {i:True for i in range(limit+1)}
    sieve[0] = sieve[1] = False
    for i in range(2,int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i**2,limit + 1,i):
                sieve[j] = False
    return sieve,[prime for prime in sieve if sieve[prime]]

def replace_digits(number:str,replace_pos:list[int]):
    replace_list = []
    start_pos = 1 if 0 in replace_pos else 0
    for i in range(start_pos,10):
        number_list = list(number)
        for pos in replace_pos:
            number_list[pos] = str(i)
        replace_list.append("".join(number_list))
    return replace_list
    

prime_dict,prime_list = gen_primes(10**6)

for prime in prime_list:
    prime_length = len(str(prime))
    for i in range(1,prime_length):
        perms = itertools.permutations(range(prime_length),i)
        for perm in perms:
            replaced_primes = replace_digits(str(prime),perm)
            count = 0
            for pot_prime in replaced_primes:
                if prime_dict[int(pot_prime)]:
                    count += 1
            if count == 8:
                print(replaced_primes)