import xlrd
import re
book = xlrd.open_workbook("Menu card Details - DB.xlsx") #open our xls file, there's lots of extra default options in this call, for logging etc. take a look at the docs
 
sheet = book.sheets()[0] #book.sheets() returns a list of sheet objects... alternatively...
#sheet = book.sheet_by_name("qqqq") #we can pull by name
sheet = book.sheet_by_index(0) #or by the index it has in excel's sheet collection
 
items = sheet.col_values(4) #returns all the VALUES of row 4,
description=sheet.col_values(5)
keys=['pork','chicken','egg','cheese','yogurt','fish','tea','dosa','paneer']
def category(data,desc,keys):
    x=[]
    for i in range(0,len(keys)+1):
        x.append([])
        x[i].append('')
    for i in range(0,len(data)):
        flag=0
        for j in range(0,len(keys)):
                    if re.search('\b'+keys[j].lower()+'.',data[i].lower()) or re.search(keys[j].lower()+'.',desc[i].lower()) :
                        x[j].append(data[i])
                        flag=1
        if flag==0 :
            x[len(keys)].append(data[i])             
    return x;
x=category(items,description,keys)
def printer(lis,key):
    for j in range(0,len(key)+1):
        try:
            print(key[j])
        except:
            print ('extraa')
        for i in range(0,len(lis[j])):
            print(str(x[j][i])+'\t')
        print('\n')
    return
                  
printer(x,keys)
