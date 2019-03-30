# coding: utf-8

from data_preprocess import get_train_test
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import metrics
from sklearn.model_selection import cross_validate, GridSearchCV, train_test_split

# 划分训练集和测试集
x_train, x_test, y_train, y_test = get_train_test()

gbm = GradientBoostingClassifier(random_state=10)
gbm.fit(x_train, y_train)
y_pred = gbm.predict(x_test)
y_predprob = gbm.predict_proba(x_test)[:, 1]

print('Accuracy : %.4g' % metrics.accuracy_score(y_test.values, y_pred))
print('AUC Score (Train): %f' % metrics.roc_auc_score(y_test, y_predprob))

grid_param = {'n_estimators' : range(20, 81, 10)}
gSearch = GridSearchCV(estimator=GradientBoostingClassifier(learning_rate=0.1,
                                                            min_samples_split=300,  # 叶子节点样本数量小于该值则不再继续划分的条件
                                                            min_samples_leaf=20,  # 叶子节点最少的样本数
                                                            max_depth=8,  # 决策树的最大深度
                                                            max_features='sqrt',  # 最多使用特征数量，None时考虑所有特征
                                                            subsample=0.8,
                                                            random_state=10),
                       param_grid=grid_param,
                       scoring='roc_auc',
                       iid=False,
                       cv=5)
gSearch.fit(x_train, y_train)
y_pred2 = gSearch.predict(x_test)
y_predprob2 = gSearch.predict_proba(x_test)[:, 1]
print(gSearch.best_params_, gSearch.best_score_)
print('Accuracy : %.4g' % metrics.accuracy_score(y_test.values, y_pred2))
print('AUC Score (Train): %f' % metrics.roc_auc_score(y_test, y_predprob2))

'''
Accuracy : 0.984
AUC Score (Train): 0.836218

{'n_estimators': 60} 0.8140045598032056

Accuracy : 0.9855
AUC Score (Train): 0.845013
'''