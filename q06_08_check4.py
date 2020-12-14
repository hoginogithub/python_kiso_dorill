import json
import q06_03_char

file_name = 'q06_08_check2.json'
with open(file_name, 'r', encoding='utf_8') as f:
    character_list = json.load(f)

characters = []
for x in character_list:
    characters.append(q06_03_char.Character(name=x.get('name'), hp=x.get('hp'), mp=x.get('mp')))

import re
import string


name_pattern = '^AA.*'
[print(x.name) for x in characters if re.search(name_pattern, x.name)]

'''
AA_list = []
for x in characters:
    m = re.search(name_pattern, x.name)
    if m is not None:
        AA_list.append(m.group())

[print(x) for x in AA_list]
'''
