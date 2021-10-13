l=int(input())
a=[]
for i in range(l):
    a.append(int(input()))
s=int(input())
c=0
p=1
for i in range(l):
    for j in range(l-1):
        
        r=a[i]+a[j]
        if i!=j and r:
            if r==s:
                c+=1
            print(i,j,c)
            
            p+=1
            
print(c)