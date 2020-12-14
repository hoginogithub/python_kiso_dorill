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
def eval_model(model, X, y, eval_func):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0)
    model.fit(X_train, y_train)
    predicted = model.predict(X_test)
    return y_test, predicted, eval_func(y_test, predicted)

#Accuracy 正解率 (TP + TF) / (TP + FP + FN + TF)
def my_accuracy(y_true, y_pred):
    print(f'y_true.shape {y_true.shape}')
    return (y_true == y_pred).sum() / y_true.shape[0]

#Recall 再現率 TP / TP + FN
def my_recall(y_true, y_pred):
    t = y_true == y_pred
    tpp = t & y_true
    #for x, y, z in zip(t, y_true, tpp):
    #    print(f't & y_true: {x} & {y} = {z}')
    #print(f'y_true == y_pred: {t}')
    #print(f'y_true {y_true}')
    tp = tpp.sum()
    #print(f't &  y_true {t & y_true}')
    #print(f'len y_ture {len(y_true)}')
    return tp / y_true.sum()

parser = argparse.ArgumentParser(description='select model and eval_func')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--n',action='store_true')
group.add_argument('--h',action='store_true')
group.add_argument('--k',action='store_true')
args = parser.parse_args()

dataset = load_breast_cancer()
'''
for x in dir(dataset):
    print(x)
print(f'len dataset data {len(dataset["data"])}')
print(f'feature_names {dataset["feature_names"]}')
print(f'dataset data[0,5] {dataset["data"][:5]}')
print(f'len dataset target {len(dataset["target"])}')
print(f'target_names {dataset["target_names"]}')
print(f'dataset target[0,5] {dataset["target"][:5]}')
'''

if args.k:
    model_name = 'k近傍法による分類器'
    model = KNeighborsClassifier(n_neighbors=7, p=3)
elif args.h:
    model_name = 'ハイパーパラメータを設定したランダムフォレスト'
    model = RandomForestClassifier(n_estimators=500, max_depth=100, random_state=0)
else:
    model_name = 'ランダムフォレスト(デフォルト)'
    model = RandomForestClassifier(random_state=0)

print(f'モデル{model_name}')
for name, eval_func in [('Accuracy', accuracy_score), ('My Accuracy', my_accuracy), ('Recall', recall_score), ('My Recall', my_recall)]:
    y_test, predicted, accuracy = eval_model(model, dataset["data"], dataset["target"], eval_func)
    print(f'{name}: {accuracy}')
print(confusion_matrix(y_test, predicted))
