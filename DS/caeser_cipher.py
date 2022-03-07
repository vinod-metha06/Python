"""a=input()
b=int(input())

c=str(a)+str(a)
r=''
for i in range(len(a)):
    if int(a[i])%2!=0:
        r=r+str(c[(i+b)])
    if int(a[i])%2==0:
        
        r=r+str(a[i])
print(r)
"""



a1=[]
a2=[]
r=[]
#s="a"
#print(ord(s))
for i in range(65,123):
   
   if i<91:
       a1.append(chr(i))
   if i>=97:
        a2.append(chr(i))
           
           # print(chr(i))
r=a1+a1+a2+a2
s=input()
k=int(input())
res=[]
for i in range(len(s)):
    if s[i] in r:
        c=0
        for j in range(len(r)):
            if s[i]==r[j] and c==0:
                c+=1
                
                res.append(str(r[j+k]))
    if s[i] not in r:
        res.append(s[i])
            
                


t=tuple(res)
        
print("".join(t))

        
        
    


