try:
    a = [100.0]
    print(a[-2])
except IndexError as ex:
    print('正解')
    print(f'type={type(ex)}, {ex}')
except Exception as ex:
    print('ハズレ')
    print(f'type={type(ex)}, {ex}')
