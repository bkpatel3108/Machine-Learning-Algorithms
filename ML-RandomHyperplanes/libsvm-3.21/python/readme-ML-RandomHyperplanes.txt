You need to run following commands to test RandomHyperPlanes Assignment

cd Assignment-7/
cd libsvm-3.21/python/
RandomHyperPlanes.py <<training_data_file>> <<training_labels_file>> <<testing_data_file>> <<no_of_random_planes>>

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
RandomHyperPlanes.py

Run following command for training using 'training data sets' 
and predicting labels for 'unknown data sets'

Predicated labels will be saved in Predicted_Labels_Using_RandomHyperPlanes.txt file in same directory 
as RandomHyperPlanes.py

> python3 RandomHyperPlanes.py traindata.txt trainlabels.txt testdata.txt 5

Output:
random w [[-0.719676509762395, -0.05701254600976058], [0.5440859757887813, -0.025278814343693057], [-0.1517775711771896, -0.9854890069741034], [0.14089256797176564, -0.7440731334855166], [-0.34455177566520967, -0.667119038609743]]
z [[0, 0, 0, 0, 0], [-1, -1, -1, -1, -1], [-1, 1, -1, 1, -1], [-1, 1, -1, -1, -1], [-1, 1, -1, -1, -1], [-1, 1, -1, -1, -1], [-1, 1, -1, -1, -1], [-1, 1, -1, -1, -1]]
tngLabels [0, 0, 0, 0, 1, 1, 1, 1]
z1 [[1, -1, 1, 1, 1], [-1, 1, -1, -1, -1]]

 ############## Using_RandomHyperPlanes ################### 

*
optimization finished, #iter = 4
nu = 0.927707
obj = -4.914815, rho = -0.550671
nSV = 8, nBSV = 6
Total nSV = 8
Accuracy = 87.5% (7/8) (classification)
training data accuracy =  (87.5, 0.125, 0.6)
Accuracy = 50% (1/2) (classification)

 ############## Predicted labels Using_RandomHyperPlanes ################### 

0 0
1 1

 ############## Using_OriginalDataPoints ################### 

..*.*
optimization finished, #iter = 29
nu = 0.387488
obj = -1.549822, rho = -0.000000
nSV = 8, nBSV = 0
Total nSV = 8
Accuracy = 100% (8/8) (classification)
training data accuracy =  (100.0, 0.0, 1.0)
Accuracy = 50% (1/2) (classification)

 ############## Predicted labels Using_OriginalDataPoints ################### 

0 0
1 1
