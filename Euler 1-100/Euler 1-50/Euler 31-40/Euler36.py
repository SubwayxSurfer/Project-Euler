
def palindrome_gen(num) -> list[int]:
        num_str = str(num)
        if num_str[::-1] == num_str:
            return True
        return False

def binary_coversion(num):
      return bin(num)[2:]


total = 0
for i in range(1,10**6):
    pal = palindrome_gen(i)
    binary = binary_coversion(i)
    if pal and palindrome_gen(binary):
        total += i

print(total)