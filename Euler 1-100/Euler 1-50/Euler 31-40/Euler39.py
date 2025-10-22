import math


def pythagorean_triples(n):
    triples = set()
    for a in range(1,n):
        for b in range(a,n):
            c = math.sqrt(a**2+b**2)
            if int(c) == c and a+b+c <= 1000:
                triple = tuple(sorted((a,b,int(c))))
                triples.add(triple)
    return triples


triples = pythagorean_triples(10000)

keys = [i for i in range(1,1001)]
count_dict = dict.fromkeys(keys,0)

sum_triples = [sum(triple) for triple in triples]
print(sum_triples)
for triple_sum in sum_triples:
    count_dict[triple_sum] += 1
print(max(count_dict,key=count_dict.get))