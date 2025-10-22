
def quadratic(n):
    return 4*(2*n+1)**2 - 12*n


total = 1
for i in range(1,501):
    total += quadratic(i)

print(total)