def get_int_length(number:int):
    return len(str(number))

def fraction_compare(number:float) -> tuple[int,int]:
    numer = number
    denom = 1
    while True:
        numer *= 10
        denom *= 10
        if numer % 1 == 0:
            return int(numer),denom
        

def generate_sqrt_approx():
    previous_frac = (0,1)
    for _ in range(1000):
        numer = previous_frac[1]
        denom = 2*previous_frac[1] + previous_frac[0]
        previous_frac = (numer,denom)
   
        yield numer + denom,denom

def main() -> None:
    count= 0
    for numerator,denominator in generate_sqrt_approx():
        if get_int_length(numerator) > get_int_length(denominator):
            count += 1
    print(count)
        
if __name__ == '__main__':
    main()
    