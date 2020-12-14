from threading import Thread, Lock
import time
import argparse

def add_value(value):
    global cumulative
    global args
    if not lock.acquire(blocking=False):
        raise Exception
        #raise Exception('競合が発錆しました')
    if args.no_lock:
        lock.acquire() # 計算が正しくなるように追加した
    cumulative += value
    if args.no_lock:
        lock.release() # 計算が正しくなるように追加した

def add_all(fr, to):
    for n in range(fr, to + 1):
        try:
            add_value(n)
        except Exception:
            time.sleep(0.001)
            add_value(n)

parser = argparse.ArgumentParser(description="Add Test")
parser.add_argument('-r', type=int, default=1000)
parser.add_argument('-no_lock', action='store_false')
args = parser.parse_args()

print('-- thread --')
start_time = time.time()
cumulative = 0
calc_size = args.r
th = [None] * calc_size

#print(f'no lock flag={args.no_lock}')

if args.no_lock:
    lock = Lock()  # 計算が正しくなるように追加した
for i in range(calc_size):
    start = i * 10_000
    end = (i + 1) * 10_000 - 1
    # print(f'start={start:,} end={end:,}')
    th[i] = Thread(target=add_all, args=(start, end))
    th[i].start()

for i in range(calc_size):
    th[i].join()

print('total={:,}'.format(cumulative))
print('time={}'.format(time.time() - start_time))

print('-- mormal --')
start_time = time.time()
s = 0
for n in range(calc_size * 10_000):
    s += n
print('total={:,}'.format(s))
print('time={}'.format(time.time() - start_time))

if cumulative == s:
    print('OK')
else:
    print('!!! Unmatch !!!')