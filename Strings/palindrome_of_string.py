str=input()
r=''
for i in range(1,len(str)+1):
    r=r+str[-i]
if str == r:
    print("palindrome")
elif str != r:
    print("Not pal")
    
    
    