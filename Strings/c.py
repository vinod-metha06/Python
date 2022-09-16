n=int(input())
for i in range(1,11):
    s=""
    for j in range(1,n+1):
       
        p=i*j
        if i==10:
            s=s+"   "+str(j)+"*"+str(i)+"="+str(p)
            s=s
        else:
            s=s+"    "+str(j)+"*"+str(i)+"="+str(p)
            s=s
    print(s)
        
    
    