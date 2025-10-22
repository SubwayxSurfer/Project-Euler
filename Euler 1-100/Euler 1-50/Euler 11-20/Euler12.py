import math
def triangle_num_gen(terms):
    list = []
    triangle_num = 0
    for i in range(terms):
        triangle_num+=(i+1)
        list.append(triangle_num)
    return list

triangle_list = triangle_num_gen(1000000)


number = triangle_list.index(76576500)
print(number)