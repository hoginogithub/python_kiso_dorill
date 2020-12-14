import re

def hexa_color_validation(hexa_color):
    hexa_pattern = r'^#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$'
    return re.search(hexa_pattern, hexa_color) is not None

print(hexa_color_validation('#fff'))
print(hexa_color_validation('#24ff30'))
print(hexa_color_validation('#ABC'))
print(hexa_color_validation('#fof'))
print(hexa_color_validation('#1234'))
print(hexa_color_validation('#SUV'))