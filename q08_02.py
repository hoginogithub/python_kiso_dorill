from q08_base import *

def elapsed_time(func):
    def wrapper(*args, **kargs):
        print('------------')
        start = datetime.datetime.now()
        result = func(*args, **kargs)
        end = datetime.datetime.now()
        print(f'elapsed: {(end - start).microseconds / 1e6}sec')
        return result
    return wrapper

@elapsed_time
def eval_model(model, X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0)
    model.fit(X_train, y_train)
    predicted = model.predict(X_test)
    return y_test, predicted, accuracy_score(y_test, predicted)

dataset = load_iris()

#デフォルトのランダムフォレスト
rf = RandomForestClassifier(random_state=0)

#ハイパーパラメータを設定したランダムフォレスト
rf_par = RandomForestClassifier(n_estimators=500, max_depth=100, random_state=0)

#k近傍法による分類器
knn_par = KNeighborsClassifier(n_neighbors=7, p=3)

for name, model, in [('rf', rf), ('rf_par', rf_par), ('knn_par', knn_par)]:
    y_test, predicted, accuracy = eval_model(model, dataset["data"], dataset["target"])
    print(f"Accuracy of {name}: {accuracy}")
    print(confusion_matrix(y_test, predicted))