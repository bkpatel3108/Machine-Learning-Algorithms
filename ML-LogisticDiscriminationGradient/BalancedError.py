'''
Created on Sep 16, 2016

@author: bhaumikpatel
'''
import sys

trueLblFile = sys.argv[1]
predLblFile = sys.argv[2]

trueLbls = {}
predLbls = []

with open(trueLblFile) as f:
    for line in f:
        rowArray = line.split()
        trueLbls[rowArray[1]] = rowArray[0]
f.close() 

with open(predLblFile) as f:
    for line in f:
        rowArray = line.split()
        predLbls.append(rowArray)
f.close()

a, b, c, d, error = [0.0,0.0,0.0,0.0,0.0]

for predLbl in predLbls:
    predLblRowNo = predLbl[1]
    if(trueLbls.get(predLblRowNo) == '0' and predLbl[0] == '0'):
        a += 1.0
    if(trueLbls.get(predLblRowNo) == '0' and predLbl[0] == '1'):
        b += 1.0   
    if(trueLbls.get(predLblRowNo) == '1' and predLbl[0] == '0'):
        c += 1.0 
    if(trueLbls.get(predLblRowNo) == '1' and predLbl[0] == '1'):
        d += 1.0 

#print (a, ' ' , b, ' ', c, ' ', d)   

error = 0.5 * ((b/(a + b)) + (c/(c + d)))
print(error)
                 
        

