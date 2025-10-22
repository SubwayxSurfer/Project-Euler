total = 11

dig_list = [0,3,3,5,4,4,3,5,5,4]
teen_list = [3,6,6,8,8,7,7,9,8,8]
ten_list = [0,0,6,6,5,5,5,7,6,6]
hundred_list = [0,13,13,15,14,14,13,15,15,14]

for i in range(1,1000):
    manipulation = str(i)
    dig = int(manipulation[-1])
    tens = int(str(int(manipulation)//10)[-1])
    hundred = int(str(int(manipulation)//100)[-1])

    if tens == 1:
        total+= hundred_list[hundred] + teen_list[dig]
    elif tens == 0 and dig == 0:
        total += hundred_list[hundred] - 3
    else:
        total+= hundred_list[hundred] + ten_list[tens] + dig_list[dig]

print(total)
    
