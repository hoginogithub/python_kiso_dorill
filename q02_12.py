people = [('Alice', 16), ('Bob', 19), ('Carol', 18), ('Dan', 17), ('Erin', 20)]

'''
def get_name(person):
    return person[0]

def get_age(person):
    return person[1]

def name_contains_a(name):
    return 'a' in name

def is_teenager(person):
    return 12 < get_age(person) < 20
'''

name_list = list(map(lambda p: p[0], people))
print(name_list)

name_with_a = list(filter(lambda n: 'a' in n, name_list))
print(name_with_a)

teenager = list(filter(lambda p: 12 < p[1] < 20, people))
print(teenager)

sum_of_age = sum(map(lambda p: p[1], people))
print(sum_of_age)

