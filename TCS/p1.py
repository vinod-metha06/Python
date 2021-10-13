n=int(input())
y=int(input())
l=[]
s=0
for i in range(n):
    l.append(int(input()))
    
for i in range(len(l)):
    s=s+min(l[i],y)
print(s)