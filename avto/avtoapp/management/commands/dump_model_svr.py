# -*- coding: utf-8 -*-
"""
Created on Thu May 28 13:40:32 2020

@author: ildar
"""

import json
import pandas as pd
# import matplotlib.pyplot as plt
import pprint
from sklearn.model_selection import train_test_split
import numpy as np
import pprint
import glob

from sklearn.linear_model import Ridge,  RidgeCV, ElasticNet, LassoCV, LassoLarsCV, LinearRegression, ElasticNetCV
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, make_scorer
from sklearn.externals import joblib
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn import svm
from sklearn.model_selection import GridSearchCV, train_test_split

import os

from django.core.management.base import BaseCommand
import json
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.externals import joblib
from . preprocessing import preprocess_data, clear_data
from . predict_marks import predict_marks
from django.conf import settings
from django.conf import settings
from . sts_loaded import dict_model_sts

#%% Заливаем колонки
# columns = 'cars_columns.json'

"""Сохраннеие обученных моделей в pkl"""

path_columns = os.path.join(settings.BASE_DIR,'fixtures','cars_columns.json')
# columns = 'cars_columns.json'

with open (path_columns, 'r', encoding='utf-8') as f:
    car_columns = json.load(f)

dict_model_sts = dict_model_sts()

class Command(BaseCommand):

    def handle(self, *args, **options):

        path_pikled = os.path.join(settings.BASE_DIR, 'fixtures', 'pikled')

        files_dat_pikled = glob.glob(path_pikled + '/' + '*.json')
        print('files_dat_pikled', files_dat_pikled)


        for data in files_dat_pikled:

            fail = f'{data}'

            marks_pkl = fail.split('.')
            marks_pkl = marks_pkl[0]
            marks_pkl = marks_pkl.split('_')
            marks_pkl = marks_pkl[-1]
            print('marks_pkl' * 20, marks_pkl)

            with open (data, 'r', encoding='utf-8') as f:
                avto = json.load(f)

            categ_features = ['ВладельцевпоПТС', 'Количестводверей', 'Комплектация', 'Коробкапередач',
                              'Марка', 'Модель', 'Модификация', 'Поколение', 'Привод', 'Руль',
                              'Состояние', 'Типдвигателя', 'Типкузова', 'Цвет']
            numer_features = ['Year', 'horse', 'Пробег', 'probeg_god', 'probeg_god_del',
                              'year_sqv2', 'year_sqv3', 'probeg_sqv2', 'probeg_sqv3', 'Year2020',
                              'year2020_sqv2', 'year2020_sqv3', 'probeg_god_del_sqv2', 'horse_sqv2']


            #%% делаем предобработку данных
            avto = preprocess_data(avto)
            #%% Преобразуем в датафрейм
            df_avto = pd.DataFrame(avto)
            #print(df_avto.info())
            #%%
            #Очистка  данных и заполнение пустых значений и добавление новых признаков
            df_avto = clear_data(df_avto)

            # print(df_avto.info())

            y_df_avto = df_avto['price_inf']
            df_avto_i = df_avto.drop('price_int', axis=1)
            sts_loaded = dict_model_sts[marks_pkl]

            # X_df_avto_numer = df_avto_i[numer_features]

            df_avto_i.loc[:, numer_features] = sts_loaded.transform(df_avto_i.loc[:, numer_features])
            X_df_avto_numer = df_avto_i[numer_features]
            # print(X_df_avto_numer)

            X_df_avto_categ = df_avto_i[categ_features]
            X_df_avto_categ = pd.get_dummies(X_df_avto_categ)
            X_test_categ = car_columns[marks_pkl]
            for column in X_test_categ:
                if column not in X_df_avto_categ.columns:
                    X_df_avto_categ[column] = 0

            X_train = pd.concat([X_df_avto_numer, X_df_avto_categ], axis=1)
            # print(X_train)
            #%%
            svr_reg = svm.SVR(gamma=0.01, C=1500000, kernel = 'rbf')
            svr_reg.fit(X_train, y_df_avto)

            joblib.dump(svr_reg, f"svr_cv_new_{marks_pkl}.pkl")
            print('dumped', f'{marks_pkl}')

