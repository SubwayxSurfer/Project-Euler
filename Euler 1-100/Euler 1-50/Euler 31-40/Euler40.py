index = [0,9,99,999,9999,99999,999999]

def gen_string() -> str:
    string = ""
    for i in range(1,100_0001):
        string += str(i)
    return string

string = gen_string()
total = 1
for i in index:
    total*=int(string[i])

print(total)