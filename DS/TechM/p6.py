st=input()

a=[]
sum=0
for i in range(len(st)):
    a.append(int(input()))
for i in range(len(st)):
    if st[i]=="P":
        sum=sum+a[i]
    else:
        sum=sum-a[i]
print(abs(sum*100))
