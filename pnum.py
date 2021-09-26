def p(n):
    s=0
    while n > 0:
        r=n%10
        s=(s*10)+r
        n=n//10
    return s

n=int(input())
res=p(n)
print(res)
if res == n:
    print("P")
else:
    print("M")
