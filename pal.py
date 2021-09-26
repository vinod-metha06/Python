def p(s,l):
    r=0
    #i=0
    for i in range(int(l/2)):
        if s[i] == s[l-1]:
            r=1
    return r
s=input()
l =len(s)
if p(s,l)==1:
    print("Pal")
else:
    print("M")