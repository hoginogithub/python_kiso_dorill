class Counter:
    created = 0

    def __init__(self):
        Counter.created += 1

    @classmethod
    def how_many(cls):
        return cls.created

    def __del__(self):
        Counter.created = 0

a = Counter()
b = Counter()
print(a.how_many())
print(b.how_many())
del a
print(b.how_many())
c = Counter()
print(c.how_many())
del b
print(c.how_many())