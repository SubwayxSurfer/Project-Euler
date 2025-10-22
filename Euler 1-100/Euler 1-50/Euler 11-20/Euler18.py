number = "759564174782183587102004824765190123750334880277730763679965042806167092414126568340807033414872334732371694295371446525439152975114701133287773177839681757917152381714914358502729486366046889536730731669874031046298272309709873933853600423"
staple = []
new_list_1 = []
new_list_2 = []
true = True

def triangle_num_gen(terms):
    list = [0]
    triangle_num = 0
    for i in range(terms):
        triangle_num+=(i+1)
        list.append(triangle_num)
    return list

def number_adder(num_1,num_2,num_3):
    total_1 = num_1+num_2
    total_2 = num_1+num_3
    if total_1 > total_2:
        return total_1
    else:
        return total_2

for a in range(0,len(number),2):
    group = int(number[a:a+2])
    staple.append(group)

start = 0
group2 = ()
true_list = []
triangle_list = triangle_num_gen(15)
for b in range(15):
    start = triangle_list[b]
    end = triangle_list[b+1]
    group2 =  staple[start:end]
    true_list.append(group2)

count = 14

for i in range(count,0,-1):
    for a in range(i):
        new_num = number_adder(true_list[i-1][a],true_list[i][a],true_list[i][a+1])
        true_list[i-1][a] = new_num


print(true_list[0])