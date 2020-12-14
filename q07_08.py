from multiprocessing.pool import Pool
import argparse
import time

def add_all(fr, to):
    s = 0
    for n in range(fr, to + 1):
        s += n
    return s

parser =  argparse.ArgumentParser(description='Add Test')
parser.add_argument('-num', type=int, default=100)
args = parser.parse_args()

start_time = time.time()
process_num = 10
worker = [None] * process_num

end_num = 10_000 * args.num
division = end_num // process_num

if __name__ == '__main__':
    print('-- pool --')
    with Pool(processes=process_num) as pool:
        for i in range(process_num):
            start = i * division
            end = (i + 1) * division - 1
            #print(f'start={start:,} end={end:,}')
            worker[i] = pool.apply_async(add_all, args=(start, end))
    
        wk_sum = 0
        for i in range(process_num):
            wk_sum += worker[i].get()

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
