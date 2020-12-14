import random
import math

numbers = []
for i in range(0, 20):
    numbers.append(random.randint(0, 100))
# print('numbers size:'+str(len(numbers)))
print('numbers='+ str(numbers))
print('numbers size:'+str(len(numbers)))

numbers = set(numbers)
# print('numbers size(non duplicate):'+str(len(numbers)))
print('numbers (non duplicate):'+str(numbers))
print('numbers size(non duplicate):'+str(len(numbers)))

squares = [n for n in numbers if math.sqrt(n).is_integer()]
print('squares:'+str(squares))