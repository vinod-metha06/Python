a=[]
l=int(input())
for i in range(l):
    b=[]
    for j in range(l):
        b.append(int(input()))
    a.append(b)
for i in range(l):
     for j in range(l):
        print(a[i][j],end='')
     print()
#print(a)
    

