import json
import datetime
import time

file_name = 'q06_08_a.json'
with open(file_name, 'r', encoding='utf_8') as f:
    info = json.load(f)

#[print(x) for x in info]
#print(type(info))
#[print(type(json.loads(x))) for x in info]
#[print(json.loads(x).get('size')) for x in info]
#info_list = [json.loads(x).pop('last_modification') for x in info]
#info_list = [del json.loads(x)['last_modification'] for x in info]
info_list = []
for x in info:
    #print('last_modification' in json.loads(x))
    tmp1 = json.loads(x)
    es = tmp1.pop('last_modification')
    tmp1['last_modification'] = datetime.datetime.fromtimestamp(es).strftime('%Y-%m-%d %H:%M:%S.%f')
    info_list.append(tmp1)

#print(info_list)
#[print(x.get('last_modification')) for x in info_list]
#[datetime.datetime.fromtimestamp(x.get('last_modification')) for x in info_list]

file_size_sorted = sorted(info_list, key=lambda x: x.get('size'))
[print(x) for x in file_size_sorted]

'''
with open(file_name, 'r', encoding='utf_8') as f:
    tmp = json.load(f)

print(tmp)
'''