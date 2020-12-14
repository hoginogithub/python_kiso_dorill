# ThreadPoolExecuterはExecuterの具象クラス
from concurrent.futures import (
    ThreadPoolExecutor, 
    Future
)

import time

# 非同期に行いたい処理
def add_all(fr, to):
    time.sleep(1)
    s = 0
    for n in range(fr, to + 1):
        s += n
    return s

# 非同期に行いたい処理をsubumitに渡す　-> Futuerクラスのインスタンスが返される
future = ThreadPoolExecutor().submit(add_all, 1, 4)
print(f'futuer is Future? :{isinstance(future, Future)}')

print(f'future done ? (呼び出しが終了したか？キャンセルしたか？) {future.done()}')
print(f'future running? (キャッセルできない状態か？) {future.running()}')
print(f'future cancel {future.cancelled()}')
print(future.result())
print(f'future done ? (呼び出しが終了したか？キャンセルしたか？) {future.done()}')
