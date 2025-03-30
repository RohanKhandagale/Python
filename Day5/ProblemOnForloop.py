# find the highest marks using for loop and conditional
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

max_marks = 0
for marks in student_scores:
    if marks > max_marks:
        max_marks = marks

print(max_marks)


