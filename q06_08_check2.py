import random
import string
import json

#key_list = ["name", "hp", "mp"]

file_name = 'q06_08_check2.json'
characters = []
with open(file_name, 'w', encoding='utf_8') as f:
    for _ in range(0, 100_000):
        #dict_character = {key: value for key, value in zip(key_list, [''.join(random.choices(string.ascii_letters, k=3)), random.randint(1,200), random.randint(1,200)])}
        dict_character = {}
        dict_character['name'] = ''.join(random.choices(string.ascii_letters, k=3))
        dict_character['hp'] = random.randint(1,200)
        dict_character['mp'] = random.randint(1,200)
        characters.append(dict_character)
    json.dump(characters, f, indent=4)
