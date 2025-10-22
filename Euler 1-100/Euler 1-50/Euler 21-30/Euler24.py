import itertools


def possible_permutations():
    numbers = [0,1,2,3,4,5,6,7,8,9]
    permutations_list = list(itertools.permutations(numbers,len(numbers)))
    return permutations_list

def permutation_to_numbers(array):
    true_list = []
    for number in array:
        total = 0
        for i in range(len(number)):
            total += number[i]*10**(i)
        true_list.append(total)
    true_list.sort(key = int)
    return true_list

print(permutation_to_numbers(possible_permutations())[999_999])