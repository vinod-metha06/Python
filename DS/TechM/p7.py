input1=input()


s=list(input1)

s.reverse()
r=''.join(s)
#print(r)
t=""
for i in range(len(r)):
    if r[i]!=" ":
       t=t+r[i]
    if r[i]==" ":
       x=list(t)
       x.reverse()
       x.append(" ")
       t=""
    if i==len(r)-1:
       y=list(t)
       y.reverse()
       x.extend(y)
      
print(''.join(x))