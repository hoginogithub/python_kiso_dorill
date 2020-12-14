import re

kit_pattern = 'kit*'

input_strings = [
    'kit',        # kit
    'kat',        # None
    'kitty',      # kitt
    'katty',      # None
    'kittkatty',  # kitt
    'toolkit',    # kit
    'kiwi',       # ki
    ''            # None
]

match = []
for m in map(lambda s: re.search(kit_pattern, s), input_strings):
    match.append(m.group(0)) if m is not None else match.append('None')
print(match)