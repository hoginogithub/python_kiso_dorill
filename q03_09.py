class Time:
    def __init__(self, mins=0, secs=0):
        self.mins = mins
        self.secs = secs

    def __str__(self):
        return '{0:02}:{1:02}'.format(self.mins, self.secs)

    def __add__(self, to_add):
        new_time = Time()
        new_time.mins = self.mins
        new_time.secs = self.secs
        new_time.secs += to_add

        if new_time.secs >= 60:
            new_time.mins += new_time.secs // 60
            new_time.secs = new_time.secs % 60

        return new_time

t = Time()
print(t)

print(Time(1, 0))
print(Time(3, 5) + 122)
