import re

def password_validation(password):
    #pattern = r'^.{12,}$(?=[^a-z]*[a-z])(?=[^A-Z]*[A-Z])(?=\D*\d)'
    pattern = r'^(?=[^a-z]*[a-z])(?=[^A-Z]*[A-Z])(?=\D*\d).{12,}$'
    #pattern = r'^.{12,}$'

    password_regex = re.compile(pattern)

    print(re.search(pattern, password))

    return password_regex.match(password) is not None
                         #----+-----1--
print(password_validation('aA3gaekaopeH'))