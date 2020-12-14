import re

def password_validation(password):
    #pattern = r'Hello (?=World)'
    #pattern = r'.*(?=World)'
    #pattern = r'^.{12,}$'
    pattern = r'(?=Hello).+$'

    return re.search(pattern, password)

def pass_val(pass_word):
    pattern = r'(?=[^A-Z]*[A-Z])(\D*\d)'
    return re.search(pattern, pass_word)
                     #----+-----1--
print(password_validation('Hello'))
print(password_validation('Hello World'))
print(password_validation('HelloWorld'))
print(password_validation('ZZZZ bbbb Hello ddd World'))
print(pass_val('abC'))