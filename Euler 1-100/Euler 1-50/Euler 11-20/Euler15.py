#n C r = n! / (r! * (n-r)!)

def factorial(number):
    product = 1
    for i in range(number):
        product *= (i+1)
    return product

n = factorial(40)
r = factorial(20)

answer = n/(r*r)
print(answer)