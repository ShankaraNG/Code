###important####

students = [
    {"name": "Alice", "scores": {"math": 88, "science": 90, "english": 85}, "grace_marks": 10}

]


def student_data(x):
    for student in x:
        l=student["scores"].values()
        sum=0
        for j in l:
            sum+=j
        avg=round(sum/len(student["scores"]), 2)
        print(f"{student['name']}: {avg}")

        # print(student["scores"].values())
        # total_score = sum(student["scores"].values())  # Sum the scores of each subject
        # avg_score = round(total_score / len(student["scores"]), 2)  # Calculate average
        # print(f"{student['name']}: {avg_score}")  # Print the result


a=  [  {"name": "Bob", "scores": {"math": 72, "science": 68, "english": 74}, "grace_marks": 11},
    {"name": "Charlie", "scores": {"math": 95, "science": 92, "english": 91}, "grace_marks": 9},
    {"name": "David", "scores": {"math": 60, "science": 75, "english": 70}, "grace_marks": 10},
    {"name": "Eve", "scores": {"math": 82, "science": 78, "english": 88}, "grace_marks": 11}]

# student_data(students)


def return_mean_grace(students):
    # write your code below this comment
    sum=0
    for student in students:
        sum+=student["grace_marks"]
    
    avg=round(sum/len(students),2)
    print(avg)

return_mean_grace(a)
    
