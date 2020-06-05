
"""
Created on Fri Jun  5 10:27:52 2020

@author: ildar
"""
import os

from sklearn.externals import joblib
import glob
from django.conf import settings

#path = 'H:/avto/data_cars/pkl/'
# path_sts = 'H:/avto/data_cars/sts_pkl/'


##print(list_mark)
path_sts = os.path.join(settings.BASE_DIR,'fixtures','sts_pkl')


files_dat_sts = glob.glob(path_sts + '/'+ '*.pkl')
# print('files_dat_sts', files_dat_sts)

list_mark_sts = []
for mark in files_dat_sts:
    mark_model = mark.split('_')
    mark_model = mark_model[-1]
    # mark_model = mark_model.split('_')[2]
    mark_model = mark_model.split('.')[0]
    list_mark_sts.append(mark_model)

# print(list_mark_sts)


def dict_model_sts():
    dict_model_sts = {}
    for mark in list_mark_sts:
        model_loaded_sts = joblib.load(path_sts + '/' + f"sts_pkl_{mark}.pkl")
        # print(type(model_loaded_sts))
        dict_model_sts[mark] = model_loaded_sts
    return dict_model_sts

#print(dict_model_sts)