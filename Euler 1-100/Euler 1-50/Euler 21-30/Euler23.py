import itertools

def factor_sum(number:int) -> int:
    factor_total = 0
    for i in range(1,number):
        if number%i == 0:
            factor_total += i
    return factor_total

def abundance_funct():
    abundance_numbers = []
    for i in range(1,28123):
        if i < factor_sum(i):
            abundance_numbers.append(i)
    return abundance_numbers


def abundance_pairs(array):
    array+= array
    abundance_pairs = itertools.combinations(array,2)
    pairs_sum = []
    for pair in abundance_pairs:
        if sum(pair) < 28123:
            pairs_sum.append(sum(pair))
    abundance_pairs = list(set(pairs_sum))
    return abundance_pairs

def non_abundance_sums():
    numbers = []
    [numbers.append(i) for i in range(1,28123)]
    abundance_sums = abundance_pairs(abundance_funct())
    for sums in abundance_sums:
        if sums in numbers:
            numbers.remove(sums)
    # for a in range(12,53):
    #     if a in numbers:
    #         print(a)
    return sum(numbers)


def main():
    print(non_abundance_sums())


if __name__ == "__main__":
    main()