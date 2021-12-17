n=int(input())
i=0
c=0
val=str(n)
while i==0:
    r=int(val)-int(val[0])
    c+=1
    if r==0:
        print(r,c)
        i=1
    else:
        val =str(r)
        
    