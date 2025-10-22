def gen_primes(limit:int):
    sieve = {i:True for i in range(limit+1)}
    sieve[0] = sieve[1] = False
    for i in range(2,int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i**2,limit + 1,i):
                sieve[j] = False
    return [prime for prime in sieve if sieve[prime]]


def main() -> None:
    max_num = 1_000_000

    prime_list = gen_primes(max_num)
    
    required_condition = False
    
    max_top = 600#len(prime_list) - 1
    bottom_pointer, top_pointer = 0, max_top
    
    while required_condition is False:
        total = sum(prime_list[bottom_pointer:top_pointer])
        if total in prime_list:
            print(total,top_pointer-bottom_pointer)
            required_condition = True
        elif top_pointer == max_top or total > max_num:
            top_pointer -= (bottom_pointer + 1)
            bottom_pointer = 0
        else:
            top_pointer += 1
            bottom_pointer += 1
        

if __name__ == '__main__':
    main() 