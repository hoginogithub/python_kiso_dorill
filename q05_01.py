import re

def jp_postal_code_validation(postal_code):
    return re.search(r'\d{3}-\d{4}', postal_code) is not None and len(postal_code) == 8

print(jp_postal_code_validation('16-0001'))
print(jp_postal_code_validation('166-0001'))
print(jp_postal_code_validation('16a-0001'))
print(jp_postal_code_validation('166a0001'))
print(jp_postal_code_validation('1666-0001'))
print(jp_postal_code_validation('16666-0001'))
print(jp_postal_code_validation('aaaa-0001'))