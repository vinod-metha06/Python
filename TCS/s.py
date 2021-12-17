k=[2,4]

def fac(x):
    s=0
    for i in range(1, x + 1):
       if x % i == 0:
           s=s+i
         
    return s

# Write inside the function

for i in range(len(k)):
    n=fac(k[i])
    print(n)
           

