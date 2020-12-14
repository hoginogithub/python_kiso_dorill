from q08_base import *

dataset = load_wine()

# 1<= k <=9, 3<= n_neighbors <=7 の探索空間を定義
search_space = {'kbest__k': range(1,10),
                'model__n_neighbors': range(3,8) }

kbest_knn = Pipeline([('kbest', SelectKBest(mutual_info_classif)),('model', KNeighborsClassifier())])
X_train, X_test, y_train, y_test = train_test_split(dataset['data'], dataset['target'], test_size=0.33, random_state=0)

# search_space内をGridSearchCV関数で探索
grid_cv = GridSearchCV(kbest_knn, param_grid=search_space, cv=4)
grid_cv.fit(X_train, y_train)
#for x in dir(grid_cv):
#    print(x)

# 最も優秀だったパラメータの条件を表示
print(f'best parameters: {grid_cv.best_params_}')
print(f'best score: {grid_cv.best_score_}')

# 探索したパラメータでテストデータを予測
predicted = grid_cv.predict(X_test)
print(f'score of test_data: {accuracy_score(y_test, predicted)}')