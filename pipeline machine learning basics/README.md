# yandexpraktikum_consultation
Yandex praktikum consultation without data and sulotion code

## Pipeline structure

- config - a folder with config files in yaml format
- data - folder with data files
 - external - data from external sources
 - interim - spliting data
 - raw - raw data
 - processed - data after processing
- experiments - configs, logs of model results
- models - store models here
- src - source folder
 - data - work with data
 - evaluate - evaluate metrics
 - feature - work with features
 - pipelines - helper function sources
 - train - model training
 - transforms - change of features