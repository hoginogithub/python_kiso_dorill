tags = {
    'interesting': 174,
    'fascinating': 42,
    'Boring': 87,
    'Fascinating': 65,
    'Interesting': 141,
    'Funny': 91
}

print(tags.get('interesting', 0))
print(tags.get('excitement', 9999999))
tags_frequency = {
    k.lower() : tags.get(k.lower(), 0) +
                tags.get(k.capitalize(), 0)
    for k in tags.keys()
}

for k, v in tags_frequency.items():
    print(k + ':' + str(v))