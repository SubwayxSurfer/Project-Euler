n = 100
sum_of_squares = 0
square_of_sum = 0

for i in range(1,n+1):
    sum_of_squares += i**2
    square_of_sum += i

answer = square_of_sum**2 - sum_of_squares
print(answer)