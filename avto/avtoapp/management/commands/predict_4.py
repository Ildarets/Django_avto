# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 14:40:05 2020

@author: ildar
"""
import os

from django.core.management.base import BaseCommand
import json
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.externals import joblib
from . preprocessing import preprocess_data, clear_data
from . predict_marks import predict_marks
from django.conf import settings


#%% Заливаем колонки
# columns = 'cars_columns.json'
"""
Предсказывает цену с помощью модели SVR. Работает.
"""

class Command(BaseCommand):

    def handle(self, *args, **options):
        # with open (path_columns, 'r', encoding='utf-8') as f:
        #     car_columns = json.load(f)
        #%%
        # file = 'cars_params_test_1.json'
        path_test = os.path.join(settings.BASE_DIR, 'fixtures', 'parsed_cars.json')
        with open (path_test, 'r', encoding='utf-8') as f:
            avto = json.load(f)

        #path_predict_model = 'H:/avto/data_cars/pkl/'
        #%%
        # path_stsSc = 'H:/avto/data_cars/'

        #%% делаем предобработку данных
        avto = preprocess_data(avto)
        #%% Преобразуем в датафрейм
        df_avto = pd.DataFrame(avto)
        print(df_avto.info())
        #%%
        #Очистка  данных и заполнение пустых значений и добавление новых признаков
        X_df_avto = clear_data(df_avto)
        print(X_df_avto.info())

        #%%
        # X_df_avto = df_avto
        # print(X_df_avto.info())

        #%%
        for i in range(len(X_df_avto)):
            df_avto_i = X_df_avto.iloc[[i]]
            if df_avto_i['Марка'].any() == 'Audi':
                predict_marks('audi', df_avto_i)
            elif df_avto_i['Марка'].any() == 'BMW':
                predict_marks('bmw', df_avto_i)
            elif df_avto_i['Марка'].any() == 'Chery':
                predict_marks('chery', df_avto_i)
            elif df_avto_i['Марка'].any() == 'Chevrolet':
                predict_marks('chevrolet', df_avto_i)
            elif df_avto_i['Марка'].any() == 'Сhrysler':
                predict_marks('chrysler', df_avto_i)
            elif df_avto_i['Марка'].any() == 'Сitroen':
                predict_marks('citroen', df_avto_i)
            elif df_avto_i['Марка'].any() == 'Daewoo':
                predict_marks('daewoo', df_avto_i)
            elif df_avto_i['Марка'].any() == 'Datsun':
                predict_marks('datsun', df_avto_i)
            elif df_avto_i['Марка'].any() == 'Dodge':
                predict_marks('dodge', df_avto_i)
            elif df_avto_i['Марка'].any() == 'Ford':
                predict_marks('ford', df_avto_i)
            elif df_avto_i['Марка'].any() == 'ГАЗ':
                predict_marks('gaz', df_avto_i)
            elif df_avto_i['Марка'].any() == 'Geely':
                predict_marks('geely', df_avto_i)
            elif df_avto_i['Марка'].any() == 'Great':
                predict_marks('great', df_avto_i)
            elif df_avto_i['Марка'].any() == 'Honda':
                predict_marks('honda', df_avto_i)
            elif df_avto_i['Марка'].any() == 'Hyundai':
                predict_marks('hyundai', df_avto_i)
            elif df_avto_i['Марка'].any() == 'Infiniti':
                predict_marks('infiniti', df_avto_i)
            elif df_avto_i['Марка'].any() == 'Jaguar':
                predict_marks('jaguar', df_avto_i)
            elif df_avto_i['Марка'].any() == 'Jeep':
                predict_marks('jeep', df_avto_i)
            elif df_avto_i['Марка'].any() == 'Kia':
                predict_marks('kia', df_avto_i)
            elif df_avto_i['Марка'].any() == 'Lexus':
                predict_marks('lexus', df_avto_i)
            elif df_avto_i['Марка'].any() == 'Mazda':
                predict_marks('mazda', df_avto_i)
            elif df_avto_i['Марка'].any() == 'Mercedes-benz':
                predict_marks('mercedes-benz', df_avto_i)
            elif df_avto_i['Марка'].any() == 'Mitsubishi':
                predict_marks('mitsubishi', df_avto_i)
            elif df_avto_i['Марка'].any() == 'Москвич':
                predict_marks('moskvich', df_avto_i)
            elif df_avto_i['Марка'].any() == 'Nissan':
                predict_marks('nissan', df_avto_i)
            elif df_avto_i['Марка'].any() == 'Opel':
                predict_marks('opel', df_avto_i)
            elif df_avto_i['Марка'].any() == 'Peugeot':
                predict_marks('peugeot', df_avto_i)
            elif df_avto_i['Марка'].any() == 'Porsche':
                predict_marks('porsche', df_avto_i)
            elif df_avto_i['Марка'].any() == 'Renault':
                predict_marks('renault', df_avto_i)
            elif df_avto_i['Марка'].any() == 'Skoda':
                predict_marks('skoda', df_avto_i)
            elif df_avto_i['Марка'].any() == 'Ssangyong':
                predict_marks('ssangyong', df_avto_i)
            elif df_avto_i['Марка'].any() == 'Subaru':
                predict_marks('subaru', df_avto_i)
            elif df_avto_i['Марка'].any() == 'Toyota':
                predict_marks('toyota', df_avto_i)
            elif df_avto_i['Марка'].any() == 'ВАЗ':
                predict_marks('vaz', df_avto_i)
            elif df_avto_i['Марка'].any() == 'Volkswagen':
                predict_marks('volkswagen', df_avto_i)
 