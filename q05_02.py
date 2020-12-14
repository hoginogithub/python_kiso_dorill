import re

def sum_numbers(string):
    sold = map(int, re.findall(r'\d+', string))
    print(type(sold))
    return sum(sold)

def sum_num(string):
    sold = 0
    for s in re.finditer('\d+', string):
        sold += int(s.group())
    return sold

s1 ='1a2b3c'
print(sum_numbers(s1))
print(sum_num(s1))
print(sum_numbers('aaa'))