from itertools import zip_longest

x = [1,2,3]
y = [10,20,30,40]

print('---sum---')
print(f'sum(y)={sum(y)}')

print('---zip----')
z = zip(x, y)
print(f'type z:{type(z)}')
for a, b in z:
    print(f'a={a} b={b}')

print('---zip_longest----')
print(f'type z:{type(z)}')
z = zip_longest(x, y, fillvalue=max(x))
for a, b in z:
    print(f'a={a} b={b}')

