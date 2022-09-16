
def main():
    l=int(input())
    a=[]
    a=list(map(int,input().split()))[:l]
    a.sort()
    b=list(set(a))
    res=[]
    for i in range(1,l+1):
        if i not in b:
            res.append(i)
    print(*res)
        

main()