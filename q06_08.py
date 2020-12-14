import os
import json
import datetime

def serialize_to_json(file):
    file_info = os.stat(file)
    info = {
        'name': os.path.basename(file),
        'size': file_info.st_size,
        'last_modification': file_info.st_mtime,
    }
    return json.dumps(info)

files = []
extensions = ('.txt', '.csv', 'dat')
for dirpath, dirnames, filenames in os.walk('.'):
    for filename in filenames:
        if filename.endswith(extensions):
            files.append(serialize_to_json(os.path.join(dirpath, filename)))

export_f = 'q06_08_' + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.json'
with open(export_f, 'w') as f:
    json.dump(files, f, indent=4)