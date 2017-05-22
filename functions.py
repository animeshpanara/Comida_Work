import re
def stringFeatures(string,keys):
        strings=string.lower().split()
        x=[]
        y=[]
        for i in range(0,len(keys)):
            y.append(0)    
        
        for i in range(0,len(keys)):
                for j in range(0,len(strings)):
                        if re.match(keys[i].lower(),strings[j]):
                                x.append(i)
                                break
        for i in range(0,len(x)):
                y[x[i]]=1
        print(y)
        return string,y;
def featureExtraction(arrayofstrings,keys):
	y=[]
	for i in range(0,len(arrayofstrings)):
		y.append([])
		arrayofstrings[i],y[i]=stringFeatures(arrayofstrings[i],keys)
	return y;
def finalcatogery(featurevector):
        z=[]
        y=featurevector
        for i in range(0,len(featurevector)):
                z.append([])
        for i in range(0,len(featurevector)) :
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
        return z;
	
