s1=input()
s2=input()
if len(s1)==len(s2):
    a=[]
    b=[]
    for i in range(len(s1)):
        a.append(s1[i])
    for i in range(len(s2)):
        b.append(s2[i])
    a.sort()
    b.sort()
    x=''.join(a)
    y=''.join(b)
    print(x==y,"Anagram")
else:
    print("Not Anagram")
    
    
    # Codition for anagram
    # String1 and String2 both must contains same character of same numbers