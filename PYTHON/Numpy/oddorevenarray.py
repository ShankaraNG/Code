import numpy as np 

def function(x,y):

    array=np.arange(x,y+1)
    arrayofeven=[]
    arrayofodd=[]
    for i in array:
        if(i%2==0):
            arrayofeven.append(int(i))
        else:
            arrayofodd.append(int(i))
        
    arrayofeven=np.array(arrayofeven)
    arrayofodd=np.array(arrayofodd)
    
    if(len(arrayofeven)==len(arrayofodd)):
        newarray=np.vstack([arrayofodd,arrayofeven])
    else:
        newarray=np.hstack([arrayofodd,arrayofeven])
                  
    print(newarray)  

function(11,21)
