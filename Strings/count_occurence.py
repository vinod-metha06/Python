s="aab"
key="b"
print(s.count(key))
c=0
for i in range(len(s)):
    if s[i]==key:
        c+=1
print(c)