def lcalling(f):
    return lambda n: f(f'<!--{n}--!>')

def lsmall_func(v):
    return (v, v)

g = lcalling(lsmall_func)

print(g('ABC'))