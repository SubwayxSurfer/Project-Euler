
def reverse_number(number:int) -> int:
    return int(str(number)[::-1])

def is_palindrome(number:int) -> bool:
    if number == reverse_number(number):
        return True
    return False
    
def is_lychrel(number,iterations):
    new_number = number + reverse_number(number)
    if is_palindrome(new_number):
        return False
    elif iterations >= 50:
        return True
    else:
        iterations += 1
        return is_lychrel(new_number,iterations)
    
    
def main() -> None:
    count = 0
    for i in range(1,10_001):
        if is_lychrel(i,0):
            count += 1
    print(count)

if __name__ == '__main__':
    main()