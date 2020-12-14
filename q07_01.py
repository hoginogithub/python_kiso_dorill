from threading import Thread
from functools import reduce
import time
import random

def add_all(fr, to, index):
    #if index % 2:
    #    time.sleep(1)
    #print({index})
    s = 0
    for n in range(fr, to + 1):
        s += n
    result[index] = s

print('-- thread --')
start_time = time.time()
calc_size = 10
result = [0] * calc_size
th = [None] * calc_size
th_list = [x for x in random.sample(range(0, calc_size), calc_size)]
print(th_list)
#start_index = [range(0, calc_size)]

for i in range(calc_size):
    start = i * 10_000
    end = (i + 1) * 10_000 - 1
    #print(f'start={start:,} end={end:,}')
    for j in th_list:
        th[j] = Thread(target=add_all, args=(start, end, j))
        th[j].start()

for i in th_list:
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