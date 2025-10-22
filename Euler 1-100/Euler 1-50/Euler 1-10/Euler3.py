#600851475143
import math




def prime_generator(number):
    count = 3
    sqrtnumber = int(math.sqrt(number))
    prime_holder = []

    while count <= sqrtnumber:
        isprime = True
        
        for x in range(2, int(math.sqrt(count) + 1)):
            if count % x == 0: 
                isprime = False
                break
        
        if isprime:
            if number%count == 0:
                prime_holder.append(count)
        
        count += 1
        return prime_holder

prime_holder = prime_generator(600851475143)
print(max(prime_holder))