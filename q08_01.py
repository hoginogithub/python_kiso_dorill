from q08_base import *
import pandas as pd
import mglearn
import matplotlib.pyplot as plt

iris = load_iris()
#print(f'type iris: {type(iris)}')
#print(iris)
#print(f'type iris.data {type(iris.data)}')
#print(f'len iris.data {len(iris.data)}')
#print(f'iris.data {iris.data}')
#print(f'type iris.target {type(iris.target)}')
#print(f'len iris.target {len(iris.target)}')
#print(f'iris.target {iris.target}')
X_train, X_test, y_train, y_test = \
    train_test_split(iris['data'], iris['target'], 
                     test_size=0.33, random_state=0)

'''
print(f'len X_train {len(X_train)}')
print(f'type X_train {type(X_train)}')
print(f'X_train {X_train}')
print(f'len y_train {len(y_train)}')
print(f'type y_train {type(y_train)}')
print(f'y_train {y_train}')
print(f'len X_test {len(X_test)}')
print(f'type X_test {type(X_test)}')
print(f'X_test {X_test}')
print(f'len y_test {len(y_test)}')
print(f'type y_test {type(y_test)}')
print(f'y_test {y_test}')
'''
'''
test_dataframe = pd.DataFrame(X_train, columns=iris["feature_names"])
test_datalebel = pd.Series(y_train)
gr1 = pd.plotting.scatter_matrix(test_dataframe, c=test_datalebel)
plt.show()
'''

model = RandomForestClassifier(random_state=0)
model.fit(X_train, y_train)
predicted = model.predict(X_test)

print(confusion_matrix(y_test, predicted))

print(f'Acuuracy: {accuracy_score(y_test, predicted)}')
print(f'predicted: \n{predicted}')
