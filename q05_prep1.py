import re

st = 'ad45tg78es273ta11'
p = re.compile('d[4-9]')
m = p.search(st)
print(m)
m = re.search('[0-9]+', st)
print(m)

print(re.findall('[0-9]{2,2}', st))

for s in re.finditer('[0-9]{2,2}', st):
    print(s.span(), s.group())

print(re.sub('\d+', '#', st))
print(re.split('\d+', st))

m = re.search('[a-zA-Z]+([0-9]+)[a-zA-Z]+([0-9]+)[a-zA-Z]+([0-9]+)', st)
print(m.group())
for i in range(0, 4):
    print(m.group(i))

print(re.search('\d{3}-', '1111-'))
