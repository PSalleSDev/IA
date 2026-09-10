import pandas as pd
from enum import Enum
import matplotlib.pyplot as plt

class Course(Enum):
    GEC = "GEC"
    GES = "GES"

class Student:
    def __init__(self, name: str, age: int, grade: int, course: Course, semester: int):
        self.name: str = name
        self.age: int = age
        self.grade: int = grade
        self.course: Course = course
        self.semester: int = semester

students: list[Student] = [
    Student("Pedro", 20, 7, Course.GEC, 5),
    Student("Gustavo", 21, 3, Course.GES, 2),
    Student("Davi", 18, 10, Course.GEC, 5),
    Student("João", 22, 5, Course.GES, 1),
    Student("Gabriel", 24, 0, Course.GEC, 10)
]

df: pd.DataFrame = pd.DataFrame([student.__dict__ for student in students])

#plt bar
#plt.bar(df["name"].array, df["semester"].array)

# plt histogram
# plt.hist(df["semester"].array)
# plt.xlabel("Semesters")
# plt.ylabel("Studants")
# plt.title("Semesters per Studants")

#plt scatter
plt.scatter(df["name"].array, df["semester"].array)
plt.xlabel("Semesters")
plt.ylabel("Studants")
plt.title("Semesters per Studants")

plt.show()