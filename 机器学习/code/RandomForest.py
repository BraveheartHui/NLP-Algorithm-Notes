# coding: utf-8

from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import GridSearchCV

from data_preprocess import get_train_test

x_train, x_test, y_train, y_test = get_train_test()

rf = RandomForestClassifier(oob_score=True,   # 是否采用袋外样本来评估模型的好坏
                            random_state=10,
                            n_estimators=60)
rf.fit(x_train, y_train)
y_pred = rf.predict(x_test)
y_predprob = rf.predict_proba(x_test)[:, 1]
print('oob scores : ', rf.oob_score_)
print('Origin Accuracy : %.4g' % metrics.accuracy_score(y_test.values, y_pred))
print('Origin AUC Score (Train): %f' % metrics.roc_auc_score(y_test, y_predprob))

grid_param = {'max_depth': range(10, 71, 10)}  # 决策树的最大深度
gSearch = GridSearchCV(estimator=RandomForestClassifier(oob_score=True,
                                                        n_estimators=60,
                                                        max_features='sqrt',  # 划分子树时考虑的最大特征数
                                                        min_samples_leaf=1,  # 叶子节点最小的样本数
                                                        min_samples_split=2,  # 子树继续划分的条件（样本数）
                                                        max_leaf_nodes=None,  # 最大叶子节点数
                                                        min_impurity_split=None  # 结点划分最小不纯度，该值限制决策树的增长
                                                        ),
                       param_grid=grid_param,
                       scoring='roc_auc',
                       iid=True,
                       cv=5)
gSearch.fit(x_train, y_train)
y_pred2 = gSearch.predict(x_test)
y_predprob2 = gSearch.predict_proba(x_test)[:, 1]
print('\n', gSearch.best_params_, gSearch.best_score_, '\n')
print('oob scores : ', rf.oob_score_)
print('After Accuracy : %.4g' % metrics.accuracy_score(y_test.values, y_pred2))
print('After AUC Score (Test): %f' % metrics.roc_auc_score(y_test, y_predprob2))

'''
oob scores :  0.9826875
Origin Accuracy : 0.9845
Origin AUC Score (Train): 0.693618

 {'max_depth': 10} 0.8066946727988774 

oob scores :  0.9826875
After Accuracy : 0.9855
After AUC Score (Test): 0.849208
'''