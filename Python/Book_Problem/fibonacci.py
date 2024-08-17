def find_fib(n):
    if n <= 2:
        return 1
    fib_x, fib_next = 1, 1
    
    i = 3
    while i <= n:
        i += 1
        fib_x, fib_next = fib_next, fib_next + fib_x
        
    return fib_next

def list_fib(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]

    fib_list = [1, 1]
    fib_x, fib_next = 1, 1
    
    i = 3
    while i <= n:
        fib_x, fib_next = fib_next, fib_next + fib_x
        fib_list.append(fib_next)
        i += 1
    return fib_list

for x in range(1, 11):
    print(find_fib(x))
    
for x in range(1, 11):
    print(list_fib(x))
