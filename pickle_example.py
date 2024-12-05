import pickle


class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades


alice = Student("Alice", 20, [1, 4, 2, 1])

student_grades = {"Alice": [1, 4, 2, 1], "Bob": [2, 2, 3, 5], "Charlie": [1, 1, 1, 1]}


file_path = "student_grades.pkl"

with open(file_path, "wb") as file:
    pickle.dump(student_grades, file)
    pickle.dump(alice, file)


with open(file_path, "rb") as file:
    loaded_grades = pickle.load(file)
    loaded_alice = pickle.load(file)

# print(loaded_grades)
# print(loaded_alice.__dict__)

student_grades.update({"Dean": [2, 2, 2, 2]})
print(student_grades)
