c=0
a=[2,5,7]
for i in range(1,251):
    if i%a[0]==0:
        c+=1
    if i%a[1]==0:
        c+=1
    if i%a[2]==0:
        c+=1
print(250-c)
