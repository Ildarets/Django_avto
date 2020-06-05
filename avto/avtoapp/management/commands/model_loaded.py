# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 10:27:52 2020

@author: ildar
"""
import os

from sklearn.externals import joblib
import glob
from django.conf import settings

# path = 'H:/avto/data_cars/pkl/'

path_models = os.path.join(settings.BASE_DIR,'fixtures','new_pkl')
# print('path_models', path_models)
files_dat = glob.glob(path_models + '/' +'*.pkl')
# print('files_dat', files_dat)
list_mark = []
for mark in files_dat:
    mark_model = mark.split('_')
    mark_model = mark_model[-1]
    # mark_model = mark_model.split('_')[2]
    mark_model = mark_model.split('.')[0]
    list_mark.append(mark_model)

# print(list_mark)

def dict_model_pred():
    dict_model = {}
    for mark in list_mark:
        model_loaded = joblib.load(path_models + '/' + f"svr_cv_new_{mark}.pkl")
        # print(type(model_loaded))
        dict_model[mark] = model_loaded
    return dict_model
    