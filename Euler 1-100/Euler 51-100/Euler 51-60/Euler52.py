
def count_digits(num:str) -> dict[str,int]:
    digit_counter = {}
    for digit in num:
       if digit in digit_counter:
           digit_counter[digit] += 1
       else:
           digit_counter[digit] = 1
    return digit_counter 

def compare_dicts(keys:list,dict1:dict,dict2:dict) -> bool:
    for key in keys:
        if dict1.get(key) != dict2.get(key):
            return False
    return True

run = True
x = 1000
while run:
    x += 1
    base_counter = count_digits(str(x))
    count = 0
    condition = True
    for mult in range(2,7):
        if condition:
            counter = count_digits(str(mult*x))
            for digit in str(x):
                condition = compare_dicts(str(x),base_counter,counter)
            
        count += 1 if condition else 0
    
    if count == 5:
        print(x)
                        
        
        
    
    