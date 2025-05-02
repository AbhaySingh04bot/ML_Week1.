marks = [
    [85, 90, 80],   # Student 1
    [78, 88, 92],   # Student 2
    [90, 76, 84]    # Student 3
]

for i in range(3):
    total = sum(marks[i])
    average = total / 3
    print("Student", i + 1, "- Total Marks:", total, "Average Marks:", round(average, 2))

