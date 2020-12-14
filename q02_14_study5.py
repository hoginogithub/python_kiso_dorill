def separator(f):
    def wrapper(*args, **kwargs):
        print('-----------------------')
        print(f'{f.__name__}')
        v = f(*args, **kwargs)
        return v
    return wrapper

step03_text = 'step03_text'

@separator
def foo_step01():
    return 1

@separator
def foo_step02(a):
    x = 10
    print(locals())
    return 2

@separator
def foo_step03():
    print(step03_text)
    return 3

@separator
def foo_step04():
    step03_text = 'step04_text'
    print(step03_text)
    return 4

'''
@separator
def foo_step05():
    #step05_text = 'step05_text'
    return 5
'''
@separator
def foo_step05(a, b):
    print(f'step05 a + b = {a + b}')
    return 5

@separator
def foo_step06():
    x = 6
    def foo_step06_sub():
        print(x)
    foo_step06_sub()
    return 6

@separator
def foo_step07(f, x, y):
    print(f'f={f.__name__} x={x} y={y}')
    return f(x, y)

def foo_step07_sub(a, b):
    print(f'a + b={a + b}')
    return a + b

#@separator
def foo_step07_sub2():
    print('---- mu separator -----')
    def bar():
        print('bar in foo_step07_sub2')
        return 'bar result'
    return bar

@separator
def foo_step08(a):
    x = 1
    print('-foo_step08 called-a={} x={}'.format(a,x))
    def bar():
        print(locals())
        # print(f'a={a} x={x}')
        return 'bar result in foo_step08 a={} x={}'.format(a,x)
    return bar

@separator
def foo_step09_01(fnc):
    def bar():
        print('<bar in foo_step09_01>')
        result = fnc() + ' <-barの中でfncを実行しました'
        return result
    return bar

def foo_step09_sub1():
    return 'foo_step09_sub!'

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return 'Coor:' + str(self.__dict__)

def foo_step09_02(fnc):
    print(fnc.__name__ + ' decorated foo_step09_02')
    def fnc_checker(a, b):
        if a.x < 0 or a.x < 0:
            a = Coordinate(a.x if a.x >= 0 else 0, a.y if a.y >=0 else 0)
        if b.x < 0 or b.x < 0:
            b = Coordinate(b.x if b.x >= 0 else 0, b.y if b.y >=0 else 0)
        result = fnc(a, b)
        if result.x < 0 or result.y < 0:
            result = Coordinate(result.x if result.x >= 0 else 0, result if result.y >= 0 else 0)
        return result
    return fnc_checker

def step09_add(a, b):
    return Coordinate(a.x + b.x, a.y + b.y)

def step09_sub(a, b):
    return Coordinate(a.x - b.x, a.y - b.y)


@foo_step09_02
@separator
def step10_add(a, b):
    return Coordinate(a.x + b.x, a.y + b.y)

@foo_step09_02
@separator
def step10_sub(a, b):
    return Coordinate(a.x - b.x, a.y - b.y)

@separator
def foo_step11_01(a, b, *args):
    return f'{a} {b} {args}'

def foo_step11_02(a, b):
    return f'{a} {b}'

def foo_step11_03(a, b, c):
    return f'{a} {b} {c}'

def foo_step11_04(**kwargs):
    from operator import itemgetter
    print(type(kwargs))
    sort_args = sorted(kwargs.items(), key=itemgetter(0))
    print(sort_args)
    return (str(kwargs))

def foo_step11_05(*args, **kwargs):
    return f'args={str(args)} kwargs={str(kwargs)}'

def foo_step12_deco(fnc):
    def bar(*args, **kwargs):
        print('$$$ FOO STEP12 DECORATE $$$')
        for x in args:
            print(x)
        v = fnc(*args, **kwargs)
        return v
    return bar

@separator
@foo_step12_deco
def foo_step12(a, b):
    return step10_add(a, b)

print(foo_step01())
print(foo_step02(20))
print(foo_step03())
print(foo_step04())
print(step03_text)
#print(foo_step05())
#print(step05_text)
print(foo_step05(1, 2))
print(foo_step06())
print(foo_step07(foo_step07_sub, 33, 44))
print(foo_step07.__class__)
print(f'issubclass(foo_step07, object)={issubclass(foo_step07.__class__, object)}')
step07 = foo_step07_sub2()
print(f'step07.__name__={step07.__name__}')
print(f'exectute={step07()}')
step08_01 = foo_step08(81)
step08_02 = foo_step08(82)
#print(dir(step08_01))
#print(step08_01.__closure__)
print(step08_01())
print(step08_02())
step09_01 = foo_step09_01(foo_step09_sub1)
print(step09_01())
foo_step09_sub1 = foo_step09_01(foo_step09_sub1)
print(foo_step09_sub1())
a_coodinate = Coordinate(100, 200)
b_coodinate = Coordinate(200, 400)
print(a_coodinate)
print(b_coodinate)
print(step09_add(a_coodinate, b_coodinate))
print(step09_sub(a_coodinate, b_coodinate))
step09_add = foo_step09_02(step09_add)
step09_sub = foo_step09_02(step09_sub)
print(a_coodinate)
print(b_coodinate)
print(step09_add(a_coodinate, b_coodinate))
print(step09_sub(a_coodinate, b_coodinate))
print(step10_add(a_coodinate, b_coodinate))
print(step10_sub(b_coodinate, a_coodinate))
print(foo_step11_01('A', 'B', 'X', 'Y', 'Z'))
step11_arg = ('a', 'b', 'T')
print(foo_step11_01(*step11_arg))
step11_02 = [4, 5]
print(foo_step11_02(*step11_02))
step11_03 = {'c':33, 'a':11, 'b':22}
print(foo_step11_03(**step11_03))
print(foo_step11_04(**step11_03))
print(foo_step11_05(*step11_02, 'm', **step11_03, z='hello world'))
print(foo_step11_05(*step11_02))
print(foo_step11_05(**step11_03))
a_coodinate = Coordinate(100, 200)
b_coodinate = Coordinate(200, 400)
print(foo_step12(a_coodinate, b_coodinate))