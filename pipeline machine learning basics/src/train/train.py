from comet_ml import Experiment
from comet_ml.utils import ConfusionMatrix

experiment = Experiment(api_key="K52aFZZhyMdEDeMC8Dz9r67GM",
                        project_name="yandex-project", workspace="alimbekovkz")

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import f1_score, make_scorer
from typing import Text, Dict
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import PredefinedSplit
from sklearn.utils import shuffle

class UnsupportedClassifier(Exception):

    def __init__(self, estimator_name):

        self.msg = f'Unsupported estimator {estimator_name}'
        super().__init__(self.msg)

def get_supported_estimator():

    return {
        'logreg': LogisticRegression,
        'decisionTree': DecisionTreeClassifier,
        'randomforest': RandomForestClassifier
    }

def downsample(features, target, fraction):
    '''
	Your code is here !!!
	'''

def upsample(features, target, repeat):
    '''
	Your code is here !!!
	'''

def train(df: pd.DataFrame, target_column: Text, estimator_name: Text, param_grid: Dict, cv: int, valid_df, class_weight, sampler, sampler_rate):

    estimators = get_supported_estimator()

    if estimator_name not in estimators.keys():

        raise UnsupportedClassifier(estimator_name)

    '''
	Your code is here !!!
	'''
	
    clf.fit(X_train, y_train)
    
    for i in range(len(clf.cv_results_['params'])):
        for k,v in clf.cv_results_.items():
            if k == "params":
                experiment.log_parameters(v[i])
            else:
                experiment.log_metric(k,v[i])

    return clf