def isPrime(n):
    if n<= 1:
        return False;
    
    for i in range(2,n):
        if n%i==0:
            return False
    
    return True

#n=int(input())
a=list(map(int,input().split()))
p=[]
for i in range(len(a)):
    
    
    if isPrime(a[i]):
        p.append(a[i])
if len(p)==0:
    print("0")
if len(p)>0:
    print(sum(p))

        
    
    #print("Prime number")
    #else:
    #print("Non prime number")