students = {
    1: "Abhay",
    2: "Aman",
    3: "Rohit"
}

def search_student(roll):
    if roll in students:
        print("Student Name:", students[roll])
    else:
        print("Roll number not found")

search_student(3)
