You need to run two python files to test naive bayes machine learning algorithm
1. NaiveBayesAlgoImpl.py <<data_file>> <<training_labels_file>> 
2. BalancedError.py <<labels_file>> <<predicted_labels_file>>

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1. NaiveBayesAlgoImpl.py 
Run following command for training using 'training data sets' 
and predicting labels for 'unknown data sets'

> python3 NaiveBayesAlgoImpl.py breast_cancer/breast_cancer.data breast_cancer/trainlabels/breast_cancer.trainlabels.0

Predicated labels will be saved in predlabels.txt file in same directory as NaiveBayesAlgoImpl.py

Output:
0 1
0 10
0 33
0 36
1 40
1 48
0 53
0 54
1 61
0 64
1 74
1 76
0 78
0 81
1 84
0 99
0 105
1 107
1 110
1 111
1 113
1 116
0 132
0 151
1 179
0 180
1 185
0 190
1 195
0 208
1 209
1 224
1 231
1 263
1 273
0 277
1 314
1 319
1 324
0 335
1 348
1 354
1 356
0 369
1 403
1 411
1 438
1 472
1 475
1 478
1 481
1 482
0 512
1 518
0 535
1 554
0 563
0 567
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

2. BalancedError.py
Run following command to check Balanced Error of predicted labels using naive bayes algorithm

> python3 BalancedError.py breast_cancer/breast_cancer.labels predlabels.txt

Output:
0.08712121212121213
