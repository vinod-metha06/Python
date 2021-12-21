a=[[454,55,521,14],[78,326,104,989],[23447,174,87,845],[25,81,53,11]]
#a=[[11,22,33],[44,55,66],[77,88,99]]

x=104
s=0
p=""
l=0
for i in range(len(a)):
    if x%2==0:
        for j in range(len(a[i])):
            #print(a[i][j])
            if int(a[i][j])%2 !=0:
                p=str(a[i][j])
                for k in range(len(p)):
                    l+=int(p[k])
                s+=l
    if x%2!=0:
        for j in range(len(a[i])):
            #print(a[i][j])
            if int(a[i][j])%2 ==0:
                p=str(a[i][j])
                for k in range(len(p)):
                    
                    l+=int(p[k])
                  
#return int(l)            
print(int(l))
                    
                
                
