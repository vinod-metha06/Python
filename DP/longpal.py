def bottom_up(s,n):
    mat = n*[n*[0]]
    for i in range(n-2):
        for j in range(i+1,n):
            if s[-i]==s[j]:
                mat[i][j]=2+s[i+1][j-1]
            else:
                mat[i][j]=max(mat[i+1][j],mat[i][j-1])
    return mat[0][n-1]
s="abeebac"
print(bottom_up(s,len(s)))
                

    
    
    