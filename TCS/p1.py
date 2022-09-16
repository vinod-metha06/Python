# n=int(input())
# y=int(input())
# l=[]
# s=0
# for i in range(n):
#     l.append(int(input()))
    
# for i in range(len(l)):
#     s=s+min(l[i],y)
# print(s)\
    
vow=['a','e','i','o','u']    
v=[]
c=[]
p=input()
for i in range(len(p)):
    if p[i] in vow:
        v.append(p[i])
    if p[i] not in vow:
        c.append(p[i])
t=len(v)
cn=0     

for i in range(len(c)):  
    if t!=0:
        a=ord(c[i]) 
        if chr(a+1) in vow:
            t=t-1
            cn=cn+1
        if chr(a-1) in vow:
            t=t-1    
            cn=cn+1
print(cn)
         

