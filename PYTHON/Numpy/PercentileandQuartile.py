import numpy as np
def calc(a,b,c):
    try:
    #YOUR CODE GOES HERE
        if(b=="Percentile" and len(a)!=0 and c!=0):
            res=np.percentile(a,c)
            return res
        elif(b=="Quantile" and len(a)!=0 and c!=0):
            res=np.quantile(a,c)
            return res
        else:
            raise Exception   
    except Exception as e:
        if(len(a)==0 or c==0):
            res="Null value passed"
        else:
            res="Formula Error: Wrong Formula"
        return  res

a=[1,2,3,4,5,6,7]
b="Percentile"
c=25
res=calc(a,b,c)
print(res)
