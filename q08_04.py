from q08_base import *
import argparse

def elapsed_time(func):
    def wrapper(*args, **kargs):
        print('------------')
        print(f'{args[3]}')
        start = datetime.datetime.now()
        result = func(*args, **kargs)
        end = datetime.datetime.now()
        print(f'elapsed: {(end - start).microseconds / 1e6}sec')
        return result
    return wrapper

@elapsed_time
def my_cv(model, X, y, kfold):
    result = []
    for train_index, test_index, in kfold.split(X):
        model.fit(X[train_index], y[train_index])
        predicted = model.predict(X[test_index])
        result.append(accuracy_score(y[test_index], predicted).round(8))
        print(confusion_matrix(y[test_index], predicted))
    return result 

parser = argparse.ArgumentParser(description='select model and eval_func')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--n',action='store_true')
group.add_argument('--h',action='store_true')
group.add_argument('--k',action='store_true')
args = parser.parse_args()

dataset = load_breast_cancer()

if args.k:
    model_name = 'k近傍法による分類器'
    model = KNeighborsClassifier(n_neighbors=7, p=3)
elif args.h:
    model_name = 'ハイパーパラメータを設定したランダムフォレスト'
    model = RandomForestClassifier(n_estimators=500, max_depth=100, random_state=0)
else:
    model_name = 'ランダムフォレスト(デフォルト)'
    model = RandomForestClassifier(random_state=0)

kfold = KFold(n_splits=3, shuffle=True, random_state=0)

print(f'モデル{model_name}')

cv_acc = cross_val_score(model, dataset.data, dataset.target, cv=kfold, scoring='accuracy')
my_cv_acc = my_cv(model, dataset.data, dataset.target, kfold)

print(f'CV accuracy: {cv_acc}')
print(f'My CV accuracy: {my_cv_acc}')