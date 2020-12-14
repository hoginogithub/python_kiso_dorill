try:
    a = [1,2,3]
    ix = 5
    print(a[ix])
    print('go ahead')
except IndexError as iErr:
    print(f'インデックスとして与えられた{ix}が不正です')
    print(f'Type={type(iErr)}, {iErr}')
    print(type(iErr) is IndexError)