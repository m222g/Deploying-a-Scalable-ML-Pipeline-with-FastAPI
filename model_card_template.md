# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

This model was implemented with the RandomForestClassifier from the scikit-learn library.

## Intended Use

This models intended use is to predict whether a persons income is greater than or less than $50,000 a year, based on numerous demographics.

## Training Data

This model was trained with Census Income Data from 1994 provided by UCI Irvine Machine Learning Repository. The training set contained 80% of the original dataset.

## Evaluation Data

This model was evaluated by a test set containing 20% of the original dataset.

## Metrics

Precision: 0.7459 | Recall: 0.6334 | F1: 0.6850

workclass: ?, Count: 389
Precision: 0.6207 | Recall: 0.4286 | F1: 0.5070
workclass: Federal-gov, Count: 191
Precision: 0.7879 | Recall: 0.7429 | F1: 0.7647
workclass: Local-gov, Count: 387
Precision: 0.7353 | Recall: 0.6818 | F1: 0.7075
workclass: Private, Count: 4,578
Precision: 0.7468 | Recall: 0.6364 | F1: 0.6872
workclass: Self-emp-inc, Count: 212
Precision: 0.7699 | Recall: 0.7373 | F1: 0.7532
workclass: Self-emp-not-inc, Count: 498
Precision: 0.7170 | Recall: 0.4841 | F1: 0.5779
workclass: State-gov, Count: 254
Precision: 0.7692 | Recall: 0.6849 | F1: 0.7246
workclass: Without-pay, Count: 4
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
education: 10th, Count: 183
Precision: 0.3333 | Recall: 0.1667 | F1: 0.2222
education: 11th, Count: 225
Precision: 1.0000 | Recall: 0.2727 | F1: 0.4286
education: 12th, Count: 98
Precision: 1.0000 | Recall: 0.4000 | F1: 0.5714
education: 1st-4th, Count: 23
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
education: 5th-6th, Count: 62
Precision: 1.0000 | Recall: 0.5000 | F1: 0.6667
education: 7th-8th, Count: 141
Precision: 1.0000 | Recall: 0.0000 | F1: 0.0000
education: 9th, Count: 115
Precision: 1.0000 | Recall: 0.3333 | F1: 0.5000
education: Assoc-acdm, Count: 198
Precision: 0.6667 | Recall: 0.5957 | F1: 0.6292
education: Assoc-voc, Count: 273
Precision: 0.6400 | Recall: 0.5079 | F1: 0.5664
education: Bachelors, Count: 1,053
Precision: 0.7653 | Recall: 0.7244 | F1: 0.7443
education: Doctorate, Count: 77
Precision: 0.8525 | Recall: 0.9123 | F1: 0.8814
education: HS-grad, Count: 2,085
Precision: 0.6520 | Recall: 0.4290 | F1: 0.5175
education: Masters, Count: 369
Precision: 0.8294 | Recall: 0.8454 | F1: 0.8373
education: Preschool, Count: 10
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
education: Prof-school, Count: 116
Precision: 0.8298 | Recall: 0.9286 | F1: 0.8764
education: Some-college, Count: 1,485
Precision: 0.6986 | Recall: 0.5271 | F1: 0.6008
marital-status: Divorced, Count: 920
Precision: 0.7800 | Recall: 0.3786 | F1: 0.5098
marital-status: Married-AF-spouse, Count: 4
Precision: 1.0000 | Recall: 0.3333 | F1: 0.5000
marital-status: Married-civ-spouse, Count: 2,950
Precision: 0.7400 | Recall: 0.6854 | F1: 0.7116
marital-status: Married-spouse-absent, Count: 96
Precision: 1.0000 | Recall: 0.2500 | F1: 0.4000
marital-status: Never-married, Count: 2,126
Precision: 0.7885 | Recall: 0.3981 | F1: 0.5290
marital-status: Separated, Count: 209
Precision: 1.0000 | Recall: 0.3684 | F1: 0.5385
marital-status: Widowed, Count: 208
Precision: 1.0000 | Recall: 0.1579 | F1: 0.2727
occupation: ?, Count: 389
Precision: 0.6207 | Recall: 0.4286 | F1: 0.5070
occupation: Adm-clerical, Count: 726
Precision: 0.6377 | Recall: 0.4583 | F1: 0.5333
occupation: Armed-Forces, Count: 3
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
occupation: Craft-repair, Count: 821
Precision: 0.6667 | Recall: 0.4751 | F1: 0.5548
occupation: Exec-managerial, Count: 838
Precision: 0.7941 | Recall: 0.7481 | F1: 0.7704
occupation: Farming-fishing, Count: 193
Precision: 0.5556 | Recall: 0.1786 | F1: 0.2703
occupation: Handlers-cleaners, Count: 273
Precision: 0.6667 | Recall: 0.3333 | F1: 0.4444
occupation: Machine-op-inspct, Count: 378
Precision: 0.5882 | Recall: 0.4255 | F1: 0.4938
occupation: Other-service, Count: 667
Precision: 0.8750 | Recall: 0.2692 | F1: 0.4118
occupation: Priv-house-serv, Count: 26
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
occupation: Prof-specialty, Count: 828
Precision: 0.7880 | Recall: 0.7679 | F1: 0.7778
occupation: Protective-serv, Count: 136
Precision: 0.7586 | Recall: 0.5238 | F1: 0.6197
occupation: Sales, Count: 729
Precision: 0.7647 | Recall: 0.6771 | F1: 0.7182
occupation: Tech-support, Count: 189
Precision: 0.6667 | Recall: 0.6275 | F1: 0.6465
occupation: Transport-moving, Count: 317
Precision: 0.6087 | Recall: 0.4375 | F1: 0.5091
relationship: Husband, Count: 2,590
Precision: 0.7442 | Recall: 0.6863 | F1: 0.7141
relationship: Not-in-family, Count: 1,702
Precision: 0.7938 | Recall: 0.4096 | F1: 0.5404
relationship: Other-relative, Count: 178
Precision: 0.6667 | Recall: 0.2500 | F1: 0.3636
relationship: Own-child, Count: 1,019
Precision: 0.6667 | Recall: 0.1176 | F1: 0.2000
relationship: Unmarried, Count: 702
Precision: 1.0000 | Recall: 0.2667 | F1: 0.4211
relationship: Wife, Count: 322
Precision: 0.7071 | Recall: 0.6923 | F1: 0.6996
race: Amer-Indian-Eskimo, Count: 71
Precision: 0.7500 | Recall: 0.6000 | F1: 0.6667
race: Asian-Pac-Islander, Count: 193
Precision: 0.7719 | Recall: 0.7097 | F1: 0.7395
race: Black, Count: 599
Precision: 0.7059 | Recall: 0.5538 | F1: 0.6207
race: Other, Count: 55
Precision: 1.0000 | Recall: 0.6667 | F1: 0.8000
race: White, Count: 5,595
Precision: 0.7455 | Recall: 0.6338 | F1: 0.6851
sex: Female, Count: 2,126
Precision: 0.7126 | Recall: 0.5107 | F1: 0.5950
sex: Male, Count: 4,387
Precision: 0.7506 | Recall: 0.6547 | F1: 0.6994
native-country: ?, Count: 125
Precision: 0.7241 | Recall: 0.6774 | F1: 0.7000
native-country: Cambodia, Count: 3
Precision: 1.0000 | Recall: 0.0000 | F1: 0.0000
native-country: Canada, Count: 22
Precision: 0.7000 | Recall: 0.8750 | F1: 0.7778
native-country: China, Count: 18
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
native-country: Columbia, Count: 6
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
native-country: Cuba, Count: 19
Precision: 0.6667 | Recall: 0.8000 | F1: 0.7273
native-country: Dominican-Republic, Count: 8
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
native-country: Ecuador, Count: 5
Precision: 1.0000 | Recall: 0.5000 | F1: 0.6667
native-country: El-Salvador, Count: 20
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
native-country: England, Count: 14
Precision: 0.5000 | Recall: 0.5000 | F1: 0.5000
native-country: France, Count: 5
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
native-country: Germany, Count: 32
Precision: 0.8182 | Recall: 0.6923 | F1: 0.7500
native-country: Greece, Count: 7
Precision: 1.0000 | Recall: 0.0000 | F1: 0.0000
native-country: Guatemala, Count: 13
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
native-country: Haiti, Count: 6
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
native-country: Honduras, Count: 4
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
native-country: Hong, Count: 8
Precision: 0.5000 | Recall: 1.0000 | F1: 0.6667
native-country: Hungary, Count: 3
Precision: 1.0000 | Recall: 0.5000 | F1: 0.6667
native-country: India, Count: 21
Precision: 0.7778 | Recall: 0.8750 | F1: 0.8235
native-country: Iran, Count: 12
Precision: 0.5000 | Recall: 0.4000 | F1: 0.4444
native-country: Ireland, Count: 5
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
native-country: Italy, Count: 14
Precision: 0.7500 | Recall: 0.7500 | F1: 0.7500
native-country: Jamaica, Count: 13
Precision: 0.0000 | Recall: 1.0000 | F1: 0.0000
native-country: Japan, Count: 11
Precision: 0.7500 | Recall: 0.7500 | F1: 0.7500
native-country: Laos, Count: 4
Precision: 1.0000 | Recall: 0.0000 | F1: 0.0000
native-country: Mexico, Count: 114
Precision: 1.0000 | Recall: 0.3333 | F1: 0.5000
native-country: Nicaragua, Count: 7
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
native-country: Peru, Count: 5
Precision: 0.0000 | Recall: 0.0000 | F1: 0.0000
native-country: Philippines, Count: 35
Precision: 1.0000 | Recall: 0.7500 | F1: 0.8571
native-country: Poland, Count: 14
Precision: 0.6667 | Recall: 1.0000 | F1: 0.8000
native-country: Portugal, Count: 6
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
native-country: Puerto-Rico, Count: 22
Precision: 0.8333 | Recall: 0.8333 | F1: 0.8333
native-country: Scotland, Count: 3
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
native-country: South, Count: 13
Precision: 0.5000 | Recall: 0.5000 | F1: 0.5000
native-country: Taiwan, Count: 11
Precision: 0.7500 | Recall: 0.7500 | F1: 0.7500
native-country: Thailand, Count: 5
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
native-country: Trinadad&Tobago, Count: 3
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
native-country: United-States, Count: 5,870
Precision: 0.7442 | Recall: 0.6265 | F1: 0.6803
native-country: Vietnam, Count: 5
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
native-country: Yugoslavia, Count: 2
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000


## Ethical Considerations

Data relating to any sort of demographics can reflect biases. This may cause uneven performance across different groups. 

## Caveats and Recommendations

This dataset is from 1994, so it doesn't reflect modern trends. Periodically retraining and reevaluating the model with updated data could make it more reliable. 
