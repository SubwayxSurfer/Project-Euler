import csv


directory = "Euler 1-50\Euler 41-50\Euler42.csv"
letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
word_dict = {letters[i]:(i+1) for i in range(len(letters))}

def word_sum(word):
    total = 0
    for letter in word:
        total+=word_dict[letter]
    return total

def triangular_num(limit):
    return [(i*(i+1))/2 for i in range(1,limit+1)]

with open(directory,"r") as file:
    reader = csv.reader(file,delimiter = ",")
    for row in reader:
        words = row

count = 0
triangle_list = triangular_num(100)
for word in words:
    word_total = word_sum(word)
    if word_total in triangle_list:
        count += 1

print(count)
