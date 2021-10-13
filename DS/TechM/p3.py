input1=input()
input2=input()
r=len(input2)

c=0
for i in range(len(input1)):
    if i<=r-1:
        if input1[0]!=input2[0]:
            c=0
        elif input1[i]==input2[i]:
            c=1
if c==1:
    print("yes")
    #return "yes"
else:
    print("no")
    #return "no"
            
        