people = [('Alice', 16), ('Bob', 19), ('Carol', 18), ('Dan', 17), ('Erin', 20)]

def get_name(person):
    return person[0]

def get_age(person):
    return person[1]

def name_contains_a(name):
    return 'a' in name

def is_teenager(person):
    return 12 < get_age(person) < 20

name_list = []
for person in people:
    name_list += [get_name(person)]
print(name_list)

name_with_a = []
for name in name_list:
    if name_contains_a(name):
        name_with_a += [name]
print(name_with_a)

teenager = []
for person in people:
    if is_teenager(person):
        teenager += [person]
print(teenager)

sum_of_age = 0
for person in people:
    sum_of_age += get_age(person)
print(sum_of_age)

