'''
Created on Sep 18, 2016

@author: bhaumikpatel
'''
import sys


dataFile = sys.argv[1]
tngLblFile = sys.argv[2]

#Read data file
dataSets = []
with open(dataFile) as f:
    for row in f:
        rowArray = list(map(float, row.split()))
        dataSets.append(rowArray)
f.close()
noCols = len(dataSets[0])   #noCols = no of class attributes
noRows = len(dataSets)  #noRows = no of training data sets
        
#Read label file
tngLabels = {} #create map of tngLabels to retrieve them in O(1) time
tnglblClsCnt = [0]*noCols
with open(tngLblFile) as f:
    for row in f:
        rowArray = row.split()
        tngLabels[rowArray[1]] = rowArray[0]
        tnglblClsCnt[int(rowArray[0])] += 1
f.close()

#Calculate Mean vector from training data sets
m0 = [0]*noCols
m1 = [0]*noCols

for i, data in enumerate(dataSets):
    for j, attr in enumerate(data):
        if('0' == tngLabels.get(str(i))):
            m0[j] = m0[j] + attr
        elif('1' == tngLabels.get(str(i))):
            m1[j] = m1[j] + attr
#
for i, val in enumerate(m0):
    m0[i] = val/tnglblClsCnt[0]

for i, val in enumerate(m1):
    m1[i] = val/tnglblClsCnt[1]        

print ('mean')    
print (m0)
print (m1) 

predLbls = []
for i, rowArray in enumerate(dataSets):
    if tngLabels.get(str(i)) is None:
        for j, item in enumerate(rowArray):
            data0Dist = 0
            data1Dist = 0
            data0Dist = data0Dist + (item - m0[j]) ** 2
            data1Dist = data1Dist + (item - m1[j]) ** 2
        
        if(data0Dist < data1Dist):
            print ("0 ", i)
            predLbl = "0 " + str(i)
            predLbls.append(predLbl)
        else:
            print ("1 ", i)
            predLbl = "1 "+ str(i)
            predLbls.append(predLbl)

#Calculate Standard deviation from training data sets
std0 = [0.0]*noCols
std1 = [0.0]*noCols

for i, data in enumerate(dataSets):
    for j, attr in enumerate(data):
        if('0' == tngLabels.get(str(i))):
            std0[j] = std0[j] + ((attr - m0[j])**2)
        elif('1' == tngLabels.get(str(i))):
            std1[j] = std1[j] + ((attr - m1[j])**2)
#
for i, val in enumerate(std0):
    std0[i] = (std0[i]/tnglblClsCnt[0])**(0.5)

for i, val in enumerate(std1):
    std1[i] = (std1[i]/tnglblClsCnt[1])**(0.5)
    
print ('standard deviation')
print (std0)
print (std1)

#Predict labels for data sets
predLbls = []
for i, data in enumerate(dataSets):
    if(tngLabels.get(str(i)) is None):
        pdf0Val = 0.0
        pdf1Val = 0.0
        for j, attr in enumerate(data):
            #Gaussian Probability Density Function (PDF)
            pdf0Val = pdf0Val + (((attr - m0[j])/std0[j])**2)
            pdf1Val = pdf1Val + (((attr - m1[j])/std1[j])**2)
        if(pdf0Val < pdf1Val):
            predLbls.append('0 ' + str(i))
            print('0 '+ str(i))
        else:
            predLbls.append('1 ' + str(i))
            print('1 '+ str(i))

#print "Predicted Labels" 
#print predLbls 

#write predicted labels to file
with open('predlabels.txt', 'w') as f:
    for row in predLbls:
        f.write(row + '\n')
f.close()
    
