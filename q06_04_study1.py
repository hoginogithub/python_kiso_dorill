file_name = 'q06_04a.txt'

with open(file_name, 'r', encoding='utf_8') as f:
    print(f.tell())
    print(f.seek(6))
    print(f.read())
    print(f.tell())
    print(f.seek(9))
    print(f.read())
    print(f.seek(0, 2))
    print(type(f.read()))

with open(file_name, 'ab') as f:
    print(f.tell())
    print(f.seek(0))
    print(f.seek(12))
    print(f.seek(24, 1))
    print(f.seek(-12,1))
    print(f.seek(-10, 2))



