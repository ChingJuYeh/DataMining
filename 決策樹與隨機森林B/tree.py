# In[1]:
import pandas as pd
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
from sklearn.tree import export_graphviz
from six import StringIO  
from IPython.display import Image  
import pydotplus
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree

diabetestrain=pd.read_csv("train_data (1).csv")
diabetestest=pd.read_csv("test_data (1).csv")
#x_train讀進train_data.csv除了Outcome以外的數值
x_train=diabetestrain.drop(['Outcome'], axis=1) #刪除Output那列
x_train


# In[30]:


#y_train讀進train_data.csv的Outcome之值
y_train = diabetestrain.Outcome
y_train


# In[31]:

x_test = diabetestest.drop(['Outcome'], axis=1)
x_test

# In[32]:

y_test = diabetestest.Outcome
y_test


# In[33]:

# 建立決策樹classifier
model = DecisionTreeClassifier(criterion="gini") #用基尼係數建立決策樹模型
# train決策樹classifier
model = model.fit(x_train,y_train) #執行訓練
# 預測x_test中的Outcome
y_pred = model.predict(x_test) #樣本屬於每一個類別的機率


# In[34]:
# 準確率:用預測比對test_data中的Outcome
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
# In[35]:

features=x_train.columns
features

# In[36]:
dot_data = StringIO() #讀取字串
export_graphviz(model, out_file=dot_data,filled=True, rounded=True,special_characters=True, feature_names = features,class_names=['0','1'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('decisionforest.png')
Image(graph.create_png())

# In[37]:
print("Feature importances :\n{}".format(model.feature_importances_)) #基尼係數越小，不純度越低，特徵越好 #顯示八個項目和糖尿病間的相關性

# In[38]:
diabetes_features = [x for i,x in enumerate(x_test.columns) if i!=8] #將一個可遍歷數據對象組合為一個索引數列，同時列出數據和數據下標，一般用在for-loop中
def plot_feature_importances_diabetes(model):
    plt.figure(figsize=(8,6))
    n_features = 8
    plt.barh(range(n_features), model.feature_importances_, align='center')
    plt.yticks(np.arange(n_features), diabetes_features)
    plt.xlabel("Feature importance")
    plt.ylabel("Feature")
    plt.ylim(n_features,-1)
plot_feature_importances_diabetes(model)
plt.savefig('feature_importance_decision')




# In[39]:

bestd= 3 #哪個深度最好
model3 = DecisionTreeClassifier(criterion="gini", max_depth=3)
model3 = model3.fit(x_train,y_train)
y_pred = model.predict(x_test)
maxd = metrics.accuracy_score(y_test, y_pred)#紀錄最高準確率
# 建立決策樹classifier 讓深度最大只有3 限制樹的深度以降低過擬合
for i in range(4,100):
    model3 = DecisionTreeClassifier(criterion="gini", max_depth=i)
    model3 = model3.fit(x_train,y_train) 
    y_pred = model3.predict(x_test)
    testd = metrics.accuracy_score(y_test, y_pred)
    if(maxd<testd):
        maxd = testd
        bestd = i
print("the best depth is ",bestd,",and accuracy is",maxd)


# In[40]:
#用最佳深度重建model
model3 = DecisionTreeClassifier(criterion="gini", max_depth=bestd)
model3 = model3.fit(x_train,y_train) 
y_pred = model3.predict(x_test)

dot_data = StringIO()
export_graphviz(model3, out_file=dot_data,filled=True, rounded=True,special_characters=True, feature_names = features,class_names=['0','1'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('forest_maxdepth.png')
Image(graph.create_png())


# In[41]:


print("Feature importances:\n{}".format(model.feature_importances_))


# In[42]:


diabetes_features = [x for i,x in enumerate(x_test.columns) if i!=8]
def plot_feature_importances_diabetes(model):
    plt.figure(figsize=(8,6))
    n_features = 8
    plt.barh(range(n_features), model.feature_importances_, align='center')
    plt.yticks(np.arange(n_features), diabetes_features)
    plt.xlabel("Feature importance")
    plt.ylabel("Feature")
    plt.ylim(n_features,-1)
plot_feature_importances_diabetes(model)
plt.savefig('feature_importance_maxdepth')

#In[43]:
#using random forest to build a model
model2 = RandomForestClassifier(n_estimators=100, random_state=0)
model2.fit(x_train,y_train)
y_pred2 = model2.predict(x_test)
print("Feature importances:\n{}".format(model2.feature_importances_))
print("Accuracy:",metrics.accuracy_score(y_test, y_pred2))
pred = model2.estimators_[0].predict(x_test.values)
max = metrics.accuracy_score(y_test, pred)
maxi = 0
for i in range (1,100):
    pred = model2.estimators_[i].predict(x_test.values)
    p = metrics.accuracy_score(y_test, pred)
    if max < p :
        max = p
        maxi= i
print("voting accuracy:",max)
print("maxi=",maxi)
#In[44]:
#random_forest graphiz
dot_data = StringIO()
export_graphviz(model2.estimators_[maxi], out_file=dot_data,filled=True, rounded=True,special_characters=True, feature_names = features,class_names=['0','1'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('forest_maxdepth2.png')
Image(graph.create_png())
diabetes_features = [x for i,x in enumerate(x_test.columns) if i!=8] #將一個可遍歷數據對象組合為一個索引數列，同時列出數據和數據下標，一般用在for-loop中
#In[45]:
#randomforest_ bar chart
def plot_feature_importances_diabetes2(model2):
    plt.figure(figsize=(8,6))
    n_features = 8
    plt.barh(range(n_features), model2.estimators_[maxi].feature_importances_, align='center')
    plt.yticks(np.arange(n_features), diabetes_features)
    plt.xlabel("Feature importance")
    plt.ylabel("Feature")
    plt.ylim(n_features,-1)
plot_feature_importances_diabetes2(model2)
plt.savefig('feature_importance_random')

#In[46]:
#adding Bagging to decision tree
model1 = BaggingClassifier(model, n_estimators=100, max_samples=0.8,
                        random_state=1)
model1 = model1.fit(x_train,y_train)
y_pred1 = model1.predict(x_test)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred1))
feature_importances = np.mean([
    tree.feature_importances_ for tree in model1.estimators_
], axis=0)
print("feature importances:",feature_importances)
#In[47]:
def plot_feature_importances_diabetes(model1):
    plt.figure(figsize=(8,6))
    n_features = 8
    plt.barh(range(n_features), feature_importances, align='center')
    plt.yticks(np.arange(n_features), diabetes_features)
    plt.xlabel("Feature importance")
    plt.ylabel("Feature")
    plt.ylim(n_features,-1)
plot_feature_importances_diabetes(model)
plt.savefig('feature_importance_bagging')
# %%
