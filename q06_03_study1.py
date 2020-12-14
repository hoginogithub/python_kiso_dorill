import random
import csv
import string

character_num = 500_000
character_attr = ["name", "hp", "mp"]

with open('q06_03c.csv', 'w', encoding='utf_8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(character_attr)
    for _ in range(0, character_num):
        character = [''.join(random.sample(string.ascii_letters, 3)), random.randint(1,200), random.randint(1,200)]
        writer.writerow(character)