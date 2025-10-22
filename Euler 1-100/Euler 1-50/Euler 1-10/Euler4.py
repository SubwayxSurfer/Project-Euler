palindrome = []
true = True

def rev_palindrome(number):
    reverse = 0
    pl = number
    while pl > 0:
        remainder = pl%10
        reverse = reverse*10+remainder
        pl = pl//10
    if reverse == number:
        palindrome.append(number)


for a in range(999,100,-1):
    for b in range(999,100,-1):
        pos_pal = a*b
        rev_palindrome(pos_pal)

print(max(palindrome))