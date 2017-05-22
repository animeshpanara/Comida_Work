import xlrd
import xlwt
import re
import numpy as np
book1 = xlrd.open_workbook("Menu and Food Attributes (1).xlsx") #open our xls file, there's lots of extra default options in this call, for logging etc. take a look at the docs
book = xlrd.open_workbook("Menu card Details - DB.xlsx") 
sheet = book.sheets()[0] #book.sheets() returns a list of sheet objects... alternatively...
#sheet = book.sheet_by_name("qqqq") #we can pull by name
sheet = book.sheet_by_index(0) #or by the index it has in excel's sheet collection

items = sheet.col_values(4) #returns all the VALUES of row 4,
description=sheet.col_values(5)

desc=[]
for i in range(0,len(description)) :
    desc.append(description[i].lower().split())
data = [] #make a data store
for i in range(1,sheet.nrows):
  data.append(sheet.row_values(i)) 
#print (desc)
my_list= items
keys=['pork','chicken','egg','fish','brocoli','garlic','potato','onion','yogurt','paneer','chees.']
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
z,x,y=catogerizer(items[1:1000],description[1:1000],keys)
def printer(lis,key,y):
    for i in range(0,len(lis)):
        print(str(lis[i])+','+str(y[i]))
        print('\n')
    return;
def printingfunc(lis,key,y):
    z=[]
    for i in range(0,len(lis)):
        z.append([])
        '''for j in range(0,3):
            z[i].append(0)
        '''
    for i in range(0,len(lis)):
        string=''
        '''for j in range(0,len(y[i])):
            if y[i][j]==1:
                string+=(str(keys[j])+',')
                if j>=0 and j<=3:
                    z[i][0]=1
                    continue
                if j>=4 and j<=7:
                    z[i][1]=2
                    continue
                if j>=8 and j<=10:
                    z[i][2]=3
                    continue
        
        '''
        j=0
        while j<len(y[i]):
            if y[i][j]==1:
                string+=(str(keys[j])+',')
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
        print(str(lis[i])+':'+string+str(z[i]))     
        print('\n')
    return lis,z;
X_train,Z_train=printingfunc(z,keys,y)
X_train=y
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.preprocessing import LabelBinarizer
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
#forest = RandomForestClassifier(n_estimators=10, random_state=1)
#multi_target_forest = MultiOutputClassifier(forest, n_jobs=-1)
X1=np.array(y)
Y1=np.array(Z_train)
print(X1.shape)
print(Y1)
#multi_target_forest.fit(X1,Y1)
#print(multi_target_forest.fit(X_train,Z_train).predict(X_train))
#classif = OneVsRestClassifier(estimator=SVC(random_state=0))
Y1 = MultiLabelBinarizer().fit_transform(Z_train)
classifier = Pipeline([
    ('clf', OneVsRestClassifier(LinearSVC()))])
classifier.fit(X_train, Y1)
print(Y1)
#Z_tain = LabelBinarizer().fit_transform(Z_train)
#classif.fit(X1,Y1).predict(X1)
