'''
Created on Oct 29, 2016

@author: bhaumikpatel
'''
import sys
import random
import math

def dotProduct(w, x):
    dp = 0.0
    for wi, xi in zip(w, x):
        # print ("wi->"+str(wi))
        # print ("xi->"+str(xi))
        dp += wi * xi
    return dp
    
    
# find best eta by experiments
eta = 0.01
# eta = 0.0001
# eta = 0.000000001

dataFile = sys.argv[1]
tngLblFile = sys.argv[2]

# Read data file
dataSets = []
with open(dataFile) as f:
    for row in f:
        rowArray = list(map(float, row.split()))
        rowArray.append(1.0)
        dataSets.append(rowArray)
f.close()
noCols = len(dataSets[0])  # noCols = no of class attributes
noRows = len(dataSets)  # noRows = no of training data sets
        
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

# print data
print (dataSets)
print (tngLabels)
# repeat for each column
for i in range(0, noCols, 1):
    for j in range(0, noRows - 1, 1):
        print ('column :' + str(i) + ' row :' + str(j) + ' : ' + str(dataSets[j][i]) 
               + ' training label : ' + str(tngLabels.get(j)))
        currentRow = j
        lSize = 0
        lp = 0
        rSize = 0
        rp = 0
                
        #check in previous direction
        for j1 in range(j, -1, -1):
            lSize+=1
            if(tngLabels.get(j1) == -1):
                lp+=1
        
        #check in next direction
        for j2 in range(j+1, noRows, 1):
            rSize+=1
            if(tngLabels.get(j2) == -1):
                rp+=1
                
        #calculate gini
        gini = (lSize/noRows)*(lp/lSize)*(1 - lp/lSize) + (rSize/noRows)*(rp/rSize)*(1 - rp/rSize)
        print ('gini : ' + str(gini))  
        
        if(gini < minGini):
            minGini = gini
            print ('minGini : ' + str(minGini))
            k = i
            s = (dataSets[j][i] + dataSets[j+1][i])/2.0      
            
print ('minGini : ' + str(minGini))   
print ('k : ' + str(k)) 
print ('s : ' + str(s))    
            
            
        
    



  

            
