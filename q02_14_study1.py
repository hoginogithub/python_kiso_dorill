def deco(fnc):
    print('Deco')
    return fnc

@deco
def foo():
    print('foo')

#foo()