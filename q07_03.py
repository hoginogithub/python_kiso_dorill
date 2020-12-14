from threading import Thread
from functools import reduce
import time

def add_all(fr, to, index):
    s = 0
    for n in range(fr, to + 1):
        s += n
    result[index] = s

print('-- thread --')
start_time = time.time()
calc_size = 10
result = [0] * calc_size
th = [None] * calc_size

for i in range(calc_size):
    start = i * 10_000
    end = (i + 1) * 10_000 - 1
    args_d = {'fr': start, 'to': end, 'index': i}
    th[i] = Thread(target=add_all, kwargs=args_d)
    th[i].start()

for i in range(calc_size):
    th[i].join()

print('total={:,}'.format(reduce(lambda x, y: x + y, result)))
print('time={}'.format(time.time() - start_time))

print('-- mormal --')
start_time = time.time()
s = 0
for n in range(0, 100_000):
    s += n
print('total={:,}'.format(s))
print('time={}'.format(time.time() - start_time))