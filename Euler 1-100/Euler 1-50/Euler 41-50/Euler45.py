def triangle_num(limit:int):
    for i in range(1,limit+1):
        yield i*(i+1)//2

def pent_num(limit:int):
    for i in range(1,limit+1):
        yield i*(3*i-1)//2

def hex_num(limit:int):
    for i in range(1,limit+1):
        yield i*(2*i-1)

lim = 100_000

tri = triangle_num(lim)
pent = pent_num(lim)
hex = hex_num(lim)
pent_list = []
hex_list = []

for i in range(lim):
    tris = next(tri)
    pent_list.append(next(pent))
    hex_list.append(next(hex))

    if tris in pent_list and tris in hex_list:
        print(tris)

    