import re
import xlrd
from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import LabelBinarizer
def stringFeatures(string,keys):
        string=string.lower().split()
        x=[]
        y=[]
        for i in range(0,len(keys)):
            y.append(0)    
        print(y)
        for i in range(0,len(keys)):
                for j in range(0,len(string)):
                        if re.match(keys[i].lower(),string[j]):
                                x.append(i)
                                break
        for i in range(0,len(x)):
                y[x[i]]=1
        return y;

keys=['pork','chicken','garlic','garlic','egg','chees.','yogurt','fish','tea','dosa','paneer']
x=processString("cheesy chicken rolls with egg and meat",keys)
print(x)

book1 = xlrd.open_workbook("Menu and Food Attributes (1).xlsx") #open our xls file, there's lots of extra default options in this call, for logging etc. take a look at the docs
book = xlrd.open_workbook("Menu card Details - DB.xlsx") 
sheet = book.sheets()[0] #book.sheets() returns a list of sheet objects... alternatively...
#sheet = book.sheet_by_name("qqqq") #we can pull by name
sheet = book.sheet_by_index(0) #or by the index it has in excel's sheet collection

items = sheet.col_values(4) #returns all the VALUES of row 4,
description=sheet.col_values(5)
