students = {
    "Ethan": 85,
    "George": 68,
    "John": 99,
    "Michael": 72,
    "Bob": 83
}
sum = 0
for i in students.values():
    sum = sum+i
avg = sum / len(students)
print("Class average:", avg)

highest = max(students.values())
lowest = min(students.values())
print(f"Student with the highest is {students[highest]}")
print(f"Student with the lowest is {students[highest]}")

search = 