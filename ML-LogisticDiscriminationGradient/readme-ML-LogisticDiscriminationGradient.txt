You need to run following python file to test logistic discrimination gradient descent
machine learning algorithm
1. LogisticDiscriminationGradientImpl.py <<data_file>> <<training_labels_file>> 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1. LogisticDiscriminationGradientImpl.py
Run following command for training using 'training data sets' 
and predicting labels for 'unknown data sets'

Predicated labels will be saved in predlabels.txt file in same directory 
as LogisticDiscriminationGradientImpl.py

First example data set

> python3 LogisticDiscriminationGradientImpl.py data.txt trainlabels.txt

Output:
error = 2.7741441316340163
error = 2.77414386679051
error = 2.7741436020387114
error = 2.7741433373785713
error = 2.7741430728100434
error = 2.7741428083330786
........................
error = 2.7740787127289117
error = 2.774078470048429
error = 2.774078227448333
error = 2.774077984928585
error = 2.7740777424891436
error = 2.7740775001299687
error = 2.7740736332668865
error = 2.774073392266144
error = 2.7740731513449517
error = 2.774072910503269
error = 2.774072669741058
error = 2.774072429058279
error = 2.7740721884548902
error = 2.7740719479308553
........................
error = 2.774006047067437
error = 2.7740058278535824
error = 2.7740056087086895
error = 2.7740053896327246
error = 2.774005170625655
error = 2.7740049516874485
error = 2.774004732818072
error = 2.77399971774477
error = 2.773999500517579
error = 2.7739848869803363
error = 2.7739846743722985
error = 2.773984461830113
error = 2.7739842493537474
error = 2.773984036943174
error = 2.7739838245983597
error = 2.7739836123192747
error = 2.773983400105888
error = 2.7739714115543896
error = 2.773971203099676
error = 2.7739709947088853
error = 2.773970786381987
error = 2.7739705781189508
error = 2.773970369919749
error = 2.77397016178435
error = 2.773969953712727
error = 2.7739697457048482
error = 2.7739695377606854
error = 2.7739693298802077
error = 2.773969122063388
error = 2.7739689143101955
........................
error = 2.7735523808830536
error = 2.773552280885721
w = [0.715485527830472, 0.7135806628452996, -6.549160585168024]
||w|| = 1.0105032918905246
Distance to origin = -6.481087827943012

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Second example data set

> python3 LogisticDiscriminationGradientImpl.py data2.txt trainlabels2.txt

Output:
Initial w [-0.008116338592849206, -0.008501308968700036, 0.008487022115410177]
error = 3.510014888518331
error = 3.6291000361856156
error = 3.73631686225878
error = 3.828402631364017
error = 3.904404336199328
error = 3.965001030950326
........................
error = 2.778520790889386
error = 2.7785206907799926
error = 2.778520590673972
error = 2.778520490571322
error = 2.778520390472043
error = 2.778520290376136
error = 2.778520190283599
error = 2.778520090194433
error = 2.7785199901086375
error = 2.7785198900262134
error = 2.7785197899471576
error = 2.778519689871473
error = 2.778519589799158
error = 2.7785194897302126
error = 2.778519389664637
error = 2.778519289602431
error = 2.778519189543594
error = 2.778519089488126
error = 2.7785189894360265
error = 2.7785188893872963
error = 2.7785187893419345
error = 2.7785186892999403
error = 2.7785185892613145
error = 2.778518489226057
error = 2.7785183891941676
error = 2.7785182891656452
error = 2.778518189140491
error = 2.778518089118703
error = 2.7785179891002834
error = 2.7785178890852302
error = 2.778517789073544
error = 2.7785176890652243
error = 2.778517589060271
error = 2.778517489058684
error = 2.778517389060463
w = [6.262165352366716, -1.066324725969659, -16.342951580714068]
||w|| = 6.352303780644974
Distance to origin = -2.572759764813185
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Extra:

2. BalancedError.py
Run following command to check Balanced Error of predicted labels

> python3 BalancedError.py labels.txt predlabels.txt
