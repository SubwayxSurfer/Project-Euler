def digit_gen(num):
    return [int(dig) for dig in str(num)]


numerator = 1
denominator = 1
for a in range(1,100):
    for b in range(a + 1,100):
        a_list = digit_gen(a)
        b_list = digit_gen(b)
        for ind_a,dig_a in enumerate(a_list):
            for ind_b,dig_b in enumerate(b_list):
                if dig_a == 0 or dig_b == 0:
                    pass
                elif dig_a == dig_b:
                    a_list.pop(ind_a)
                    b_list.pop(ind_b)
                    if len(a_list) == len(b_list) != 0:
                        if a_list[0] == 0 or b_list[0] == 0:
                            pass
                        elif a_list[0] / b_list[0] == a/b:
                            numerator *= a_list[0]
                            denominator *= b_list[0]
                            print(a_list[0],b_list[0])

print(numerator,denominator)
                