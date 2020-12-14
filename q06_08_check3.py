import json
import q06_03_char

file_name = 'q06_08_check2.json'
with open(file_name, 'r', encoding='utf_8') as f:
    character_list = json.load(f)

characters = []
for x in character_list:
    #characters += q06_03_char.Character(name=x.get('name'), hp=x.get('hp'), mp=x.get('mp'))
    characters.append(q06_03_char.Character(name=x.get('name'), hp=x.get('hp'), mp=x.get('mp')))

#print(sum(map(lambda x: x.hp == 1, characters)))
#print(sum(map(lambda x: x.hp == 200, characters)))
# [print(f'{i:06}:{x}') for i,x in enumerate(characters) if x.hp == 1]


'''
hp counter

hp_count_dict = {} 
for x in characters:
    hp_count_dict[x.hp] = hp_count_dict[x.hp] + 1 if x.hp in hp_count_dict else  1
    
from operator import itemgetter

hp_sorted = sorted(hp_count_dict.items(), key=itemgetter(0))
for hp, count in hp_sorted:
    print(f'hp:{hp:03d} {count}')
'''

import re
import string
'''
A-Z start count

uppercase_count_dict = {k: 0 for k in string.ascii_uppercase}

name_pattern = r'^[A-Z]'
for x in characters:
    m = re.search(name_pattern, x.name) 
    if m is not None:
        uppercase_count_dict[m.group()] += 1

for x in string.ascii_uppercase:
    print(f'{x}... = {uppercase_count_dict[x]}')

'''


name_pattern = '^AA.*'
[print(y) for y in [x.name for x in characters if re.search(name_pattern, x.name)]]

'''
AA_list = []
for x in characters:
    m = re.search(name_pattern, x.name)
    if m is not None:
        AA_list.append(m.group())

[print(x) for x in AA_list]
'''
