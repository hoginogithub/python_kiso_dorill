a = 90
b = 2
for ix in range(10):
    print(f'{ix}')
    if b != ix:
        print(f'{a} / {b - ix} = {a / (b -ix)}')

for ix in range(10):
    print(f'{ix}')
    try:
        print(f'{a} / {b - ix} = {a / (b -ix)}')
    except ZeroDivisionError:
        pass