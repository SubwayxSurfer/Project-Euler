def gen_primes(limit:int):
    sieve = {i:True for i in range(limit+1)}
    sieve[0] = sieve[1] = False
    for i in range(2,int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i**2,limit + 1,i):
                sieve[j] = False
    return sieve,[prime for prime in sieve if sieve[prime]]

def prime_check(value:int):
    for i in range(2,int(value**0.5)+1):
        if value % i == 0:
            
            return False
    
    return True

def gen_quadratics(a:int,b:int,c:int):
    """
    a,b,c represents the coefficients for a quadratic
    """
    n = 1
    while True:
        yield a*n**2 + b*n + c
        n += 1

def main():
    #prime_dict,prime_list = gen_primes(100_000)
    bottom_left = gen_quadratics(4,2,1)
    top_left = gen_quadratics(4,0,1)
    top_right = gen_quadratics(4,-2,1)
    
    values = [bottom_left,top_left,top_right]
    
    count = 1
    prime_count = 0
    n = 1
    
    run = True
    while run == True:
        n += 2
        
        for value in values:
            v = value.__next__()
            #print(v)
            
            if prime_check(v):
                #print(v)
                prime_count += 1
        
        count += 4
                    
        proportion = prime_count/count
        #print(proportion)
        
        if proportion < 0.1:
            run = False
            print(n)
            print(proportion)


if __name__ == "__main__":
    main()