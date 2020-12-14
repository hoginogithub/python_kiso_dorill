import pickle
import q06_03_char

def save_characters(characters):
    with open('q06_05.dat', 'wb') as f:
        pickler = pickle.Pickler(f)
        pickler.dump(characters)

with open('q06_03c.csv', 'r', encoding='utf_8') as f:
    lines = f.readlines()

attributes = lines[0].rstrip('\n').split(',')
characters = []
for i in range(1, len(lines)):
    character = q06_03_char.Character()
    values = lines[i].rstrip('\n').split(',')
    for j in range(0, len(attributes)):
        setattr(character, attributes[j], values[j])
    characters.append(character)

print(f'character num={len(characters)}')

save_characters(characters)