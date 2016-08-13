<<<<<<< HEAD
import numpy as np
import math
from sklearn.preprocessing import PolynomialFeatures
#Mention path of txt dataset file  
grid=np.loadtxt('E:\Ganesh\NNML project\Neural-Net-and-Machine-Learning-Repo\Neural Network and Machine Learning Repo\Regression-Multivariate Linear and Polynomial\Regression data.txt', delimiter=' ')
#first 2 columns consist of feature varaibles

#last column signifies office price dependant on the feature variables

#you could increase the number of features by adding data till the second last column

parameter_row=len(grid)
parameter_column=len(grid[0])-1
X=np.zeros((parameter_row,parameter_column))
Y=np.zeros(parameter_row)
#using normal equation for solution
for i in range(0,parameter_row):
    for j in range(0,parameter_column):
        X[i][j]=grid[i][j]
        Y[i]=grid[i][j+1]

#Using PolynomialFeatures from scikit-learn to generate polynomials based on given degree
#for polynomial regression, change degree to value>1        

poly=PolynomialFeatures(degree=1)
X=poly.fit_transform(X,Y)

#Normal Equation matrix:
XTX= X.T.dot(X)
beta= np.linalg.inv(XTX).dot(X.T).dot(Y)
print("weighted (beta) values of equation are")
print(beta)

=======
import numpy as np
import math
from sklearn.preprocessing import PolynomialFeatures
#Mention path of txt dataset file  
grid=np.loadtxt('E:\Ganesh\NNML project\Neural-Net-and-Machine-Learning-Repo\Neural Network and Machine Learning Repo\Regression-Multivariate Linear and Polynomial\Regression data.txt', delimiter=' ')
#first 2 columns consist of feature varaibles

#last column signifies office price dependant on the feature variables

#you could increase the number of features by adding data till the second last column

parameter_row=len(grid)
parameter_column=len(grid[0])-1
X=np.zeros((parameter_row,parameter_column))
Y=np.zeros(parameter_row)
#using normal equation for solution
for i in range(0,parameter_row):
    for j in range(0,parameter_column):
        X[i][j]=grid[i][j]
        Y[i]=grid[i][j+1]

#Using PolynomialFeatures from scikit-learn to generate polynomials based on given degree
#for polynomial regression, change degree to value>1        

poly=PolynomialFeatures(degree=1)
X=poly.fit_transform(X,Y)

#Normal Equation matrix:
XTX= X.T.dot(X)
beta= np.linalg.inv(XTX).dot(X.T).dot(Y)
print("weighted (beta) values of equation are")
print(beta)

>>>>>>> e54204041256e2a1d2e6044a129cd8b7d5f894ae
