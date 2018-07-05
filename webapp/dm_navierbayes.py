import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report



def importdata():
    balance_data = pd.read_csv('C:/DM/ipl/webapp/test2.csv')
    print ("lenght: ", len(balance_data))
    balance_data = balance_data.dropna() 
    return balance_data
 

def splitdataset(balance_data):
   
 
    name5 = balance_data.match_winner.unique()
    e = balance_data.match_winner.astype(pd.api.types.CategoricalDtype(categories=name5)).cat.codes
    balance_data['match_winner_1']=pd.Series(e,index=balance_data.index)

    name = balance_data.Team1.unique()
    # print(name)
    a = balance_data.Team1.astype(pd.api.types.CategoricalDtype(categories=name)).cat.codes
    balance_data['Team_1']=pd.Series(a,index=balance_data.index)

    name2 = balance_data.Team2.unique()
    b = balance_data.Team2.astype(pd.api.types.CategoricalDtype(categories=name2)).cat.codes
    balance_data['Team_2']=pd.Series(b,index=balance_data.index)
    
    name3 = balance_data.Venue_Name.unique()
    print(name3)
    c = balance_data.Venue_Name.astype(pd.api.types.CategoricalDtype(categories=name3)).cat.codes
    balance_data['Venue_Name_1']=pd.Series(c,index=balance_data.index)

    # name4 = balance_data.Toss_Winner.unique()
    # d = balance_data.Toss_Winner.astype(pd.api.types.CategoricalDtype(categories=name4)).cat.codes
    # balance_data['Toss_Winner_1']=pd.Series(d,index=balance_data.index)

    # print(balance_data)
    X = balance_data.values[:,6:]
    Y = balance_data.values[:,5]
    # print(type(X))
    # X = X.astype('int')
    # Y = Y.astype('int')
    
    X_train, X_test, y_train, y_test = train_test_split(X, Y,test_size = 0.3,random_state = 100)
    # print(type(X_train)) 
    return X, Y, X_train, X_test, y_train, y_test
     

def train_using_nb(X_train, y_train):
    print(">>>>>>>>>>>>>>>>>>>>>insid nb")
    clf_nb = GaussianNB(priors=None)
    # print(X_train)
    # print(y_train)
    X_train = X_train.astype('int')
    y_train = y_train.astype('int')
    clf_nb.fit(X_train,y_train)
    # print("<<<return to main")
    return clf_nb
    
def prediction(X_test, clf_object):
    y_pred = clf_object.predict(X_test)
    return y_pred
     
def cal_accuracy(y_test, y_pred):
          
     print ("Accuracy : ",accuracy_score(y_test,y_pred)*100)
     
    
def Nbmain(context):
    
    data = importdata()
    
    X, Y, X_train, X_test, y_train, y_test = splitdataset(data)
    # print(X_train)
    # print(y_train)
    # print(type(X_train))
    # print(X)
    # print(type(X))

    clf_nb = train_using_nb(X_train, y_train)
    
    team = ['Royal Challengers Bangalore','Kings XI Punjab','Delhi Daredevils','Mumbai Indians','Kolkata Knight Riders','Rajasthan Royals','Deccan Chargers','Chennai Super Kings','Kochi Tuskers Kerala','Pune Warriors' ,'Sunrisers Hyderabad','Gujarat Lions','Rising Pune Supergiants']
    


    test = [[int(context['team1']),int(context['team2']),int(context['venue'])]];
    # print(test)
    # print("Results Using Gini Index:")
    y_pred_nb = prediction(test,clf_nb)

    y_unique=team[y_pred_nb[0]]


    # for i in range(len(X_test)):
    #     print(X_test[i])
    #     print(y_pred_nb[i])
    # print(X_test)
    # print(y_pred_nb)
    
    return y_unique
     
    
