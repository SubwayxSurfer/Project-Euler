import math
answer = []


def prime_generator():
    count = 2
    n = 0
    
    while n<10001:
        isprime = True
        
        for x in range(2, int(math.sqrt(count))+1):
            if count % x == 0: 
                isprime = False
                break
        
        if isprime:
            answer.append(count)
            n+=1

        count += 1


prime_generator()
print(answer[-1])