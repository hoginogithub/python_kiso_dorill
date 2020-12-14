from operator import attrgetter

class Student:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def __str__(self):
        return self.name + ' ' + str(self.height) + ' ' + str(self.weight)

students = [
    Student('Alice', 165, 49.52),
    Student('Bob', 172, 63.12),
    Student('Charlie', 185, 77.42),
    Student('Dave', 169, 70.03),
    Student('Eve', 165, 55.78),
]

students.sort(key=attrgetter('weight'), reverse=False)
shudents_sorted = sorted(students, key=attrgetter('height'), reverse=True)
for s in shudents_sorted:
    print(s)
