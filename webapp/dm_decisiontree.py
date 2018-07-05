import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
 

def importdata():
    balance_data = pd.read_csv('C:/DM/ipl/webapp/test.csv')
    print ("lenght: ", len(balance_data))
    balance_data = balance_data.dropna() 
    return balance_data
 

def splitdataset(balance_data):
 
    names = balance_data.Name.unique()
    print(names)
    a = balance_data.Name.astype(pd.api.types.CategoricalDtype(categories=names)).cat.codes
    balance = balance_data.drop(['Name'],axis=1)
    balance['nvalues']=a
    X = balance.values[:,1:]
    Y = balance.values[:,0]
 
    
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.3, random_state = 100)
     
    return X, Y, X_train, X_test, y_train, y_test
     

def train_using_gini(X_train, y_train):
 
    clf_gini = DecisionTreeClassifier(criterion = "gini")
    clf_gini.fit(X_train, y_train)
    return clf_gini
     

def tarin_using_entropy(X_train, y_train):
 
    clf_entropy = DecisionTreeClassifier(criterion = "entropy")
    clf_entropy.fit(X_train, y_train)
    return clf_entropy
 
 
def prediction(X_test, clf_object):
 
    y_pred = clf_object.predict(X_test)
    # print("Predicted values:")
    # print(y_pred)
    return y_pred
     
def cal_accuracy(y_test, y_pred):
          
    print ("Accuracy : ",accuracy_score(y_test,y_pred)*100)
     
    
def Dmmain(context):
     
    
    data = importdata()
    X, Y, X_train, X_test, y_train, y_test = splitdataset(data)
    clf_gini = train_using_gini(X_train, y_train)
    # clf_entropy = tarin_using_entropy(X_train, y_train)
    
    test = [[context['over'],context['ball'],context['strike'],context['name']]];
    # print(test)
    # print("Results Using Gini Index:")
     
    #  #Prediction using gini
    y_pred_gini = prediction(test,clf_gini)
    # print(y_pred_gini)
    return y_pred_gini

    # for i in y_pred_gini:
    #     print(i)

    # cal_accuracy(y_test, y_pred_gini)
     
    # print("Results Using Entropy:")
    # # Prediction using entropy
    # y_pred_entropy = prediction(X_test, clf_entropy)
    # cal_accuracy(y_test, y_pred_entropy)
     
    
