import re

class PhoneReformatError(Exception):
    pass

def validate_phone_number(phone_number):
    pattern = '^0[1-9]([.\s-]?[0-9]{2}){4}'
    if re.match(pattern, phone_number):
        return re.sub('[.\s-]', '', phone_number)
    else:
        #raise PhoneReformatError
        raise PhoneReformatError('Invalid Phone Number.')

try:
    print(validate_phone_number('08.36.65.65.65'))
    print(validate_phone_number('08 36 65 65 65'))
    print(validate_phone_number('08-36-65-65-65'))
    print(validate_phone_number('00.36.65.65.65'))
except PhoneReformatError as iErr:
    print(iErr)

