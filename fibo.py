
def fib(n):
    a=0
    b=1
    if n>0:
        c=a+b
        a=b
        b=c
        print(c)
        fib(n-1)
    
n=int(input())
print(0,1)
fib(n)