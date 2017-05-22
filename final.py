import xlrd
import xlwt
import re
import functions as fn
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
data=[]
for i in range(0,len(items)):
    data.append([])
    data[i]=str(items[i])+' '+str(description[i])
keys=['pork','chicken','egg','fish','brocoli','garlic','potato','onion','yogurt','paneer','chees.']

X_train=np.core.defchararray.add(items[1:],description[1:])
Y_train=fn.featureExtraction(X_train[0:1000],keys)
Z_train=fn.finalcatogery(Y_train)
'''
mlb = MultiLabelBinarizer()
Y = mlb.fit_transform()
X1=np.array(X_train)
Y1=np.array(Z)
Y1= mlb.fit_transform(Y1)
classif = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', OneVsRestClassifier(LinearSVC()))])
classif.fit(X_train[1:1000],Y1)
'''
