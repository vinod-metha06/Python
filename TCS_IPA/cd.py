s=input()
r=""
a=[]
for i in range(len(s)):
    if s[i]!=".":
        r=r+s[i]
    if s[i]==".":
        
        a.append(r)
        r=""
        
        
    
print(a)