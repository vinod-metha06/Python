a=list(map(int,input().split()))
b=list(map(str,input().split()))
c=[]
v=0
for i in range(len(a+b)):
    if i%2==0:
        
        c.append(a[i])
        print(i)
    if i%2!=0:
        c.append(b[i])
        print(i)
print(c)
        
    
