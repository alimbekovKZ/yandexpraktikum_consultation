import numpy as np
import pandas as pd
import sklearn.base
from sklearn.metrics import f1_score, precision_score, recall_score, confusion_matrix, accuracy_score
from typing import Text, Tuple, Dict

def evaluate(df: pd.DataFrame, target_column: Text, clf: sklearn.base.BaseEstimator) -> Tuple[float, np.array]:
    
    '''
	Your code is here !!!
	'''

    print("F1 score is {:6.3f}".format(f1))
    print("Precision score is {:6.3f}".format(precision))
    print("Recall score is {:6.3f}".format(recall))
    print("Accuracy is {:6.3f}".format(accuracy))

    return f1, cm, precision, recall, accuracy