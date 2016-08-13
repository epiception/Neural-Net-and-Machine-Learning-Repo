<<<<<<< HEAD
<<<<<<< HEAD
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

iris=np.loadtxt('C:\Users\USER\Desktop\iris1.csv', delimiter=',')
alpha=0.9 #learning rate=0.9
data=iris[:, :4]
y=iris[:,4]
z = np.empty(150, dtype=object)
temp = np.empty(3, dtype=object)
d = np.empty(3, dtype=object)
category=["","virginica","versicolor","setosa"]
for i in range(0,150):
    x=int(y[i])
    z[i]=category[x]

weights=np.array([6,3,6])
weights=np.array([weights,weights,weights])
ax.scatter(weights[:,0],weights[:,1],weights[:,2],c='purple', marker='^')
ax.scatter(data[:,0],data[:,1],data[:,2],c='r', marker='o')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
weights=np.array([6.0,3.0,6.0])
weights=np.array([weights,weights,weights])
ax = fig.add_subplot(122, projection='3d')
#number of epochs=1000
#using 3 attributes of data to show weight migration and classification in 3d space
for s in range(1,1000):
    for i in range(0,150):
            for j in range(0,3):
                temp=np.square(data[i,:3]-weights[j,:]); #calculating the Euclidian Distance
                d[j]=np.sum(temp)
        #finding minimum distance and its respective index value
            val=np.min(d)
            from operator import itemgetter
            column=min(enumerate(d), key=itemgetter(1))[0]
            weights[column,:]=weights[column,:]+(alpha*(data[i,:3]-weights[column,:])) #weight updation
    alpha=alpha*0.75; 
print('Current Weights')
print(weights)
ax.scatter(weights[:,0],weights[:,1],weights[:,2],c='blue', marker='^', s=50)
ax.scatter(data[:,0],data[:,1],data[:,2],c='r', marker='o')
ax.set_xlabel('Weight Migrated X Label')
ax.set_ylabel('Weight Migrated Y Label')
ax.set_zlabel('Weight Migrated Z Label')
plt.show()
#shows the co-ordinates of weights with respect to previous data and the migration of weights to the data centers in the 3d space
=======
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

iris=np.loadtxt('C:\Users\USER\Desktop\iris1.csv', delimiter=',')
alpha=0.9 #learning rate=0.9
data=iris[:, :4]
y=iris[:,4]
z = np.empty(150, dtype=object)
temp = np.empty(3, dtype=object)
d = np.empty(3, dtype=object)
category=["","virginica","versicolor","setosa"]
for i in range(0,150):
    x=int(y[i])
    z[i]=category[x]

weights=np.array([6,3,6])
weights=np.array([weights,weights,weights])
ax.scatter(weights[:,0],weights[:,1],weights[:,2],c='purple', marker='^')
ax.scatter(data[:,0],data[:,1],data[:,2],c='r', marker='o')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
weights=np.array([6.0,3.0,6.0])
weights=np.array([weights,weights,weights])
ax = fig.add_subplot(122, projection='3d')
#number of epochs=1000
#using 3 attributes of data to show weight migration and classification in 3d space
for s in range(1,1000):
    for i in range(0,150):
            for j in range(0,3):
                temp=np.square(data[i,:3]-weights[j,:]); #calculating the Euclidian Distance
                d[j]=np.sum(temp)
        #finding minimum distance and its respective index value
            val=np.min(d)
            from operator import itemgetter
            column=min(enumerate(d), key=itemgetter(1))[0]
            weights[column,:]=weights[column,:]+(alpha*(data[i,:3]-weights[column,:])) #weight updation
    alpha=alpha*0.75; 
print('Current Weights')
print(weights)
ax.scatter(weights[:,0],weights[:,1],weights[:,2],c='blue', marker='^', s=50)
ax.scatter(data[:,0],data[:,1],data[:,2],c='r', marker='o')
ax.set_xlabel('Weight Migrated X Label')
ax.set_ylabel('Weight Migrated Y Label')
ax.set_zlabel('Weight Migrated Z Label')
plt.show()
#shows the co-ordinates of weights with respect to previous data and the migration of weights to the data centers in the 3d space
>>>>>>> origin/master
=======
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

iris=np.loadtxt('C:\Users\USER\Desktop\iris1.csv', delimiter=',')
alpha=0.9 #learning rate=0.9
data=iris[:, :4]
y=iris[:,4]
z = np.empty(150, dtype=object)
temp = np.empty(3, dtype=object)
d = np.empty(3, dtype=object)
category=["","virginica","versicolor","setosa"]
for i in range(0,150):
    x=int(y[i])
    z[i]=category[x]

weights=np.array([6,3,6])
weights=np.array([weights,weights,weights])
ax.scatter(weights[:,0],weights[:,1],weights[:,2],c='purple', marker='^')
ax.scatter(data[:,0],data[:,1],data[:,2],c='r', marker='o')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
weights=np.array([6.0,3.0,6.0])
weights=np.array([weights,weights,weights])
ax = fig.add_subplot(122, projection='3d')
#number of epochs=1000
#using 3 attributes of data to show weight migration and classification in 3d space
for s in range(1,1000):
    for i in range(0,150):
            for j in range(0,3):
                temp=np.square(data[i,:3]-weights[j,:]); #calculating the Euclidian Distance
                d[j]=np.sum(temp)
        #finding minimum distance and its respective index value
            val=np.min(d)
            from operator import itemgetter
            column=min(enumerate(d), key=itemgetter(1))[0]
            weights[column,:]=weights[column,:]+(alpha*(data[i,:3]-weights[column,:])) #weight updation
    alpha=alpha*0.75; 
print('Current Weights')
print(weights)
ax.scatter(weights[:,0],weights[:,1],weights[:,2],c='blue', marker='^', s=50)
ax.scatter(data[:,0],data[:,1],data[:,2],c='r', marker='o')
ax.set_xlabel('Weight Migrated X Label')
ax.set_ylabel('Weight Migrated Y Label')
ax.set_zlabel('Weight Migrated Z Label')
plt.show()
#shows the co-ordinates of weights with respect to previous data and the migration of weights to the data centers in the 3d space
>>>>>>> origin/master
