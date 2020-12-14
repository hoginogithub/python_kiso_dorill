try:
    example = [x for x in range(0, 10)]
    print(example)
    '''
    for i in range(0, len(example)):
        print(f'{example[i]} len={len(example)} i={i}')
    '''
    for comp in example:
        print(f'comp={comp}')
        if comp % 2 == 0:
            example.remove(comp)
        print(example)
    '''
    for i in range(0, len(example)):
        print(f'{example} len={len(example)} i={i}')
        if example[i] % 2 == 0:
            print(f'remove:{example[i]}')
            example.remove(example[i])
    '''
except IndexError as ex:
    print('正解')
    print(f'type={type(ex)}, {ex}')
except Exception as ex:
    print('ハズレ')
    print(f'type={type(ex)}, {ex}')
