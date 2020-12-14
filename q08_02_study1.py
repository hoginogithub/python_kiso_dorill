from datetime import datetime
from time import time

now_time = datetime.now()
#print(now_time)
print(f'datetime.now type:{type(now_time)}')
print(f'now_time: {now_time}')
print(f'datetime.microsecond type:{type(now_time.microsecond)}')
print(f'now_time.microsecond: {now_time.microsecond}')
print(f'1e6:{1e6:,} type 1e6: {type(1e6)}')
print(f'datetime.timestamp type:{type(now_time.timestamp)}')
print(f'now_time.timestamp: {now_time.timestamp()}')


#for x in  dir(today_time):
#    print(str(x))

es = time()
#print(f'time type:{type(es)}')
es_datetime = datetime.fromtimestamp(es)
print(es_datetime)
