try:
    a = [1,2,3]
    ix = 9
    s.qqqq
    print(a[ix])
except IndexError as iErr:
    print(f'インデックスとして与えられた{ix}が不正です')
    print(f'Type={type(iErr)}, {iErr}')
    print(type(iErr) is IndexError)
except NameError as iErr:
    print(f'Type={type(iErr)}, {iErr}')
except Exception as iErr:
    print(f'Type={type(iErr)}, {iErr}')
