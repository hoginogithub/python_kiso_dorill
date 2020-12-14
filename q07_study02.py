# ThreadPoolExecuterはExecuterの具象クラス
from concurrent.futures import (
    ThreadPoolExecutor,
    Future,
    as_completed
)
import time
import argparse

# 時間計測
def elapsed_time(fnc):
    def wrapper(*args, **kwargs):
        st = time.time()
        v = fnc(*args, **kwargs)
        print(f'{fnc.__name__}: {time.time() - st}')
        return v
    return wrapper

# 非同期に行いたい処理
def add_all(fr, to):
    time.sleep(1)
    s = 0
    for n in range(fr, to + 1):
        s += n
    return s

# normal add
@elapsed_time
def normal_add(end_num):
    s = 0
    for n in range(0, end_num):
        s += n
    print('total={:,}'.format(s))

# thread add
@elapsed_time
def thread_add(end_num):
    work_num = 10
    division = end_num // work_num

    futures = []
    s = 0
    with ThreadPoolExecutor(max_workers = work_num) as executor:
        for i in range(work_num):
            start = i * division
            end = (i + 1) * division - 1
            futures.append(executor.submit(add_all, start, end))
        for future in as_completed(futures):
            s += future.result()
    print('total={:,}'.format(s))

parser =  argparse.ArgumentParser(description='Add Test')
parser.add_argument('-num', type=int, default=100)
args = parser.parse_args()

end_num = 10_000 * args.num

normal_add(end_num)
thread_add(end_num)