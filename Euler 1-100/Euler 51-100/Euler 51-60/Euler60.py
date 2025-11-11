from sympy import isprime
from functools import lru_cache

@lru_cache
def check_int_concat(prime1:int,prime2:int) -> None:
    return isprime(concat(prime1,prime2)) and isprime(concat(prime2,prime1))

class Graph:
    def __init__(self) -> None:
        self.prime_combinations = [[],[],[],[]]#lists of length 1,2,3,4 respectively
    
    def add_prime(self, prime:int):
        self.apply_prime_comparison(prime)
        self.prime_combinations[0].append((prime,))
            
    def apply_prime_comparison(self, prime:int):
        for index in range(3,-1,-1):
            for prime_combination in self.prime_combinations[index]:
                combo_condition = True
                if all(check_int_concat(added_prime,prime) for added_prime in prime_combination):
                    new_set = (*prime_combination,prime)
                    if len(new_set) == 5:
                        print(f"Prime set: {new_set}, sum: {sum(new_set)}")
                    else:
                        self.prime_combinations[len(new_set)-1].append(new_set)
    
def concat(num1:int,num2:int):
    pow10 = 10 ** int(len(str(num2)))
    return num1 * pow10 + num2

def prime_generator():
    count = 0
    while True:
        count += 1
        if isprime(count):
            yield count

def main() -> None:
    """
    Problem:
    - generate a set of 5 prime numbers that when any 2 are concatenated gives a prime number
    
    Breakdown:
    1. Generate a set of 2 prime numbers that follow the concatenation rule
    Build upon this to generate a set of 3 prime numbers... repeat until 5
    
    2. Generate sets of 5 prime numbers and test each individual set to see if it works
    
    3. 
    
    Tools:
    - list of primes within acceptable range (10,000)
    - method to confirm if a number is prime efficiently
    
    """
    
    graph = Graph()
    prime_gen = prime_generator()
    
    for prime in prime_gen:
        if prime in (2,5):
            continue
        print(prime)
        graph.add_prime(prime)
        

if __name__ == '__main__':
    main()
