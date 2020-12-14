from multiprocessing import Process, Array

def add_all(a, b, i, r):
    for n in range(a, b+1):
        r[i] += n

if __name__ == '__main__':
    wk_num = 10
    worker = [None] * wk_num
    result = Array('i', wk_num)

    for i in range(wk_num):
        start = i * 100
        end = (i + 1) * 100 - 1
        worker[i] = Process(target=add_all, args=(start, end, i, result))
        worker[i].start()

    s = 0
    for i in range(wk_num):
        worker[i].join()
        s += result[i]
    print(f'{s:,}')
    
    total = 0
    for n in range(end + 1):
        total += n
    print(f'{total:,}')

