l=int(input())
a=[]
for i in range(l):
    a.append(int(input()))
b=[]
c=[]

for i in range(l):
      
            for j in range(2,i):
                if(a[i] % j==0):
                    c.append(a[i])
                else:
                    b.append(a[i])
b.extend(c)
print()                  
for i in range(len(b)):
    print(b[i])