input1=input()
a=0
b=0
for i in range(len(input1)):
    if input1[i]=="{":
        a+=1
    elif input1[i]=="}":
        b+=1
if a==b:
    print("correct")
    #return "correct"
else:
     print("error")
     #return "error"
    