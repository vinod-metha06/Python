x=int(input())
y=int(input())
a=[]
c=x

for i in range(x,y+1):
        sum=0
        c=i
        z=str(c)
        l=len(z)
        for j in range(l):
            sum+=int(z[j])**l
        
        if sum==c:
            a.append(sum)
        c+=1
        sum=0
        
print(a)
