try:
    s = set([x * x for x in range(0, 5)])
    s.discard(6)
    print('discard OK')
    s.remove(7)
    print('remove OK')
except KeyError as ex:
    print('正解')
    print(f'type={type(ex)}, {ex}')
except Exception as ex:
    print('ハズレ')
    print(f'type={type(ex)}, {ex}')
