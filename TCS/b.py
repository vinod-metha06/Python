l=int(input())
a=[]
for i in range(l):
    a.append(int(input()))
k=int(input())
b=[]
p=0
j=0
for i in range(l):
    if i !=k and i>k:
        if j!=0:
            b.append(a[k])
            
            k+=1
    elif i!=k and i<k:
        if j==0:
            b.append(a[i])
        
    elif i==k:
        j=1
        if p==0:
            b.append(a[-1])
            p+=1
         
    
print(b)
        
    
