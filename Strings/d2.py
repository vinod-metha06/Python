start=int(input())
end=int(input())

p=1


for i in range(start,end+1):
    if i%2==0:
        p=p*i
print(p)
    