from comet_ml import Experiment
from comet_ml.utils import ConfusionMatrix

'''
Use yor api_key !!!
'''
experiment = Experiment(api_key="",
                        project_name="", workspace="")

import argparse
import joblib
import json
import os
from typing import Text
import yaml

import sys 
import os.path as path

p = path.abspath(path.join(__file__ ,"../../.."))
sys.path.append(p)
from src.data.dataset import get_dataset
from src.evaluate.evaluate import evaluate


def evaluate_model(config_path: Text, base_config_path: Text):

    config = yaml.load(open(config_path), Loader=yaml.FullLoader)
    base_config = yaml.load(open(base_config_path), Loader=yaml.FullLoader)

    target_column = base_config['featurize']['target_column']
    test_df = get_dataset(base_config['split_train_test']['test_csv'], base_config['featurize']['dataset_sep'])
    model_name = base_config['base']['model']['model_name']
    models_folder = base_config['base']['model']['models_folder']

    model = joblib.load(os.path.join(models_folder, model_name))

    '''
	Your code is here !!!
	'''

    test_report = {
        'f1_score': f1,
        'precision' : precision,
        'recall' : recall,
        'accuracy' : accuracy
    }
    #print(test_report)
    filepath = os.path.join(base_config['base']['experiments']['experiments_folder'],
                            config['metrics_file'])
    json.dump(obj=test_report, fp=open(filepath, 'w'), indent=2)
    
    '''
	Your code is here !!!
	'''  
    experiment.log_confusion_matrix(matrix=cm.tolist())
    experiment.log_metrics(test_report)
    experiment.log_dataset_hash(test_df)
    

if __name__ == '__main__':
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--config', dest='config', required=True)
    args_parser.add_argument('--base_config', dest='base_config', required=True)
    args = args_parser.parse_args()

    evaluate_model(config_path=args.config, base_config_path=args.base_config)