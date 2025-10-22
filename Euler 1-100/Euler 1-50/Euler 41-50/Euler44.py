def gen_pents(limit) -> list[int]:
    pents = []
    for i in range(1,limit+1):
        pents.append(i*(3*i-1)//2)
    return pents

pent = gen_pents(3000)
d = 0

for pent1 in pent:
    for pent2 in pent:
        if pent1 + pent2 in pent and abs(pent2 - pent1) in pent and abs(pent2 - pent1) > d:
            d = abs(pent2 - pent1)
            print(d)