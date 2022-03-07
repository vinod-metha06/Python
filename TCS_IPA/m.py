s=input()
a=[]
for i in range(len(s)):
    if int(s[i])%2!=0:
        a.append(int(s[i]))
print(sum(a))