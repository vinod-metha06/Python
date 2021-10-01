l=int(input())
s=input()
res=""
for i in range(len(s)):
    if s[i].isdigit():
        res=res+str(int(s[i])+l)
    elif s[i].isalpha():
            
       res=res+chr(ord(s[i])+l)
print(res)