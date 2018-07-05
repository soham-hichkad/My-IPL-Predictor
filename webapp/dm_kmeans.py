import xlrd
from sklearn.cluster import KMeans
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt


def Kmain(context):

    file_location = "C:/DM/ipl/webapp/data1.xlsx"
    workbook = xlrd.open_workbook(file_location)
    sheet = workbook.sheet_by_name('B1')

    x = []
    for value in sheet.col_values(3):
        value = int(value)
        val = ((value-300)/(14000-300))*(100-0)+0
        x.append(val)


    y = []
    for value in sheet.col_values(7):
        value = int(value)
        val = ((value-100)/(600-100))*(100-0)+0
        y.append(val)

    X = np.array(list(zip(x, y))).reshape(len(y), 2)
    # KMeans algorithm 
    K = 12
    kmeans_model = KMeans(n_clusters=K).fit(X)
     
    label = 0

    player_name = context['player']

    for row in range(sheet.nrows):
        for column in range(sheet.ncols):
            if sheet.cell(row, column).value == player_name:  
                reqrow = row
                label = kmeans_model.labels_[row]

    pl_run= sheet.cell(reqrow,3)   
    pl_avg = sheet.cell(reqrow,7)

    # print('Your players stats:')

    # print(pl_avg,pl_run)    
            
    # print('You should also see these players:')


    main_list = []
    for i, l in enumerate(kmeans_model.labels_):
        if kmeans_model.labels_[i] == label:
            v1 = str(sheet.cell(i,0))
            v2 = str(sheet.cell(i,3))
            v3 = str(sheet.cell(i,7))
            main_list.append([v1.replace('text:','').replace("'",''),v2.replace('text:','').replace("'",''),v3.replace('text:','').replace("'",'')])


    # print(main_list)
    return main_list
        
               
