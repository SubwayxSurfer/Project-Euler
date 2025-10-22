def check_prime(number:int, prime_list = [])

def gen_quadratics(a:int,b:int,c:int):
    """
    a,b,c represents the coefficients for a quadratic
    """
    n = 1
    while True:
        yield a*n**2 - b*n + c
        n += 1
        
def 