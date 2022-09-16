class Account:
    def __init__(self,*p):
        self.num=p[0]
        self.pin=p[1]
        self.bal=p[2]
        self.wd=p[3]
        self.actp=p[4]
    
    def f(self,w,c):
        for i in self.plist:
            if i.num==c:
                if i.bal>w or i.bal==w:
                    
                    i.bal=i.bal-w
                    print(str(i.num)+" "+str(i.bal)+" "+str(w))
      
class ATM(Account):
    def __init__(self,plist):
        self.plist=plist
    
    def f2(self,cnum,pno,wd):
        k=len(self.plist)
        ct=0
        for i in self.plist:
            ct+=1
            if i.num==cnum:
                if i.pin==pno:
                    ct-=1
                    self.f(wd,cnum)
        
        if c==len(self.plist):
         print("No account Exists")
  
    def f3(self,at):
        d={}
        c=0
        for i in self.plist:
            c+=1
            if i.actp==at:
                c-=1
                d[i.num]=i.bal
        sorted(d.items())
        
        #print(dt,c,len(self.plist))
        if c!=len(self.plist):
        #print("RE",sorted(d.items()))
            for i in sorted(d.items()):
                print(i[0],i[1])
        #return sorted(d.items())
        if c==len(self.plist):
            print("No match Found")
            
    

n=int(input())
p=[]
for i in range(n):
  num=int(input("num"))
  pin=int(input("pin"))
  bal=float(input("bal"))
  wd=float(input("wd"))
  ac=input("ac")
  m=Account(num,pin,bal,wd,ac)
  p.append(m)
c=ATM(p)
nm=int(input("nm"))
pn=int(input("pn"))
w=float(input("w"))

c.f2(nm,pn,w)
a=input()
#print(a)
c.f3(a)
