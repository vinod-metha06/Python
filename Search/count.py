a=[1,1,1,1,2,2,3,3,3,4]

d={}
for i in range(len(a)):
    d[a[i]]=1
    


# for x, y in d.items():
#       print(x, y)

 
for i in range(len(a)):
    c=0 
    for j in range(len(a)):
       
        if a[i]/a[j]==1:
            c+=1
         
    d.update({a[i]: c})
    

# print() 
    
# for x, y in d.items():
#       print(x, y)
# h=max(d.keys(), key=(lambda k: d[k]))
# max_key = max(d, key=d.get)#get key with max value
s=0
for x, y in d.items():
    if y>1:
        s+=1
print(s)

# print(h)
# print(max_key)

    
    

    