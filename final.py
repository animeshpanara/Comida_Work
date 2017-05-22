import xlrd
import xlwt
import re
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import MultiLabelBinarizer

book1 = xlrd.open_workbook("Menu and Food Attributes (1).xlsx") #open our xls file, there's lots of extra default options in this call, for logging etc. take a look at the docs
book = xlrd.open_workbook("Menu card Details - DB.xlsx") 
sheet = book.sheets()[0] #book.sheets() returns a list of sheet objects... alternatively...
#sheet = book.sheet_by_name("qqqq") #we can pull by name
sheet = book.sheet_by_index(0) #or by the index it has in excel's sheet collection
items = sheet.col_values(4) #returns all the VALUES of row 4,
description=sheet.col_values(5)
for i in range(0,len(items)):
    items[i]=str(items[i])+' '
X_train=np.core.defchararray.add(items,description)
mlb = MultiLabelBinarizer()
#Y = mlb.fit_transform(y_train_text)
def catogerizer(data,desc,keys):
    x=[]
    y=[]
    item=[]
    for i in range(0,len(data)):
        y.append([])
        item.append('')
        for j in range(0,len(keys)):
            y[i].append(0)
    for i in range(0,len(keys)+1):
        x.append([])
    for i in range(0,len(item)):
        item[i]=data[i]+' '+desc[i]
        items=item[i].lower().split()
        flag=0
        for j in range(0,len(keys)):
            for k in range(0,len(items)):
                if re.match(keys[j].lower(),items[k]):
                            x[j].append(item[i])
                            try:
                                y[i][j]=1
                            except:
                                print(str(i)+','+str(j)+'\n')
                            break
        if flag==0:
            x[len(keys)].append(item[i])
    return data,item,y

keys=['pork','chicken','egg','fish','brocoli','garlic','potato','onion','yogurt','paneer','chees.']
data,item,y=catogerizer(items[1:1000],description[1:1000],keys)
def printingfunc(lis,key,y):
    z=[]
    for i in range(0,len(lis)):
        z.append([])
        '''for j in range(0,3):
            z[i].append(0)
        '''
    for i in range(0,len(lis)):
        j=0
        while j<len(y[i]):
            if y[i][j]==1:
                if j>=0 and j<=3:
                    z[i].append('non-veg')
                    j=4
                    continue
                if j>=4 and j<=7:
                    z[i].append('veggies')
                    j=8
                    continue
                if j>=8 and j<=10:
                    z[i].append('milk product')
                    j=11
                    continue
            j=j+1
        if len(z[i])==0:
            z[i].append('extras')
    return lis,z;
X,Z=printingfunc(data,keys,y)
X1=np.array(X_train)
Y1=np.array(Z)
Y1= mlb.fit_transform(Y1)
classif = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', OneVsRestClassifier(LinearSVC()))])

classif.fit(X_train[1:1000],Y1)
