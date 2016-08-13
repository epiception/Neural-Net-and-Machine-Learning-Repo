<<<<<<< HEAD
import numpy as np
import math as math
import matplotlib.pyplot as plt
from sklearn import linear_model, datasets

# import some data to play with
iris = datasets.load_iris()
Y = iris.target[:100]
X = iris.data[:100, :2]  # we only take the first two features.
alpha=0.001
convergence_point=0.001
X1=[]
X2=[]
for i in range(0,len(Y)):
    if int(Y[i]) is 0:
        X1.append(map(float,X[i]))
    if int(Y[i]) is 1:
        X2.append(map(float,X[i]))


X1=np.array(X1)
X2=np.array(X2)
plt.scatter(X1[:,0],X1[:,1],color='red')
plt.scatter(X2[:,0],X2[:,1],color='blue')
plt.xlabel('Parameter 1')
plt.ylabel('Parameter 2')
plt.legend(['0', '1'])
plt.show()

def logistic_func(theta, x):
    return float(1) / (1 + math.e**(-x.dot(theta)))

def cost_func(theta,x,y):
    log_val=logistic_func(theta,x)
    gradient=y*np.log(log_val)+(1-Y)*np.log(1-log_val)
    #print(gradient)
    return np.mean(gradient)

def grad_desc(theta_values,X,y):
    X = (X - np.mean(X, axis=0)) / np.std(X, axis=0)
    cost = cost_func(theta_values, X, y)
    print(cost)
    new_cost=1
    change_in_cost=1
    i=1
    while(change_in_cost>convergence_point):
        theta_values=theta_values+(alpha*(y-logistic_func(theta_values,X))).T.dot(X)
        new_cost=cost_func(theta_values,X,y)
        print(new_cost)
        #cost_iter.append([i,new_cost])
        change_in_cost=new_cost-cost
        cost=new_cost
        i+=1
    return theta_values

shape = X.shape[1]
#y_flip = np.logical_not(Y) #flip Setosa to be 1 and Versicolor to zero to be consistent
betas = np.zeros(shape)
fitted_values= grad_desc(betas, X, Y)
print(fitted_values)
#X = (X - np.mean(X, axis=0)) / np.std(X, axis=0)
prediction=logistic_func(fitted_values,X)
prediction=map(float,prediction)
prediction=np.around(prediction)
print(prediction)
print(X)
plt.scatter(X[:,0],X[:,1],color='red')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.legend(['0', '1'])
x_line=np.linspace(2,7,50)
intercept=-(fitted_values[1]/fitted_values[0])*np.mean(X2)-np.mean(X1)
y_line=-(fitted_values[1]/fitted_values[0])*x_line+intercept
plt.plot(x_line,y_line,'--')
plt.show()
=======
import numpy as np
import math as math
import matplotlib.pyplot as plt
from sklearn import linear_model, datasets

# import some data to play with
iris = datasets.load_iris()
Y = iris.target[:100]
X = iris.data[:100, :2]  # we only take the first two features.
alpha=0.001
convergence_point=0.001
X1=[]
X2=[]
for i in range(0,len(Y)):
    if int(Y[i]) is 0:
        X1.append(map(float,X[i]))
    if int(Y[i]) is 1:
        X2.append(map(float,X[i]))


X1=np.array(X1)
X2=np.array(X2)
plt.scatter(X1[:,0],X1[:,1],color='red')
plt.scatter(X2[:,0],X2[:,1],color='blue')
plt.xlabel('Flower 1')
plt.ylabel('Flower 2')
plt.legend(['0', '1'])
plt.show()

def logistic_func(theta, x):
    return float(1) / (1 + math.e**(-x.dot(theta)))

def cost_func(theta,x,y):
    log_val=logistic_func(theta,x)
    gradient=y*np.log(log_val)+(1-Y)*np.log(1-log_val)
    #print(gradient)
    return np.mean(gradient)

def grad_desc(theta_values,X,y):
    X = (X - np.mean(X, axis=0)) / np.std(X, axis=0)
    cost = cost_func(theta_values, X, y)
    print(cost)
    new_cost=1
    change_in_cost=1
    i=1
    while(change_in_cost>convergence_point):
        theta_values=theta_values+(alpha*(y-logistic_func(theta_values,X))).T.dot(X)
        new_cost=cost_func(theta_values,X,y)
        print(new_cost)
        #cost_iter.append([i,new_cost])
        change_in_cost=new_cost-cost
        cost=new_cost
        i+=1
    return theta_values

shape = X.shape[1]
#y_flip = np.logical_not(Y) #flip Setosa to be 1 and Versicolor to zero to be consistent
betas = np.zeros(shape)
fitted_values= grad_desc(betas, X, Y)
print(fitted_values)
X = (X - np.mean(X, axis=0)) / np.std(X, axis=0)
prediction=logistic_func(fitted_values,X)
prediction=map(float,prediction)
prediction=np.around(prediction)
>>>>>>> e54204041256e2a1d2e6044a129cd8b7d5f894ae
