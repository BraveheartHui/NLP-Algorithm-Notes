# coding: utf-8
from data_preprocess import get_train_test
from sklearn import metrics
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split, GridSearchCV


# 划分训练集和测试集
x_train, x_test, y_train, y_test = get_train_test()

xgb = XGBClassifier()
xgb.fit(x_train, y_train)
y_pred = xgb.predict(x_test)
y_predprob = xgb.predict_proba(x_test)[:, 1]
print('Origin Accuracy : %.4g' % metrics.accuracy_score(y_test.values, y_pred))
print('Origin AUC Score (Train): %f' % metrics.roc_auc_score(y_test, y_predprob))


# 调参
grid_param = {'n_estimators': range(100, 101),
              'max_depth': range(3, 11)}
gSearch = GridSearchCV(estimator=XGBClassifier(learning_rate=0.1,
                                               max_delta_step=0,  # 限制每棵树权重改变的最大步长
                                               subsample=1,  # 控制每棵树随机采样的比例
                                               colsample_bytree=1  # 每棵树随机采样的列数（属性）占比
                                               ),
                       param_grid=grid_param,
                       scoring='roc_auc',
                       iid=False,
                       cv=5)
gSearch.fit(x_train, y_train)
y_pred2 = gSearch.predict(x_test)
y_predprob2 = gSearch.predict_proba(x_test)[:, 1]
print(gSearch.best_params_, gSearch.best_score_)
print('After Accuracy : %.4g' % metrics.accuracy_score(y_test.values, y_pred2))
print('After AUC Score (Train): %f' % metrics.roc_auc_score(y_test, y_predprob2))


'''
0    19680
1      320
Name: Disbursed, dtype: int64
Origin Accuracy : 0.9855
Origin AUC Score (Train): 0.832942
{'max_depth': 5, 'n_estimators': 100} 0.8180064631441869
After Accuracy : 0.9855
After AUC Score (Train): 0.836566
'''