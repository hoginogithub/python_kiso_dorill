from multiprocessing import Process, Array
import time

def add_all(fr, to, index, array):
    s = 0
    for n in range(fr, to + 1):
        s += n
    array[index] = s

num = 100

print('-- process --')
start_time = time.time()
wk_num = 10
result = Array('q', wk_num)
worker = [None] * wk_num

end_num = 10_000 * num
division = end_num // wk_num

if __name__ == '__main__':
    for i in range(wk_num):
        start = i * division
        end = (i + 1) * division - 1
        #print(f'start={start:,} end={end:,}')
        worker[i] = Process(target=add_all, args=(start, end, i, result))
        worker[i].start()
    wk_sum = 0
    for i in range(wk_num):
        worker[i].join()
        #print(result)
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
