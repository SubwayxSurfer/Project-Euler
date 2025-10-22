import math

for a in range(100,1000):
    for b in range(100,1000):
        global answer
        c = math.sqrt(a**2+b**2)
        if c != round(c):
            pass
        else:
            if a+b+c == 1000:
                print(a,b,c)
                answer = int(a*b*c)
print(answer)
