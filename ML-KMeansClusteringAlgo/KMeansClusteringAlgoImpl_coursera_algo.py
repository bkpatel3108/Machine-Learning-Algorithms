'''
Created on Nov 15, 2016

@author: bhaumikpatel
'''
import sys

dataFile = sys.argv[1]
k = int(sys.argv[2])
dataSet = []

# Reading dataSet from dataSet file
with open(dataFile) as f:
    for row in f:
        dataPoint = list(map(float, row.split()))
        dataSet.append(dataPoint)
f.close()    
noCols = len(dataSet[0])    
noRows = len(dataSet)  

#initialize dictionary to store labels
labelDic = {}

# initialize k means
# initialized k in reverse order so it can make same exact clusters as our test datasets
kmeans = []
for i in range(0, k, 1):
    kmeans.append(list(map(float,dataSet[i])))

print ('initial kmeans' + str(kmeans)) 
prevKmeans = []
for i in range(0, k, 1):
    prevKmeans.append([float('Infinity')] * noCols)
    
kmeanDiff = 1.0

#repeat this process till it converge
#for loop for testing
while(kmeanDiff > 0.00):

    #for each point in dataset
    for i, dataPoint in enumerate(dataSet):
        dataLbl = 0
        curMinDst = float('Infinity');
        #for each kmeans point
        for j in range(0, k, 1):
            kmean = kmeans[j]
            curDst = 0.0
            for l, attr in enumerate(dataPoint):
                curDst = curDst + ((attr - kmean[l])**2)
            if(curDst < curMinDst):
                dataLbl = j
                curMinDst = curDst
        labelDic[i] = dataLbl
        
    #recompute mean based on assigned labels
    # initialize k sums
    sums = []
    lblCntArr = [0] * k
    for i in range(0, k, 1):
        sums.append([0.0] * noCols)
        
    for i, dataPoint in enumerate(dataSet):
        dataLbl = labelDic.get(i)
        attrSum = sums[dataLbl]
        lblCntArr[dataLbl] += 1
        for j, attr in enumerate(dataPoint):
            attrSum[j] = attrSum[j] + attr
    
    for i in range(0, k, 1):
        attrSum = sums[i]
        kmean = kmeans[i]
        for j, attr in enumerate(attrSum):
            if(lblCntArr[i] > 0):
                kmean[j] = attr / lblCntArr[i]  
            
    #difference in previous kmean and new kmean
    kmeanDiff = 0.0
    for i in range(0, k, 1):
        for j  in range(0, noCols, 1):
            kmeanDiff += abs(kmeans[i][j] - prevKmeans[i][j])
    
    print ('kmeanDiff : ' + str(kmeanDiff))    
    for i in range(0, k, 1):
        for j  in range(0, noCols, 1):
            prevKmeans[i][j] = kmeans[i][j]

print ('--------')
print ('Clusters')
print ('--------')
for key, value in labelDic.items() :
    print (value, key)
    
with open('predlabels.txt', 'w') as f:
    for key, value in labelDic.items() :
        f.write(str(value) + " " + str(key) + '\n')
f.close()   