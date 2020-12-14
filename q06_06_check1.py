import pickle
import random

with open('q06_05.dat', 'rb') as f:
    picker = pickle.Unpickler(f)
    characters = picker.load()

print(f'character num={len(characters)}')

#[print(x) for x in characters]
#[print(x) for x in random.sample(characters, 5)]
#[print(f'{i+1:07d}:{characters[i]}') for i in [0,1,2]]
[print(f'{i+2:07d}:{characters[i]}') for i in range(0,3)]
[print(f'{i+2:07d}:{characters[i]}') for i in random.sample(range(0,500_000), 3)]
