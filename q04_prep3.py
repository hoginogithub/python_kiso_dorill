def divide(a, b):
    if b == 0:
        raise ZeroDivisionError(f'0での除算はできません')
    return a / b

try:
    print(divide(10, 3))
    print(divide(10, 0))
except ZeroDivisionError as zErr:
    print(f'type={type(zErr)}, {zErr}')