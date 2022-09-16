n=int(input())
a=[]
for i in range(n):
    t=list(map(int,input().split()))
    a.append(t)
d={}
for i in range(0,n):
    y=[]
    s=0
    s=a[i][0]
    r=len(set(a[i]))
    d[i+1]=s+r
    print(s+r)
    print(a[i])
print(d)
print(max(d))
p=[]
for i in d.values():
    p.append(i)
ti=len(set(p))

if n==ti:
    print("Tie")
if max(d)==1:
    print("Radha")
if max(d) !=1:
    print(max(d))