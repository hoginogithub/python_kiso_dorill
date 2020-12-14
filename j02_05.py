import time
import datetime

fib = lambda n: n if n < 2 else fib(n-1) + fib(n-2)

start = time.time()
print(fib(15))
end = time.time()
print(datetime.datetime.fromtimestamp(end - start))