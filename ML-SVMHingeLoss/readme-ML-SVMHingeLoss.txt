You need to run following python file to test gradient descent with hinge loss
machine learning algorithm
1. SVMHingeLoss.py <<data_file>> <<training_labels_file>> 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1. SVMHingeLoss.py
Run following command for training using 'training data sets' 
and predicting labels for 'unknown data sets'

Predicated labels will be saved in predlabels.txt file in same directory 
as SVMHingeLoss.py


> python3 SVMHingeLoss.py data.txt trainlabels.txt

Output:
Initial w [-0.0009430314426018046, 0.008249978556707635, -0.0030367622246563865]
error = 4.867560490338471
error = 4.327560490338471
error = 3.787560490338471
error = 3.37867641122081
error = 3.308042310659857
error = 3.19867641122081
error = 3.148042310659857
error = 3.0380423106598564
error = 2.9686764112208097
error = 2.8780423106598563
error = 2.78867641122081
.....................
error = 2.1986764112208093
error = 2.1280423106598554
error = 2.0186764112208095
error = 2.0072721686569914
error = 1.9486764112208095
error = 1.8679062692179451
error = 1.8479062692179449
error = 1.827906269217945
.....................
error = 1.036790348335606
error = 1.0279062692179444
error = 1.0079062692179441
error = 0.9879062692179443
.....................
error = 0.0653861057717866
error = 0.10427018488944872
error = 0.0742701848894487
error = 0.0653861057717866
.....................
error = 0.0542701848894489
error = 0.024270184889449098
error = 0.0
error = 0.0
w = [1.4990569685573991, -0.4717500214432926, -2.0330367622246572]
||w|| = 1.5715342432515575
Distance to origin = 1.2936636735437819
Predicted labels :
0 7
1 8

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Extra:

2. BalancedError.py
Run following command to check Balanced Error of predicted labels

> python3 BalancedError.py labels.txt predlabels.txt

Output:
0.0
