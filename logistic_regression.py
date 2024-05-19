import numpy
x= numpy.array([1,2,3,4,5,6,7,8,9,10]).reshape([-1,1])
y=numpy.array([1,1,1,1,1,0,0,0,0,0])
from sklearn import linear_model
logr= linear_model.LogisticRegression()
logr.fit(x,y)
predicted=logr.predict(numpy.array([5.46]).reshape([-1,1]))
print(predicted)
