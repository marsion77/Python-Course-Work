
from f1 import Student

s1 = Student("Alice", 20, 92)
s2 = Student("Bob", 19, 68)
s3 = Student("Charlie", 21, 45)

students = [s1, s2, s3]

for s in students:
    print(f"{s.name}: Marks = {s.marks}, Grade = {s.grade()}")
