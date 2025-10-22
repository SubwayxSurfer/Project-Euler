import math

def prime_checker(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def quadratic_formula(a, b, n):
    return n**2 + a*n + b


largest_count = 0
largest_num = 0
for a in range(-999,1000):
    for b in range(-1000,1001):
        is_prime = True
        count = 0
        n = 0
        while is_prime:
            mab_prime = abs(quadratic_formula(a,b,n))
            is_prime = prime_checker(mab_prime)
            n+=1
            if is_prime:
                count += 1
        
        if count>largest_count:
            largest_count = count
            largest_num = a*b

print(largest_num)
        



