def fib2(n):  
    if n==0:
        return 0  
     
    if n == 1 or n == 2:
        return 1
    
    a = [1,1]
  
    for i in range(2, n):
        
        bottom_up_ = a[i-1] + a[i-2]
        a.append(bottom_up_)
        bottom_up_=0
        
    return a

n=int(input("Input:"))
print(fib2(n))