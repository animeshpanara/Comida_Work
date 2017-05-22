import xlrd
import xlwt
import re
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
keys=['pork','chicken','garlic','potato','onion','egg','chees.','yogurt','fish','tea','dosa','paneer']

def category(data,desc,keys):
    x=[]
    y=[]
    for i in range(0,len(data)):
        y.append([])
        for j in range(0,len(keys)):
            y[i].append(0) 
    for i in range(0,len(keys)+1):
        x.append([])
    
    for i in range(0,len(data)):
        temp=data[i].lower().split()
        flag=0
        for j in range(0,len(keys)):
                flag1=0
                for k in range(0,len(temp)):
                    if re.match(keys[j].lower(),temp[k]):
                            x[j].append(data[i])
                            y[i][j]=1
                            flag,flag1=1,1
                            break
                if flag1==0:
                    for k in range(0,len(desc[i])):
                        if re.match(keys[j].lower(),desc[i][k]):
                                x[j].append(data[i])
                                y[i][j]=1
                                flag=1
                                break
                
        if flag==0 :
            x[len(keys)].append(data[i])             
    return x,y;
x,y=category(my_list[1:10],desc[1:10],keys)
print (str(len(desc))+','+str(len(keys))+','+str(len(x)))

def printer(lis,key,y):
    for j in range(0,len(key)+1):
        try:
            print(key[j])
        except:
            print ('extraa')
        for i in range(0,len(lis[j])):
            print(str(x[j][i])+','+str(y[i]))
        print('\n')
    return
                  
printer(x,keys,y)
