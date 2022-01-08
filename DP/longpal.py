def bottom_up(s,n):
    mat = n*[n*[None]]
    for i in range(n-2):
        for j in range(i+1,n):
            if s[-i]==s[j]:
                mat[i][j]=2+s[i+1][j+1]
                

    
    
    