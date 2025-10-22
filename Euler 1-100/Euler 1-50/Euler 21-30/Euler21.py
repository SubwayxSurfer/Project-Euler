def factor_sum(number:int) -> int:
    factor_total = 0
    for i in range(1,number):
        if number%i == 0:
            factor_total += i
    return factor_total

def pair_finder(number:int) -> bool:
    factor_total = factor_sum(number)
    factor_total_2 = factor_sum(factor_total)
    if number == factor_total_2:
        return True
    else:
        return False

def main():
    amicable_sum = 0
    for a in range(1,10_000):
        if pair_finder(a) and a != factor_sum(a):
            amicable_sum += a
    print(amicable_sum)

if __name__ =="__main__":
    main()