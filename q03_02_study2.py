class Counter:

    def __init__(self):
        self.created = 0
        self.created += 1

a = Counter()
print(a.created)

b = Counter()
print(b.created)

del a
del b

c = Counter()
print(c.created)