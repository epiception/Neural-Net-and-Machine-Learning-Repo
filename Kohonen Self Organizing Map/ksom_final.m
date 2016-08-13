%Kohonen Self Organizing Maps using Original Algorithm on IRIS Dataset
%This is a case of no limitting function. so h(i)=1 in this case
%no. of epochs=1000 
%learning rate=0.9
clc;
clear all;
X=iris_dataset;
X=X'; 
W=[6 3 6 0;6 3 6 0;6 3 6 0]; %non-random offset weights, 
%primarily based on seperation of weights and data range
versicolor=0;virginica=0;setosa=0;
category=char('versicolor','virginica','setosa');
alpha=0.9;
disp('Initial Weights:')
disp(W);
d=zeros(1,3);column=0;
disp('Training Begins:')
for s=1:1000
    for i=1:150
        for j=1:3
                temp=(X(i,:)-W(j,:)).^2; %Calculating Square of Euclidian Distance
                d(j)=sum(temp);
        end
        [val,column]=min(d);%finding minimum distance and its respective index value
         W(column,:)=W(column,:)+alpha*(X(i,:)-W(column,:)); %Weight Updation
    end
    %end
    alpha=alpha*0.75; %Slow alpha reduction
    %to check weight updation at each epoch uncomment *here*
    %disp('Current Weights')
    %disp(W)
end
disp('New Weights are:')
disp(W);
disp('New Classification:')
for i=1:150
    for j=1:3
            temp=(X(i,:)-W(j,:)).^2; %Calculating Square of Euclidian Distance
            d(j)=sum(temp);
    end
    [val,column]=min(d);%finding minimum distance and its respective index value
    disp('flower segregated into category');
    disp(category(column,:));
    if column==1
        versicolor=versicolor+1;
    elseif column==2
        virginica=virginica+1;
    else
        setosa=setosa+1;
    end 
end

disp('')
disp('Testing: Test with current weights using your own values to check classification')
flower_parameters(1)=input('Enter sepal length (cm):');
flower_parameters(2)=input('Enter sepal width (cm):');
flower_parameters(3)=input('Enter petal length (cm):');
flower_parameters(4)=input('Enter petal width (cm):');
flower_parameters=flower_parameters';
temp=zeros(1,4);
    for j=1:3
            temp=((flower_parameters(:)')-W(j,:)).^2;
            d(j)=sum(temp);
    end
    [val,column]=min(d);%finding minimum distance and its respective index value
    disp('Individual Euclidian Distances');
    disp(d);
    disp('Therefore based on this, the flower of given parameters can be segregated into category');
    disp(category(column,:));