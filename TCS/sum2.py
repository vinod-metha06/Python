a=int(input())
b=int(input())

res=0
for i in range(a,b+1):
    d=str(i)
    r=0
    l=0
    for j in range(len(str(i))):
        k=len(str(i))
        r=r+int(str(i[l]))
        l+=1
        print(r)
    res=(int(d[0])+int(d[1]))+res
#print(res)

