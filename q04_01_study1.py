def lcalling(f):
    return lambda n: f(f'<!--{n}--!>')

@lcalling
def lsmall_func(v):
    return (v, v)

print(lsmall_func('ABC'))