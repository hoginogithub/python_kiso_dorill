from threading import Thread, Barrier
#from functools import reduce
import time
import random
import argparse
import signal
import sys

def add_all(fr, to, index, barrier):
    s = 0
    for n in range(fr, to + 1):
        s += n
    result[index] = s
    barrier.wait()

def dead_end(signal, frame):
    print('Ctrl + C End')
    sys.exit(0)

parser =  argparse.ArgumentParser(description='Add Test')
parser.add_argument('-num', type=int, default=100)
parser.add_argument('-ng', action='store_const', const=0, default=1)
args = parser.parse_args()

signal.signal(signal.SIGINT, dead_end)

print('-- thread --')
start_time = time.time()
th_num = 10
result = [0] * th_num
th = [None] * th_num
b = Barrier(th_num + args.ng)

end_num = 10_000 * args.num
division = end_num // th_num

for i in range(th_num):
    start = i * division
    end = (i + 1) * division - 1
    #print(f'start={start:,} end={end:,}')
    th[i] = Thread(target=add_all, args=(start, end, i, b))
    th[i].start()

b.wait()

th_sum = sum(result)

print('total={:,}'.format(th_sum))
print('time={}'.format(time.time() - start_time))

print('-- normal --')
start_time = time.time()
s = 0
for n in range(end_num):
    s += n
print('total={:,}'.format(s))
print('time={}'.format(time.time() - start_time))

if th_sum == s:
    print('OK')
else:
    print('!!! Unmatch !!!')
