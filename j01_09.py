import datetime

def display_date(dt):
    print(dt.strftime('%Y年%m月%d日'))    

weeks = 5

dt = datetime.datetime.now()
display_date(dt)

d = weeks * 7

if dt.hour <=18:
   d += 1

td = datetime.timedelta(days=d)
dt += td
display_date(dt)