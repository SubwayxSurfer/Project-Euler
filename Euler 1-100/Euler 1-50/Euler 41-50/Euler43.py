def get_permutation(s):
    if len(s) == 1:
        yield s
    else:
        for i, c in enumerate(s):
            remaining_chars = s[:i] + s[i+1:]
            for p in get_permutation(remaining_chars):
                yield c + p

def mod_check(bot_lim:int,top_lim:int,divisor:int,string:str) -> bool:
    if int(string[bot_lim:top_lim])%divisor == 0:
        return True
    return False

pan_string = "0123456789"
total = 0
perms = get_permutation(pan_string)
for perm in perms:
    mods = [mod_check(1,4,2,perm),mod_check(2,5,3,perm),mod_check(3,6,5,perm),mod_check(4,7,7,perm),
    mod_check(5,8,11,perm),mod_check(6,9,13,perm),mod_check(7,10,17,perm)]
    if all(mods):
        total += int(perm)
        #print(perm)

print(total)