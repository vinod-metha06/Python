
def sp(string, prefix, pl):
   
    if len(string) == 0:
        pl.append(prefix)
    else:
        for i in range(len(string)):
            rem = string[0:i] + string[i + 1:]
            sp(rem, prefix + string[i], pl)
    return sorted(list(dict.fromkeys(pl)))
pl = []
n=input()
s=sp(n,'', pl)
print(sp(n,'', pl))
for i in range(len(s)):
    st=s[i]
    if st[0]!='0':
        print(st)
        break
        

