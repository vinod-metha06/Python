date=["20th Oct 2052","6th Oct 2052"]


def mtonum(s):
    m={
        'jan':1,
        'feb':2,
        'mar':3,
        'apr':4,
        'may':5,
        'jun':6,
        'jul':7,
        'aug':8,
        'sep':9,
        'oct':10,
        'nov':11,
        'dec':12,
    
        
    }
    w=s.strip()[:3].lower()
    try:
       n=m[w]
       return n
    except :
        pass
    
        
res=[]
for i in range(len(date)):
    
    r1=date[i][-5:]
    r2=mtonum(date[i][-9:-5])
    if len(date[i]) < 13:
        r3=date[i][:-11]
        s=str(r1)+'-'+str(r2)+'-0'+str(r3)
    else:
        r3=date[i][:-11]
        s=str(r1)+'-'+str(r2)+'-'+str(r3)
    res.append(s)
    
print(res)
  