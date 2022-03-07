s=input()
a=[]
k=-1
for i in range(len(s)):
    for j in range(len(s)):
        if j==0:
            a.append(s[i:])
        if j>0:
            a.append(s[i:k])
            k-=1
            #print(j,k)
    k=-1
l=set(a)
if "" in l:
    l.remove("")
r=list(l)
sorted_list = list(sorted(r, key = len))

print(sorted_list)

def getapal(sorted_list):
    for i in range(0,len(sorted_list)):
        t=sorted_list[i]
        if t==t[::-1]:
            print(sorted_list[i])

getapal(sorted_list)
        
    
        