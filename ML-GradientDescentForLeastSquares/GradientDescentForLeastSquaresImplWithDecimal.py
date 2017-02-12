'''
Created on Oct 1, 2016

@author: bhaumikpatel
'''
import sys
import random
import decimal

def dotProduct(w,x):
    dp = decimal.Decimal(0.0)
    for wi, xi in zip(w, x):
        #print ("wi->"+str(wi))
        #print ("xi->"+str(xi))
        dp += wi * xi
    return dp
    
    
# find best eta by experiments
eta = decimal.Decimal(0.0001)

dataFile = sys.argv[1]
tngLblFile = sys.argv[2]

#Read data file
dataSets = []
with open(dataFile) as f:
    for row in f:
        rowArray = list(map(decimal.Decimal, row.split()))
        rowArray.append(decimal.Decimal(1))
        dataSets.append(rowArray)
f.close()
noCols = len(dataSets[0])   #noCols = no of class attributes
noRows = len(dataSets)  #noRows = no of training data sets
        
#Read label file
tngLabels = {} #create map of tngLabels to retrieve them in O(1) time
with open(tngLblFile) as f:
    for row in f:
        rowArray = row.split()
        tngLabels[int(rowArray[1])] = decimal.Decimal(rowArray[0])
        if(tngLabels[int(rowArray[1])] == 0):
            tngLabels[int(rowArray[1])] = -1 
f.close()

#initialize vector w
w = [decimal.Decimal(0)]*noCols

for i, attr in enumerate(w):
    w[i] = decimal.Decimal((0.02 * random.uniform(0, 1)) - 0.01)

print ("Initial w "+ str(w))
#Compute delta f
errorDef = decimal.Decimal(1);
error = decimal.Decimal(0)
preError = decimal.Decimal('Infinity');
#preError = None;
while(errorDef > 0.001):
    dellf = [decimal.Decimal(0.0)]*noCols
    for i, data in enumerate(dataSets):
        if(tngLabels.get(i) is not None):
            dp = dotProduct(w, data)
            #print ("dp->"+str(dp))
            for j, attr in enumerate(data):
                dellf[j] += ((decimal.Decimal(tngLabels.get(i)) - dp)*attr)
                
    #Update w
    for j in range(0,len(w)):
        w[j] = w[j] + (eta * dellf[j])
        
    #compute error
    error = decimal.Decimal(0)
    for i, data in enumerate(dataSets):
        if(tngLabels.get(i) is not None):
            error += ((decimal.Decimal(tngLabels.get(i)) - dotProduct(w, data))**2)
    
    errorDef = preError - error;
    preError = error
    
    print ("error = "+str(error))
    #print ("error def = "+str(errorDef))
    #print (str(w))
    
#print w
print ("w = "+str(w))

normw = 0
for i in range(0,noCols-1):
    normw += w[i]**2

normw = normw**decimal.Decimal(0.5)
print ("||w|| = "+str(normw))

dOrigin = abs(w[noCols-1]/normw)

print ("Distance to origin = "+ str(dOrigin))

print ("Predicted labels :")
#Prediction
predLbls = []
for i, data in enumerate(dataSets):
    if(tngLabels.get(i) is None):
        dp = dotProduct(w, data)
        if(dp > 0):
            print('1 '+ str(i))
            predLbls.append('1 ' + str(i))
        else:
            print('0 '+ str(i))
            predLbls.append('0 ' + str(i))
        
#write predicted labels to file
with open('predlabels.txt', 'w') as f:
    for row in predLbls:
        f.write(row + '\n')
f.close()   
  

            