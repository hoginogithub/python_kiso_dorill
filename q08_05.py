from q08_base import *

dataset = load_iris()

'''
for x in dir(dataset):
    print(x)
'''

# load_iris()の結果からDataFrameを作成
df = pd.DataFrame(dataset['data'], columns=dataset['feature_names'])
print(f'original shape: {df.shape}')
print(df.describe())

# sepal(がく)の長さが5cm以上かどうかを示す列を作成する
df['sepal is long'] = df['sepal length (cm)'] > 5

# sepal(がく)の長さが5cm以上の行のみを取得する
long_sepal = df[df['sepal is long']]
print(f'long_sepal shape: {long_sepal.shape}')
#pd.set_option('display.max_rows', None)
print(f'{long_sepal}')

# sepal(がく)の長さと幅の和を示す列をつくる
df['sepal sum'] = df['sepal length (cm)'] + df['sepal width (cm)']
#print(df['sepal sum'])

# sepal(がく)が5cm以上かつpetal(花弁)が4cm以下である行のみ取得する
long_sepal_and_short_petal = df[df['sepal is long'] & (df['petal length (cm)'] < 4)] 
print('long_sepal_and_short_petal shape'
      f'{long_sepal_and_short_petal.shape}')
#pd.set_option('display.max_rows', None)
#print(f'{long_sepal_and_short_petal}')

# petalで始まる列を削除する
petal_removed = df[df.columns.drop(list(df.filter(regex='petal*')))]
print(f'petal_removed: {petal_removed.shape}')
print(petal_removed)