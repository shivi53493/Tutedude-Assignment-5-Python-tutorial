students ={
    'Alice':50,
    'Bob':70,
    'John':20
}
name = input("Enter the student's name: ")
if not students.get(name) == None:
    print(f"{name}'s marks: {students[name]}")
else:
    print("Student not found")