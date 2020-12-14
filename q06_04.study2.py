def bytes_to_int(x:bytes) -> int:
    return int.from_bytes(x, byteorder='big')

def int_to_bytes(x:int, bytes_size=1) -> bytes:
    return x.to_bytes(bytes_size, byteorder="big")

def bytes_or_operation(x:bytes, y:bytes) -> bytes:
    return int_to_bytes(bytes_to_int(x) | bytes_to_int(y), len(x))

def bytes_and_operation(x:bytes, y:bytes) -> bytes:
    return int_to_bytes(bytes_to_int(x) & bytes_to_int(y), len(x))

def bytes_xor_operation(x:bytes, y:bytes) -> bytes:
    return int_to_bytes(bytes_to_int(x) ^ bytes_to_int(y), len(x))

def bytes_to_hex(x:bytes) -> str:
    return memoryview(x).hex()

a = bytes.fromhex('00')

if a:
    print(f'{a} is True')
else:
    print(f'{a} is False')

b = b'\x10'
print(f'{bytes_to_int(b):08b}')
print(f'{a} | {b} = {bytes_or_operation(a, b)}')
print(f'{a} & {b} = {bytes_and_operation(a, b)}')
print(f'{a} ^ {b} = {bytes_xor_operation(a, b)}')

print(f'{a} + {b} = {a + b}')
c = b * 3
print(f'{b} * 3 = {c}')

d = bytes(range(0,3))
print(f'{d}')

print(f'{c} | {d} = {bytes_or_operation(c, d)}')

import random

list_size = 5
e_list = [int_to_bytes(random.randint(0, 255)) for _ in range(0, list_size)]
#print(e_list)
e = b''.join(e_list)
#print(f'len(e)={len(e)}')
e_str = bin(bytes_to_int(e)).lstrip('0b').zfill(list_size * 8)
#print(f'type={type(e)} e={e}')
f = b''.join([int_to_bytes(random.randint(0, 255)) for _ in range(0, list_size)])
#print(f'len(f)={len(f)}')
f_str = bin(bytes_to_int(f)).lstrip('0b').zfill(list_size * 8)
g_str = bin(bytes_to_int(bytes_and_operation(e, f))).lstrip('0b').zfill(list_size * 8)
#print(f'{bytes_to_hex(e)} & {bytes_to_hex(f)} = {bytes_to_hex(bytes_and_operation(e, f))}')

print(f'{e_str} len={len(e_str)}')
print(f'{f_str} len={len(f_str)}')
print(f'{g_str} len={len(g_str)}')

import string
h = bytes.fromhex(''.join(random.choice(string.hexdigits) for _ in range(0, (list_size * 2))))
print(h)

import struct
#k = struct.pack('B',random.randint(0,255))
k = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
print(k)
l = struct.pack('BBB',k[0], k[1], k[2])
print(l)
# m = ','.join([hex(x) for x in struct.unpack('BBB', l)])
m = ''.join(['{:02x}'.format(x) for x in struct.unpack('BBB', l)])
#print(f'{l[0]:x}{l[1]:x}{l[2]:x}{l[3]:x}{l[4]:x}')
print(m)

