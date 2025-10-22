def addition(num1:int,num2:int) -> int:
    return num1 + num2


def fibonnaci():
    fib_array = [1,1]
    up_limit = 10**999
    while fib_array[-1]<up_limit:
        fib_array.append(addition(fib_array[-1],fib_array[-2]))
    print(len(fib_array),len(str(fib_array[-1])))

fibonnaci()