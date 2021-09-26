def binary(a,s,l,key):
    mid=(s+l)//2
    while s<=l:
        if a[mid] == key:
            return 1;
        elif a[mid] > key:
            return binary(a,s,mid-1,key)
        else:
            return binary(a,mid+1,l,key)
    return -1

a=[1,2,3,4,5,6,7]
key=int(input())
s=0
l=len(a)-1
res=binary(a,s,l,key)
if res ==1:
    print("match found")
else:
    print("match not found")