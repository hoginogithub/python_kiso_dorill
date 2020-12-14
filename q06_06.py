import pickle
# import q06_03_char

with open('q06_05.dat', 'rb') as f:
    picker = pickle.Unpickler(f)
    characters = picker.load()

print(f'character num={len(characters)}')

#[print(x) for x in characters]