import time

def d_squares(limit:int):
    squares = []
    for i in range(1,limit+1):
        squares.append(2*i**2)
    return squares

def check_composite(num:int) -> bool:
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return True
    return False

def yield_comps(limit:int):
    for i in range(3,limit+1,2):
        if check_composite(i):
            yield i

def gen_primes(limit:int):
    sieve = {i:True for i in range(limit+1)}
    sieve[0] = sieve[1] = False
    for i in range(2,int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i**2,limit + 1,i):
                sieve[j] = False
    return [i for i in range(limit+1) if sieve[i]]

lim = 10_000

primes = gen_primes(lim)
comps = yield_comps(lim)
squares = d_squares(lim//100)
print(squares)

run = True
for comp in comps:
    run = True
    prime_list = [prime for prime in primes if prime < comp]
    square_list = [square for square in squares if square < comp]
    for prime in prime_list:
        for square in square_list:
            if prime + square == comp:
                run = False
    if run:
        print(comp)
        time.sleep(1)