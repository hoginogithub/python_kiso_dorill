import re

def check_balance(string):
    #f_pattern = r'(-?(?: [0-9]+ \. [0-9]+ | [0-9]+))円 '
    f_pattern = r'(-?(?: \d+ \. \d+ | \d+))円 '
    float_regex = re.compile(f_pattern, re.VERBOSE)
    #print(re.findall(float_regex, string))
    balance = [float(s) for s in float_regex.findall(string)]
    return round(sum(balance), 2)

s1 = 'これは3円、あれは-１０.５円 それは7.256円'
#s1 = 'これは3円、あれは10.5円'
print(check_balance(s1))