import random
import math

numbers = []
for i in range(0, 20):
    numbers.append(random.randint(0, 100))
# print('numbers size:'+str(len(numbers)))
print('numbers='+ str(numbers))
print('numbers size:'+str(len(numbers)))

#set_list = list(set(numbers))
#print('set_list:'+str(set_list))
#print('set_list size:'+str(len(set_list)))

duplicate_list = [x for x in set(numbers) if numbers.count(x) > 1]
print('dup_list:'+str(duplicate_list))
print('dup_list size:'+str(len(duplicate_list)))

#sort_list = list(dict.fromkeys(numbers))
#print('sort_list:'+str(sort_list))
#print('sort_list size:'+str(len(sort_list)))

duplicate_list2 = [x for x in dict.fromkeys(numbers) if numbers.count(x) > 1]
print('dup_list2:'+str(duplicate_list2))
print('dup_list2 size:'+str(len(duplicate_list2)))
