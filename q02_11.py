people = [('Alice', 16), ('Bob', 19), ('Carol', 18), ('Dan', 17), ('Erin', 20)]

def get_name(person):
    return person[0]

def get_age(person):
    return person[1]

def name_contains_a(name):
    return 'a' in name

def is_teenager(person):
    return 12 < get_age(person) < 20

name_list = list(map(get_name, people))
print(name_list)

name_with_a = list(filter(name_contains_a, name_list))
print(name_with_a)

teenager = list(filter(is_teenager, people))
print(teenager)

sum_of_age = sum(map(get_age, people))
print(sum_of_age)

