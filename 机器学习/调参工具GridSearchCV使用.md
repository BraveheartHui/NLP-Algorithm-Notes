### 作用

`sklearn`模块的`GridSearchCV`模块，能够在指定的范围内自动搜索具有不同超参数的不同模型组合，有效获得模型最佳参数组合。

### 导入模块

`from sklearn.model_selection import GridSearchCV`

### 参数介绍 

```python
def __init__(self, estimator, param_grid, scoring=None, fit_params=None,
                 n_jobs=None, iid='warn', refit=True, cv='warn', verbose=0,
                 pre_dispatch='2*n_jobs', error_score='raise-deprecating',
                 return_train_score="warn"):
    super(GridSearchCV, self).__init__(estimator=estimator, 
                                       scoring=scoring, 
                                       fit_params=fit_params,
                                       n_jobs=n_jobs, 
                                       iid=iid, 
                                       refit=refit, 
                                       cv=cv, 
                                       verbose=verbose, 
                                       pre_dispatch=pre_dispatch, 
                                       error_score=error_score, 
                                       return_train_score=return_train_score)
    self.param_grid = param_grid
```

- `estimator` : 分类器，如`GradientBoostingClassifier`。
- `param_grid` : 参数列表，格式为字典或者字典的列表。其中，参数名字作为key，参数的取值作为value。
- `scoring` : 结果的评价指标，如`roc_auc`。
- `n_jobs` : 并行数，默认1。
- `cv` : 交叉验证折数，默认3-折交叉验证。
- `iid` : 默认为True，即假设每一折样本具有相同的分布，并最小化样本的总损失。为False时是使用每一折的平均损失。
- `refit` : 默认为True，即在找到最佳参数组合之后，应用最佳参数重新fit一遍数据集。

### 属性

- `best_params_` : 最优参数结果。
- `best_score_` : 最优参数下交叉验证的结果。

--------

具体使用样例见：

- [XGBOOST.py](https://github.com/BraveheartHui/NLP-Algorithm-Notes/blob/master/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/code/GBDT.py)
- [GBDT.py](https://github.com/BraveheartHui/NLP-Algorithm-Notes/blob/master/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/code/GBDT.py)
- [RandomForest.py](https://github.com/BraveheartHui/NLP-Algorithm-Notes/blob/master/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/code/RandomForest.py)

参考博客:

- [sklearn学习8-----GridSearchCV(自动调参）](http://www.cnblogs.com/Lee-yl/p/9190192.html)
