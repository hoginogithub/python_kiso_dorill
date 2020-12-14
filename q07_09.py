from multiprocessing import Process, Queue
import argparse
import time

def add_all(fr, to, index, queue):
    s = 0
    for n in range(fr, to + 1):
        s += n
    queue.put((index, s))

parser =  argparse.ArgumentParser(description='Add Test')
parser.add_argument('-num', type=int, default=100)
args = parser.parse_args()

start_time = time.time()
process_num = 10
worker = [None] * process_num
result = [0] * process_num
q = Queue()

end_num = 10_000 * args.num
division = end_num // process_num

if __name__ == '__main__':
    print('-- process with queue --')
    for i in range(process_num):
        start = i * division
        end = (i + 1) * division - 1
        #print(f'start={start:,} end={end:,}')
        worker[i] = Process(target=add_all, args=(start, end, i, q))
        worker[i].start()
    
    for i in range(process_num):
        worker[i].join()
        value = q.get()
        result[value[0]] = value[1]
        
    print('total={:,}'.format(sum(result)))
    print('time={}'.format(time.time() - start_time))

    print('-- normal --')
    start_time = time.time()
    s = 0
    for n in range(end_num):
        s += n
    print('total={:,}'.format(s))
    print('time={}'.format(time.time() - start_time))

    if sum(result) == s:
        print('OK')
    else:
        print('!!! Unmatch !!!')
