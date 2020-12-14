def deco(fnc):
    print('Deco')
    return fnc

def foo():
    print('foo')

foo = deco(foo)
foo()