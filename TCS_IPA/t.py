

s=input()
c=0
for i in range(len(s)):
    if s[i].isalnum() == False and s[i].isspace() == False :
        c+=1
        
print(c)