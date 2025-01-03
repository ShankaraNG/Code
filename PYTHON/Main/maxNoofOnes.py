# Given a 2D List of integers, containing only 1s and 0s, return the index of the row with the maximum number of 1s.

# Note: It is given only 1 row among all will have the maximum number of 1s

# Input Format:

# arr: List[List[int]]
# Output Format:

# int
# Input Sample:

# [[0,1,1,1], [0,0,1,1], [0,0,1,1]]
# Output Sample:

# 0
# Sample Explanation:

# Row 0 has 3 ones whereas
# rows 1 and 2 have just 2 ones.


def maxOnes(arr):
    Max=None
    gcount=0
    for i in range(len(arr)):
        count=0
        for j in range(len(arr[i])):
            if(arr[i][j]==1):
                count+=1
        
        if(gcount<count):
            Max=i
            gcount=count
    
    return(Max)
    

maxOnes([[0,1,1,1], [0,0,1,1], [0,0,1,1]])  

              
