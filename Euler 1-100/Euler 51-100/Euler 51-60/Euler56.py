
def add_digit_sum(number:int) -> int:
    return sum(map(int,list(str(number))))

def main() -> None:
    largest = 0
    for a in range(1,101):
        for b in range(1,101):
            digit_sum = add_digit_sum(a**b)
            if digit_sum > largest:
                largest = digit_sum
                
    print(largest)

if __name__ == '__main__':
    main()