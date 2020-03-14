#Independent variables
import numpy as np
import matplotlib.pyplot as plt 
#Independent variables
input_set = np.array([[0,1,0],
                      [0,0,1],
                      [1,0,0],
                      [1,1,0],
                      [1,1,1],
                      [0,1,1],
                      [0,1,0]])#Dependent variable
labels = np.array([[1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1]])
labels = labels.reshape(7,1) #to convert labels to vector
np.random.seed(5)

weights = np.random.rand(3,1)
bias = np.random.rand(1)
lr = 0.05 #learning rate
def sigmoid(x):
    return 1/(1+np.exp(-x))
def sigmoid_derivative(x):
    return sigmoid(x)*(1-sigmoid(x))
    for epoch in range(25000):
      inputs = input_set
      XW = np.dot(inputs, weights)+ bias
      z = sigmoid(XW)
      error = z - labels
    print(error.sum())
    dcost = error
    dpred = sigmoid_derivative(z)
    z_del = dcost * dpred
    inputs = input_set.T
    weights = weights - lr*np.dot(inputs, z_del)
    
    for num in z_del:
        bias = bias - lr*num
inputs = input_set
XW = np.dot(inputs, weights)+ bias
z = sigmoid(XW)
error = z - labels
print(error.sum())
error = z - labels
print(error.sum())
dcost = error
dpred = sigmoid_derivative(z)
z_del = dcost * dpred
inputs = input_set.T
weights = weights-lr*np.dot(inputs, z_del)
for num in z_del:
        bias = bias - lr*num
single_pt = np.array([1,0,0])
result = sigmoid(np.dot(single_pt, weights) + bias)
print(result)
