# Given an array in form of a matrix of size (n, n), rotate the matrix clockwise by 90º.

# Input Format:

# A 2d numpy array
# Output Format:

# A 2d numpy array
# Sample Input:

# [[1 2 3] 
#  [4 5 6]
#  [7 8 9]]
# Sample Output:

# [[7 4 1]
#  [8 5 2]
#  [9 6 3]]

import numpy as np
def rotate_img(mat):
    '''mat -> A 2d numpy array
       output -> A 2d numpy array is expected to be returned'''
    
    b=mat[::-1]
    print(np.transpose(b)) 
    
a=[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]

a=np.array(a)
rotate_img(a)
