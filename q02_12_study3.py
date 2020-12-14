def gen_fnc():
    x = 1
    print('generate gen_fnc')
    def foo():
        nonlocal x
        print(x)
        print('foo count up +1')
        x += 1
    def bar():
        nonlocal x
        print(x)
        print('bar count up +2')
        x += 2
    return foo, bar


# print(gen_fnc().__name__)
f1, f2 = gen_fnc()

print(f1.__name__)
print(f2.__name__)
for i in range(0, 3):
    f1()
    f2()