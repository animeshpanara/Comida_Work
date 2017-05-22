import xlrd
book = xlrd.open_workbook("Menu card Details - DB.xlsx") #open our xls file, there's lots of extra default options in this call, for logging etc. take a look at the docs
 
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
keys=['pork','chicken','egg','cheese','yogurt','fish','tea','dosa','paneer']
def category(data,desc,keys):
    x=[]
    for i in range(0,len(keys)+1):
        x.append([])
        x[i].append('') 
    for i in range(0,len(data)):
        temp=data[i].lower().split()
        flag=0
        for j in range(0,len(keys)):
                   if (keys[j].lower() in (desc[i] or temp)) :
                        x[j].append(data[i])
                        flag=1
        if flag==0 :
            x[len(keys)].append(data[i])             
    return x;
x=category(my_list,desc,keys)
print (str(len(desc))+','+str(len(keys))+','+str(len(x)))

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
