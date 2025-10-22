import time

def gen_primes(limit:int):
    sieve = {i:True for i in range(limit+1)}
    sieve[0] = sieve[1] = False
    for i in range(2,int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i**2,limit + 1,i):
                sieve[j] = False
    return [i for i in range(limit+1) if sieve[i]]

primes = gen_primes(10_000)

def prime_factors(num:int) -> list[int]:
    factors = []
    temp = num
    for prime in primes:
        if temp % prime == 0:
            factors.append(prime)
            temp //= prime
    
    return factors

def count_factors(factors:list) -> int:
    if len(set(factors)) == 4:
        return True
    return False


count = 0
for i in range(100_000,1_000_000):
    facts = prime_factors(i)
    if count_factors(facts):
        count += 1
    else:
        count = 0
    if count == 4:
        print(i-3)
        break