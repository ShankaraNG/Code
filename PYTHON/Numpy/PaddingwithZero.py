# Given a NumPy array of shape (n,m). Add padding of a layer of 0’s on all 4 boundaries of the matrix.

# Input Format:

# First line will be consisting of two space-separated integers representing n and m.  
# There will be n lines of input consisting of m space-separated integers representing the elements of rows of the array.
# Output Format:

# A 2d numpy array.
# Sample Input:

# 3 2  
# 1 2  
# 3 4  
# 5 6
# Sample Output:

# [[0 0 0 0]
#  [0 1 2 0]
#  [0 3 4 0]
#  [0 5 6 0]
#  [0 0 0 0]]

import numpy as np
def add_padding(mat):
    '''mat-> NumPy array
       output-> NumPy array is expected to be returned'''

    # YOUR CODE GOES HERE
    
    res = None
    vetricalzero = np.zeros((np.shape(a)[0]+2,1),dtype = "int")
    horizontalzero = np.zeros((1,np.shape(a)[1]),dtype = "int")
    new_res=np.vstack([horizontalzero,mat,horizontalzero])
    res=np.hstack([vetricalzero,new_res,vetricalzero])

    
    
    print(res) 

a=[[3, 2], 
[1, 2],
[3, 4],  
[5, 6]]
a=np.array(a)
add_padding(a)
