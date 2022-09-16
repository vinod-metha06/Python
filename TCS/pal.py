                  #Define the find_Novowels function here
def find_Novowels(l):
  o=['a','i','e','o','u']
  res=[]
  y=True
  for i in l:
    c=0
    for j in i:
      
      if j.lower() not in o:
        c+=1
    if c==len(i):
      res.append(i)
  return res
  
