l=int(input())
a=[]
for i in range(l):
   a.append(int(input()))
b=[]

for i in range(l):
    if i%2==0:
        tmp=a[i]
        tmp2=a[i+1]
        b.append(tmp2)
        b.append(tmp)
print(b)
    
    
    