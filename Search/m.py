a=[1,2,3,4]
key=int(input())

x=0
for i in range(len(a)):
    if key == a[x]:
        print("Found at",i)
        break
    x=x+1
print()
if x> (len(a)-1):
    print("Not found")
