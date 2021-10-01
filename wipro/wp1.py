str=input()
res=""
for i in range(len(str)):
    if str[i].islower():
        t=str[i].upper()
        res=res+t
    elif str[i].isupper():
        t=str[i].lower()
        res=res+t
    elif str[i].isspace():
        t=" "
        res=res+t
        
print(res)

