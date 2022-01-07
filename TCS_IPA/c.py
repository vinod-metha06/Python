class CricketPlayer:
    def __init__(self,pn,pcl,page,pcf):
        self.cplayerName = pn
        self.cplayedCountry = pcl
        self.cplayerAge = page
        self.ccountryFrom = pcf

class Solution:
    def __init__(self,plist):
        self.playersList = plist

    def countPlayers(self,check_cntry):
        count = 0
        for p in self.playersList:
            if(p.ccountryFrom.lower() == check_cntry.lower()):
                count = count + 1
                
        return count
               

    def getPlayerPlayedForMaxCountry(self):
        mydict={}
        for p in self.playersList:
            mydict[p.cplayerName] = len(p.cplayedCountry)

        print(mydict)

        mx = max(mydict.values())
        names=[]

        for k in mydict:
            if(mydict[k] == mx):
                names.append(k)

        names.sort()
        print(names)

        if(len(names)>0):
            return names[0]

        else:
            return "no players found"

        

players=[]
n = int(input("enter the no. of players : "))
for i in range(n):
    pn=input("enter player name : ")
    mylist=[]
    pnc = int(input("enter count of countries that player has played against : "))
    for j in range(pnc):
        cntry = input("enter cntry name : ")
        mylist.append(cntry)
        
    mylist = set(mylist)
    page = int(input("enter age of player : "))
    pcf = input("enter home country : ")
    myobj = CricketPlayer(pn,mylist,page,pcf)
    players.append(myobj)

sol = Solution(players)
check_cntry = input("enter country name to count the players : ")
print(sol.countPlayers(check_cntry))
print(sol.getPlayerPlayedForMaxCountry())