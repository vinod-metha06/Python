d={}
#d[0]=1
for i in range(6):
    d[i+2]=1
print(d)
# print(d.keys())
# print(d.values())
# print(d.items())

# print(d.get(5)) #to get key using value

# print(d.update())
# print(d.popitem())

# a=1
# for i in range(6):
#     print(d[i+2])
#     if d[i+2]==a:
#         d[i+2]+=1
# print(d.items())
print(sorted(d.items()))
print(max(d.values()))
for i in sorted(d.items()):
        print(i[0],i[1])
      

a=[1,2]
b=[3,4]
z=dict(zip(a,b))
print(z.items())
