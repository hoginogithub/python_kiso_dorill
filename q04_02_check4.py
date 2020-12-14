try:
    a = (1, 2, 3)
    b = (0, 2, 5)
    for i in range(0, len(a)):
        if a[i] == b[i]:
            print(f'i={i}')
            b[i] = a[i]
except TypeError as ex:
    print('正解')
    print(f'type={type(ex)}, {ex}')
except Exception as ex:
    print('ハズレ')
    print(f'type={type(ex)}, {ex}')
