r=int(input())
c=int(input())

M1=[]
M2=[]

for i in range(r):
    a=[]
    for x in range(c):
        a.append(int(input()))
    M1.append(a)

for i in range(r):
    b=[]
    for x in range(c):
        b.append(int(input()))
    M2.append(b)
    
R=[]
for i in range(len(M1)):
     
   
    for j in range(len(M2[0])):
 
        for k in range(len(M2)):
            R[i][j] += M1[i][k] * M2[k][j]
for r in R:
    print(r)

for i in range(r):
    for j in range(c):
        print(R[i][j], end="")
    print()


