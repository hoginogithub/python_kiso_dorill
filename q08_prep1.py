# https://kenyu-life.com/2019/05/14/iris/
from sklearn.datasets import load_iris
from sklearn.datasets import load_breast_cancer
import pandas as pd
import mglearn
import matplotlib.pyplot as plt

def print_dataeset(name, dataset):
    print(f'-- {name} dataset ----------------------------')
    print(f'datasets type={type(dataset)}')
    print(f'keys set={dataset.keys()}')
    print(dataset['DESCR'])
    print(f'dataset[\'data\'] type={type(dataset["data"])}')
    print(f'dataset[\'data\'].shape = {dataset["data"].shape}')
    print(f'dataset[\'data\'].[:5] ={dataset["data"][:5]}')
    print(f'dataset[\'target\'] type={type(dataset["target"])}')
    print(f'dataset[\'target\'].shape = {dataset["target"].shape}')
    #print(f'dataset[\'target\'].[:5] ={dataset["target"][:5]}')
    print(f'dataset[\'target\'] ={dataset["target"]}')
    print(f'dataset[\'feature_names\'] ={dataset["feature_names"]}')

def plot_dataset(dataest):
    dataframe = pd.DataFrame(data=dataset["data"], columns=dataset["feature_names"])
    datalabel = pd.Series(data=dataset["target"])

    gr = pd.plotting.scatter_matrix(dataframe, c=datalabel, figsize=(8,8), marker='.', hist_kwds={'bins':20}, s=60, alpha=.8, cmap=mglearn.cm3)
    plt.show()

dataset = load_iris()
print_dataeset('iris', dataset)
plot_dataset(dataset)

dataset = load_breast_cancer()
print_dataeset('breast_cancer', dataset)
#plot_dataset(dataset)
