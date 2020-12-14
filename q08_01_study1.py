from sklearn.model_selection import train_test_split
import numpy as np

a = np.arange(10)
print(f'type np.arange {type(a)} a={a}')

b = train_test_split(a, test_size=0.33, random_state=0)
print(f'type train_test_split {type(b)}')
print(f'train_test_split {b}')
print(f'train_test_split list 0 {type(b[0])}')