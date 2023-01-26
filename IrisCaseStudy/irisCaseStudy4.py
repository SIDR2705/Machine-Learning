from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import numpy as np


iris = load_iris() # 1 Load the data

print("Feature names of iris dataset")
print(iris.feature_names)

print("Target names of iris dataset")
print(iris.target_names)

#Indices of removed elements
test_index=[1,51,101]

#Training data with removed elements
train_target=np.delete(iris.target,test_index)
train_data=np.delete(iris.data,test_index,axis=0)

#Testing data for testing on training data
test_target=iris.target[test_index]
test_data=iris.data[test_index]

classifier= tree.DecisionTreeClassifier()

classifier.fit(train_data,train_target)

print("Values that we removed for testing")
print(test_target)

print("Result of testing")
print(classifier.predict(test_data))