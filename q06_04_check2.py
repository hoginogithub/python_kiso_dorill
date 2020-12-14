data_file = 'q06_04b.dat' 
with open(data_file, 'wb') as f:
    # print(type(range(0,2)))
    # print(range(0,2))
    barr = bytes(range(0,2))
    f.write(barr)
    f.write(bytes.fromhex('ff'))
    # f.read() NG

with open(data_file, 'rb') as f:
    print(f.read(1))
    f.seek(1, 1)
    print(f.read())
    # f.write(bytes.fromhex('EE')) NG

with open(data_file, 'rb+') as f:
    f.write(bytes.fromhex('EE'))
    f.seek(0)
    print(f.read())

