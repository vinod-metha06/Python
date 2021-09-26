str=input()
r=''
for i in range(1,len(str)+1):
    r=r+str[-i]
if str == r:
    print("p")
elif str != r:
    print("N")
    
    