from q08_base import *

dataset = load_wine()
'''
print(f'wine data type {type(dataset)}')
for x in dir(dataset):
    print(x)
print(f'wine data {dataset["DESCR"]}')
'''

print(f'original shape: {dataset["data"].shape}')

#k-分割交差検証
# n_splits=分割数 shuffle=Trueランダムにデータを選択する、random_state=ランダムのシードを指定できる
kfold = KFold(n_splits=3, shuffle=True, random_state=0)
dim = 5

#主成分分析(PCA)による次元削減
pca = PCA(n_components=dim)

#多次元尺度構成法(MDS)による次元削減
mds = MDS(n_components=dim, random_state=0)

#相互情報量(mutual_info_classif)の上位k個を選択
kbest = SelectKBest(mutual_info_classif, k=dim)
model = RandomForestClassifier(random_state=0)

#transformed_attr = set()
for name, transformer in [('PCA', pca), ('MDS', mds), ('kbest', kbest)]:
    #print(f'{name}: type={type(transformer)} dir={dir(transformer)}')
    #for x in dir(transformer):
    #    transformed_attr.add(x)
    transformed = transformer.fit_transform(dataset['data'], dataset['target'])
    accuracy = cross_val_score(model, transformed, dataset['target'], cv=kfold, scoring="accuracy")

    print('-------------------')
    print(f'shape of {name}: {transformed.shape}')
    print(f'accuracy of {name}: {accuracy}')
    print(f'mean of {name}: {transformed.mean(axis=0)}')

'''
for x in transformed_attr:
    print(x)
print('fit_transform' in transformed_attr)
'''

    