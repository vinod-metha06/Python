input1=input()
input2=input()
for i in range(len(input1)):
    if input1[i]==input2[0]:
        s=input1.replace(input1[i],'')
print(s)