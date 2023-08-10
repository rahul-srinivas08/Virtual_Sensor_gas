
from tsfresh import extract_features, extract_relevant_features, select_features
from tsfresh.utilities.dataframe_functions import impute
from tsfresh.feature_extraction import ComprehensiveFCParameters
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import pandas as pd
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import numpy as np # linear algebra
import matplotlib 
import matplotlib.pyplot as plt
import sklearn
import seaborn as sns
def feat(fea):
    extraction_settings = ComprehensiveFCParameters()

    X = extract_features(df, column_id='index_col', column_sort='Time (seconds)',
                         default_fc_parameters=extraction_settings,
                         # we impute = remove all NaN features automatically
                         impute_function=impute)
    X_filtered = select_features(X, y)
    return X,X_filtered

def lasml(fea,y):
    X_train, X_test, y_train, y_test = train_test_split(fea, y, test_size=0.2, random_state=1,shuffle = False)
    model2 = linear_model.MultiTaskLasso(alpha=1200)
    model2.fit(X_train, y_train)

    ypred=model2.predict(X_test)
    co_pred=[]
    eth_pred=[]
    for i in range(0,len(ypred)):
        co_pred.append(ypred[i][0])
        eth_pred.append(ypred[i][1])
    return [co_pred,eth_pred]

def evalut(co,co_pred,eth,eth_pred):
    n=int(len(co)*0.8)
    plt.figure(1,figsize=(30,20))
    plt.plot(co[n:],color='blue')
    plt.plot(co_pred,color='red')
    plt.legend(['CO_pred', 'CO_true'],fontsize=36)

    plt.figure(2,figsize=(30,20))
    plt.plot(eth[n:],color='orange')
    plt.plot(eth_pred,color='purple')
    plt.legend(['eth_pred', 'eth_true'],fontsize=36)

    plt.show()
