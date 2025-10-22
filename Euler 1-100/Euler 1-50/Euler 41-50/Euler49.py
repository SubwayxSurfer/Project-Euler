import time

def gen_primes(limit:int):
    sieve = {i:True for i in range(limit+1)}
    sieve[0] = sieve[1] = False
    for i in range(2,int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i**2,limit + 1,i):
                sieve[j] = False
    return [i for i in range(limit+1) if sieve[i]]

def get_permutation(s):
    if len(s) == 1:
        yield s
    else:
        for i, c in enumerate(s):
            remaining_chars = s[:i] + s[i+1:]
            for p in get_permutation(remaining_chars):
                yield c + p

def count_items(items:list):
    counter:dict = {i:0 for i in set(items)}
    for item in items:
        counter[item]+= 1
    return counter

primes = gen_primes(10_000)
temp = []
for i in range(1000,10_000):
    temp_perms = [int(j) for j in get_permutation(str(i))]
    perms = sorted(set(temp_perms))
    prime_perms1 = [i for i in perms if i in primes]
    for perm1 in prime_perms1:
        prime_perms2 = [perm for perm in prime_perms1 if perm < perm1]
        for perm2 in prime_perms2:
            if perm2 in primes:
                perm3 = 2*perm1 - perm2
                if perm3 in primes and perm3 in prime_perms1:
                    temp.append([perm1,perm2,perm3])
                    break

ans = []
temp2 = set()
for item in temp:
    temp2.add(tuple(sorted(item)))

for i in temp2:
    run = True
    for j in i:
        if len(str(j)) < 4:
            run = False
    if run:
        ans.append("".join([str(j) for j in i]))
print(ans)
    

        
            
            
