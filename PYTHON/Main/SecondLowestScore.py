def second_lowest(students, scores):
    # '''
    # input:
    # students -> a list of students
    # scores -> list of the scores, with each score being that of the ith student
    
    # output:
    # student_data -> 2d list of data, with each inner list having name of student as 1st and score of 2nd as second element respectively
    # second_low_score -> the second lowest score
    # second_names -> list of students with score same as second lowest score, in the same order as in the students list
    # '''
    
    student_data, second_low_score, second_names = None, None, None
    
    # Your code starts here

    student_data=[]

    for i in range (len(students)):
        col = []
        col.append(students[i])
        col.append(float(scores[i]))
        student_data.append(col)
    
    print(student_data)
    
    m=max(scores)
    x=sorted(student_data,key=lambda i: i[1], reverse=True)
    print(x)

    second_names=[]
    for i in range(len(x)):
        if(float(x[i][1])<m):
            second_low_score=float(x[i][1])
            break

    for i in range(len(x)):
        if(float(x[i][1])==second_low_score):
            second_names.append(x[i][0])
    
    # Your code ends here
    print (student_data, second_low_score, second_names) 


a=["S ROY","B BOSE","N KAR","C DUTTA","G GHOSH"]
b=[1,3,2,1,1]
second_lowest(a, b)
