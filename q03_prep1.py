x = [str(x) for x in range(1,6)]
print(x)

code_name = ['abc', 'def', 'xyz']
# x = ['{0}:{1}'.format(i, v) for i, v in enumerate(code_name)]
x = [f'No.{i} Name={v}' for i, v in enumerate(code_name)]
print(x)