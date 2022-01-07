# a=10
# b=20
# l=[]
# c=0

# def isp(num):
#     for n in range(2,int(num**1/2)+1):
#         if num%n==0:
#             return False
#     return True
# for i in range(a,b):
#     if isp(i):
#         l.append(i)
        
# for j in range(len(l)):
#     t=int(l[0])
    
#n=int(input())
arr=[11,6,3,10,4,12]
m=8
d={}

s=0
for i in range(len(arr)):
    c=abs(m-arr[i])
    d[c]=arr[i]
dict(sorted(d.items()))
for i in d.values() :
    print(i, end =" ")
    


    