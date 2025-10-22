def factorial(number):
    product = 1
    for i in range(number):
        product *= (i+1)
    print(product)

if __name__ == "__main__":
    factorial(99)