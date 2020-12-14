from multiprocessing import Process
import time
import random
import argparse
import signal
import sys

def add_all(fr, to, index):
    s = 0
    for n in range(fr, to + 1):
        s += n
    result[index] = s

def dead_end(signal, frame):
    print('Ctrl + C End')
    sys.exit(0)


if __name__ == '__main__':
    parser =  argparse.ArgumentParser(description='Add Test')
    parser.add_argument('-num', type=int, default=100)
    #parser.add_argument('-ng', action='store_const', const=0, default=1)
    args = parser.parse_args()

    signal.signal(signal.SIGINT, dead_end)

    print('-- process --')
    start_time = time.time()
    wk_num = 10
    result = [0] * wk_num
    worker = [None] * wk_num

    end_num = 10_000 * args.num
    division = end_num // wk_num

    for i in range(wk_num):
        start = i * division
        end = (i + 1) * division - 1
        #print(f'start={start:,} end={end:,}')
        worker[i] = Process(target=add_all, args=(start, end, i))
        worker[i].start()
    wk_sum = 0
    for i in range(wk_num):
        worker[i].join()
        print(result)
        wk_sum += result[i]

    print('total={:,}'.format(wk_sum))
    print('time={}'.format(time.time() - start_time))

    print('-- normal --')
    start_time = time.time()
    s = 0
    for n in range(end_num):
        s += n
    print('total={:,}'.format(s))
    print('time={}'.format(time.time() - start_time))

    if wk_sum == s:
        print('OK')
    else:
        print('!!! Unmatch !!!')
