try:
    s = {'shirt': 7, 'pants': 2, 'socks': 8}
    print(sum(s))
except TypeError as ex:
    print('正解')
    print(f'type={type(ex)}, {ex}')
except Exception as ex:
    print('ハズレ')
    print(f'type={type(ex)}, {ex}')
