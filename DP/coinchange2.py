def coin(amount,coins,index,d):
    if amount ==0:
        return 1
    if amount<0 or index == len(coins):
        return 0
    
    
    key=str(amount)+"K"+ str(index)
    if key in d:
        return d.get(key)
    
    result =0
    
    for i in range(index,len(coins)-index):
        if amount>=coins[index]:
            result+=coin(amount-coins[index],coins,i,d)
    
    d[key]=result
        
    return result
a=[1,2,3]
d={}
print(coin(500,a,0,d))