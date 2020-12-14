from operator import itemgetter

students = [
    ('Alice', 165, 49.52),
    ('Bob', 172, 63.12),
    ('Charlie', 185, 77.42),
    ('Dave', 169, 70.03),
    ('Eve', 165, 55.78),
]

shudents_sorted = sorted(students, key=itemgetter(1), reverse=True)
print(shudents_sorted)