import json
import q06_03_char
import argparse
import re

parser = argparse.ArgumentParser(
    description='q06_08_check2.json '
    'analyzer')

parser.add_argument('-hp', type=int, help='hp matching')
parser.add_argument('-mp', type=int, help='mp matching')
parser.add_argument('-hp_counter', action='store_true', help='hp counter list')
parser.add_argument('-re', type=str, help='regular expressions')

args = parser.parse_args()

file_name = 'q06_08_check2.json'
with open(file_name, 'r', encoding='utf_8') as f:
    character_list = json.load(f)

characters = []
for i, x in enumerate(character_list, 1):
    characters.append(q06_03_char.Character(name=x.get('name'), hp=x.get('hp'), mp=x.get('mp')))
print(f'number of charcter = {i}')

if args.hp:
    [print(f'{i:06}:{x}') for i,x in enumerate(characters, 1) if x.hp == args.hp]


if args.mp:
    [print(f'{i:06}:{x}') for i,x in enumerate(characters, 1) if x.mp == args.mp]

if args.hp_counter:
    hp_count_dict = {} 
    for x in characters:
        hp_count_dict[x.hp] = hp_count_dict[x.hp] + 1 if x.hp in hp_count_dict else  1
    
    from operator import itemgetter

    hp_sorted = sorted(hp_count_dict.items(), key=itemgetter(0))
    for hp, count in hp_sorted:
        print(f'hp:{hp:03d} {count}')

if args.re is not None:
    name_pattern = r'{}'.format(args.re)
    name_match_list = [print(x) for x in characters if re.search(name_pattern, x.name)]

    print(f'{args.re} in name count={len(name_match_list)}')
