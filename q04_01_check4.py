try:
    a = 'Something Anything'
    print(a.len)
except AttributeError as ex:
    print('正解')
    print(f'type={type(ex)}, {ex}')
except Exception as ex:
    print('ハズレ')
    print(f'type={type(ex)}, {ex}')
