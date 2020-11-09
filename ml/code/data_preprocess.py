import pandas as pd
from sklearn.model_selection import train_test_split


def get_train_test():
    train = pd.read_csv('data/train_modified.csv')
    target = 'Disbursed'
    IDcol = 'ID'
    print(train['Disbursed'].value_counts())
    x_columns = [x for x in train.columns if x not in [target, IDcol]]
    X = train[x_columns]
    y = train['Disbursed']

    # 划分训练集和测试集
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    return x_train, x_test, y_train, y_test