import os

file_name = 'q06_04a.txt'
with open(file_name, 'w') as f:
    pass
    #f.truncate()

with open(file_name, 'r+', encoding='utf_8') as f:
    f.write('こんにちは\n')
    lines = ['ごきげんよう\n', 'さようなら\n']
    f.writelines(lines)

with open(file_name, 'r', encoding='utf_8') as f:
    print(f.read())

with open(file_name, 'r+', encoding='utf_8') as f:
    f.write('バイバイ')

with open(file_name, 'a', encoding='utf_8') as f:
    f.write('末尾に追加しました\n')
    f.seek(0)
    try:
        print(f.read())
    except Exception as iErr:
        print(f'type={type(iErr)} {iErr}')

os.remove(file_name)

with open(file_name, 'a+', encoding='utf_8') as f:
    f.write('さらに追加しました\n')
    f.seek(0)
    print(f.read())
    
