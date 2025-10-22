top_chain = 0
for i in range(1,1000000):
    number = i
    chain = 0
    while number != 1:
        if number%2 == 0:
            number /= 2
        else:
            number = (number*3) + 1
        chain+=1
    if top_chain < chain:
        top_start = i
        top_chain = chain
    
print(top_start)