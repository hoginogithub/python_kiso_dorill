class Counter:
    created = 0

    def __init__(self):
        Counter.created += 1

a = Counter()
print(a.created)

b = Counter()
print(b.created)

del a
del b

c = Counter()
print(c.created)