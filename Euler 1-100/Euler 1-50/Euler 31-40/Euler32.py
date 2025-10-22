import itertools

def pandigital_products():
    products = set()
    for perm in itertools.permutations('123456789'):
        for i in range(1, 8):
            for j in range(i+1, 9):
                a = int(''.join(perm[:i]))
                b = int(''.join(perm[i:j]))
                c = int(''.join(perm[j:]))
                if a * b == c:
                    products.add(c)
    return sum(products)

print(pandigital_products())