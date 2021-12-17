#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    a=0
    b=0
    
    j=0
    f=-1
    for i in  range(len(arr)):
        
       a+= arr[i][j]
       j+=1
       b+=arr[i][f]
       f-=1
       print(a,b,f)
    return abs(a-b)
    

if __name__ == '__main__':
  
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

   
