

s=input()
a=['a','e','i','o','u']
d={}
v=0   
for i in range(len(s)):
    if s[i] not in a:
       
        
        if s[i] in d:
            
            d[s[i]]+=1
        else:
            
            d[s[i]]=1
    if s[i]  in a:
        v+=1
        
        
print(d.items(),"vowels="+str(v))

