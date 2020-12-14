class Character:
    def __init__(self, name='', hp=0, mp=0):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp

    def __str__(self):
        return f'name={self.name} hp={self.hp} mp={self.mp}'

#with open('q06_03a.csv', 'r', encoding='utf_8') as f:
with open('q06_03b.csv', 'r', encoding='utf_8') as f:
    lines = f.readlines()

attributes = lines[0].rstrip('\n').split(',')
characters = []
for i in range(1, len(lines)):
    character = Character()
    values = lines[i].rstrip('\n').split(',')
    for j in range(0, len(attributes)):
        setattr(character, attributes[j], values[j])
    characters.append(character)

for c in characters:
    print(c)