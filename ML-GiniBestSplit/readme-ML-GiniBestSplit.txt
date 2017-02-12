You need to run following python file to test Gini Best Split
machine learning algorithm

GiniBestSplitImpl.py <<data_file>> <<labels_file>> 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
GiniBestSplitImpl.py

Run following command to find best split s and column k

> python3 GiniBestSplitImpl.py data.txt labels.txt

Output:
noOfCols : 2
noOfRows : 8
minGini : 0.0
column - k : 0
best split - s : 5.5

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Second example

> python3 GiniBestSplitImpl.py data4.txt labels4.txt

Output:
noOfCols : 3
noOfRows : 8
minGini : 0.0
column - k : 2
best split - s : 3.5

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
breast cancer data set example

> python3 GiniBestSplitImpl.py breast_cancer.data breast_cancer.labels

Output:
noOfCols : 30
noOfRows : 569
minGini : 0.07115959045914586
column - k : 20
best split - s : 16.795

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ionosphere data set example

> python3 GiniBestSplitImpl.py ionosphere.data ionosphere.labels

Output:
noOfCols : 34
noOfRows : 351
minGini : 0.13259368368857422
column - k : 4
best split - s : 0.23154000000000002
