all_students = {"Abhay", "Priya", "Aman", "Neha", "Sita", "Satyam"}

football = {"Abhay", "Aman", "Sita"}

cricket = {"Abhay", "Aman", "Neha"}

both = football & cricket

only_one = football ^ cricket

none = all_students - (football | cricket)

print("Students who play both:", both)
print("Students who play only one:", only_one)
print("Students who play none:", none)
