x=int(input())
z=str(x)
l=len(z)
sum=0
for i in range(l):
    sum+=int(z[i])**l
if sum==x:
 print("Armstrong")
else:
    print("Not Armstrong")