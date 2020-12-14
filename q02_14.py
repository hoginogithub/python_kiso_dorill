def trace_call(f):
    def traced(*args, **kwargs):
        args_str = ', '.join(map(str, args))
        print(f'start of {f.__name__}({args_str})')
        result = f(*args, **kwargs)
        print(f'end of {f.__name__}({args_str})')
        return result
    return traced

@trace_call
def ackerman(m, n):
    if m == 0:
        print('#1#')
        return n + 1
    elif n == 0:
        print('#2#')
        return ackerman(m - 1, 1)
    else:
        print('#3#')
        return ackerman(m - 1, ackerman(m, n - 1))

print(ackerman(2, 0))