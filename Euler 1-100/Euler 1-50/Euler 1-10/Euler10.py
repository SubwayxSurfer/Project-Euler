import math
primes_list = [2]
answer = 0

def generate_primes():
    count = 3

    while count<2000000:
        isPrime = True
        for a in range(2,int(math.sqrt(count)+1)):
            if count%a == 0:
                isPrime = False
                break
        if isPrime:
            primes_list.append(count)

        count += 1

generate_primes()
answer = sum(primes_list)
print(answer)