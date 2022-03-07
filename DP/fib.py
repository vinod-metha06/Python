def fib(n):
    if n == 1 or n == 2:
        return 1
    bottom_up = [None] * (n+1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up

def fib2(n):    
    if n == 1 or n == 2:
        return 1
    bottom_up = [1,1]
  
    for i in range(2, n):
        
        bottom_up_ = bottom_up[i-1] + bottom_up[i-2]
        bottom_up.append(bottom_up_)
        bottom_up_=0
    return bottom_up[n-1]


print(fib(5))