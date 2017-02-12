'''
Created on Nov 7, 2016

@author: bhaumikpatel
'''
import sys

dataFile = sys.argv[1]
tngLblFile = sys.argv[2]

# Read data file
dataSets = []
rowArray = None
with open(dataFile) as f:
    
    rowArray = [map(float,x.split()) for x in f]
    #store rows as columns and columns as rows for easy calculation
    for x in zip(*rowArray):
        dataSets.append(x)
        
f.close()
noCols = len(dataSets)  # noCols = no of class attributes
noRows = len(dataSets[0])  # noRows = no of training data sets
        
# Read label file
tngLabels = {}  # create map of tngLabels to retrieve them in O(1) time
with open(tngLblFile) as f:
    for row in f:
        rowArray = row.split()
        tngLabels[int(rowArray[1])] = int(rowArray[0])
        if(tngLabels[int(rowArray[1])] == 0):
            tngLabels[int(rowArray[1])] = -1 
f.close()

k = 0  # start with default value of k as zero
s = 0  # start with default value of s as zero
minGini = float('Infinity');
nextVal = float('Infinity');

# print data and labels
#print (dataSets)
#print (tngLabels)
print ('noOfCols : '+ str(noCols))
print ('noOfRows : '+ str(noRows))
# repeat for each column
for i, data in enumerate(dataSets):
    sortedIndexArr = sorted(range(len(data)),key=lambda x:data[x])
    data = sorted(data)
    #print ('sortedIndexArr : ' + str(sortedIndexArr))
    for j in range(0, noRows - 1, 1):
        #print ('column :' + str(i) + ' row :' + str(j) + ' : ' + str(data[j]) + ' training label : ' + str(tngLabels.get(j)))
        
        #check if next value and current value is not same then only you can make split
        nextVal = data[j+1] 
        if(data[j] != nextVal):
            #currentRow = j
            lSize = 0
            lp = 0
            rSize = 0
            rp = 0
                    
            #check in previous direction
            for j1 in range(j, -1, -1):
                lSize+=1
                if(tngLabels.get(sortedIndexArr[j1]) == -1):
                    lp+=1
            
            #check in next direction
            for j2 in range(j+1, noRows, 1):
                rSize+=1
                if(tngLabels.get(sortedIndexArr[j2]) == -1):
                    rp+=1
                    
            #calculate gini
            gini = (lSize/noRows)*(lp/lSize)*(1 - lp/lSize) + (rSize/noRows)*(rp/rSize)*(1 - rp/rSize)
            #print ('gini : ' + str(gini))  
            
            if(gini < minGini):
                minGini = gini
                #print ('minGini : ' + str(minGini))
                k = i
                s = (data[j] + data[j+1])/2.0   
            
print ('minGini : ' + str(minGini))   
print ('column - k : ' + str(k)) 
print ('best split - s : ' + str(s))    
