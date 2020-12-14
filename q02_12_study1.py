def gen_fnc():
    x = 1
    print('generate gen_fnc')
    def hoge():
        print(x)
    return hoge

print(gen_fnc().__name__)
h = gen_fnc()
h()