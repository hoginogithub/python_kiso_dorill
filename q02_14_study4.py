def deco(fnc):
    x = 'deco'
    print(x)
    #fnc()
    def wrapper():
        print(locals())
        print(x + ' wrapper')
        print(type(fnc))
        fnc()
        return 'zzzz'
    return wrapper

def foo():
    print('!!! FOO !!!')

'''
def foo(a:int = 1):
    print('!!! FOO !!!'+f'--{a}--')
'''

print('-- phase 1 --')
g = deco(foo)
print(g.__class__)
print('-- phase 2 --')
h = g()
print('-- phase 3 --')
print(h.__class__)
print(h)

'''
foo = deco(foo)
h = g()
print(h)
'''