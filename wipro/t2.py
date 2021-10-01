l=int(input())
a=[]
for i in range(l):
   a.append(int(input()))
a.sort()
if a[0]<0:
    low=a[0]
    high=a[-1]
    s=low+high
    print(s)
elif a[0]>0:
    low=a[0]
    high=a[1]
    s=low+high
    print(s)



    