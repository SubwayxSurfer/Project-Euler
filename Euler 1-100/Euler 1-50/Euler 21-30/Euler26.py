def pattern_length(n):
    remainder = 1
    remainders = []
    while remainder not in remainders:
        remainders.append(remainder)
        remainder = (remainder * 10) % n
    return len(remainders)


longest_pattern = 0
for i in range(1,1000):
    if i % 2 != 0 and i % 5 != 0:
        
        pattern = pattern_length(i)
        if pattern > longest_pattern:
            longest_pattern = pattern
            number = i

print(longest_pattern,number)