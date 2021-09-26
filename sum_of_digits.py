def sum(n):
    s=0
    for i in range(len(n)):
        s=s+int(n[i])
        
    return s

n=input()
print(sum(n))