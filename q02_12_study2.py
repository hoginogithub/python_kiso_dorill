def gen_fnc():
    x = 1
    print('generate gen_fnc')
    def hoge():
        nonlocal x
        print(x)
        print('x count up')
        x += 1
    return hoge

# print(gen_fnc().__name__)
h = gen_fnc()

print(h.__name__)
for i in range(0, 3):
    h()