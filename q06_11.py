import signal
import sys
import datetime

def log_time(signal, frame):
    '''
    Function called when the program closes
    '''
    print(f'signal type = {type(signal)} {signal}')
    print(f'frame type = {type(frame)} {frame}')
    with open('q06_11_out.txt', 'a', encoding='utf_8') as f:
        f.write(f'Script interrupted - {datetime.datetime.now()}\n')
        sys.exit(0)

print(f'signal.SIGINT={signal.SIGINT}')
signal.signal(signal.SIGINT, log_time)

while True:
    pass