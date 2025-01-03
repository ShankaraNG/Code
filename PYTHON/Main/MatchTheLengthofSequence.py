def LengthSequence(string, length):
    '''string => a string
       length => an integer representing required length of words which are be returned'''
    result= []
    # YOUR CODE GOES HERE
    x=string.split(" ")

    for i in x:
        if(len(i)==length):
            result.append(i)
    
    print(result) 

s="The world has changed and none of us can go back all we can do is our best and sometimes the best that we can do is to start over"
l=5
LengthSequence(s,l)
