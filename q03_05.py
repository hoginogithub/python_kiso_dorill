def format_float(number):
    if type(number) is not float:
        raise TypeError('引数がfloatではありません')
    number = str(number)
    integer_part, float_part = number.split('.')
    return ",".join([integer_part, float_part[0:3]])

print(format_float(3.123456))
print(format_float(5.2))
print(format_float(1))
