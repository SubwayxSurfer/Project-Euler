def factorial(number,dict = {}):
    # if number == 1:
    #     return 1
    # if number in dict:
    #     return dict[number]
    # else:
    #     factorial_number = number*factorial(number - 1)
    #     dict[number] = factorial_number
    #     return factorial_number
    counter = number
    answer = 1
    while counter > 1:
        if counter in dict:
            return answer * dict[counter]
        else:
            answer *= counter
            counter -= 1    
    else:
        if answer == 0:
            answer = 1
        dict[number] = answer
        return answer
        
        

count = 0
for n in range(23,101):
    for r in range(n):
        answer = factorial(n)/(factorial(n-r)*factorial(r))
        if answer > 1_000_000:
            count += 1
            
print(count)
        