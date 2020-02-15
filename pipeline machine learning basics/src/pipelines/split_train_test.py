import argparse
import yaml
from ipywidgets import Text

import sys 
import os.path as path

p = path.abspath(path.join(__file__ ,"../../.."))
sys.path.append(p)

from src.data.dataset import get_dataset
from src.transforms.trainsforms import split_dataset_in_train_test
from sklearn.preprocessing import StandardScaler
import numpy as np

def split_dataset(config_path: Text, base_config_path: Text):

    config = yaml.load(open(config_path), Loader=yaml.FullLoader)
    base_config = yaml.load(open(base_config_path), Loader=yaml.FullLoader)

    dataset = get_dataset(base_config['featurize']['featured_dataset_csv'], base_config['featurize']['dataset_sep'])
    random_state = base_config['base']['random_state']
    
    base_dataset = get_dataset(base_config['featurize']['dataset_csv'], base_config['featurize']['dataset_sep'])
    base_dataset = base_dataset[base_config['featurize']['features_columns_range']]
    var_numeric = base_dataset.select_dtypes([np.number]).columns

    test_size = config['test_size']
    valid_size = config['valid_size']
    train_csv_path = config['train_csv']
    test_csv_path = config['test_csv']
    valid_csv_path = config['valid_csv'] 
    
    '''
	Your code is here !!!
	'''
    
    train_dataset.to_csv(train_csv_path, sep=base_config['featurize']['dataset_sep'], encoding='utf-8', index=False)
    test_dataset.to_csv(test_csv_path, sep=base_config['featurize']['dataset_sep'], encoding='utf-8', index=False)
    valid_dataset.to_csv(valid_csv_path, sep=base_config['featurize']['dataset_sep'], encoding='utf-8', index=False)

if __name__ == '__main__':
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--config', dest='config', required=True)
    args_parser.add_argument('--base_config', dest='base_config', required=True)
    args = args_parser.parse_args()

    split_dataset(config_path=args.config, base_config_path=args.base_config)