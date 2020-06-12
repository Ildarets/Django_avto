# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 09:36:10 2020

@author: ildar
"""
import os
import pandas as pd 
import json
#from sklearn.externals import joblib
from django.core.management.base import BaseCommand
from . model_loaded import dict_model_pred
from . sts_loaded import dict_model_sts
from django.conf import settings
from avtoapp.models import Avto_pred

"""
Делает предсказание цены в зависимости от марки авто и загоняет в таблицу Avto_pred.
"""
# path_predict_model = 'H:/avto/data_cars/pkl/'

path_columns = os.path.join(settings.BASE_DIR,'fixtures','cars_columns.json')
# columns = 'cars_columns.json'

with open (path_columns, 'r', encoding='utf-8') as f:
    car_columns = json.load(f)

# print(car_columns['audi'])

categ_features = ['ВладельцевпоПТС', 'Количестводверей', 'Комплектация', 'Коробкапередач',
       'Марка', 'Модель', 'Модификация', 'Поколение', 'Привод', 'Руль',
       'Состояние', 'Типдвигателя', 'Типкузова', 'Цвет']
numer_features = ['Year', 'horse', 'Пробег', 'probeg_god', 'probeg_god_del',
   'year_sqv2', 'year_sqv3', 'probeg_sqv2', 'probeg_sqv3', 'Year2020',
   'year2020_sqv2', 'year2020_sqv3', 'probeg_god_del_sqv2', 'horse_sqv2']

dict_model = dict_model_pred()
dict_model_sts = dict_model_sts()

def predict_marks(mark, df_avto_i):  
    y_df_avto = df_avto_i['price_inf']
    df_avto_i = df_avto_i.drop('price_int', axis = 1)
    sts_loaded = dict_model_sts[mark]
    
    # X_df_avto_numer = df_avto_i[numer_features]
    
    df_avto_i.loc[:, numer_features] = sts_loaded.transform(df_avto_i.loc[:, numer_features])
    X_df_avto_numer = df_avto_i[numer_features]
    # print(X_df_avto_numer)
    
    X_df_avto_categ = df_avto_i[categ_features]
    X_df_avto_categ = pd.get_dummies(X_df_avto_categ)
    X_test_categ = car_columns[mark]
    for column in X_test_categ:
        if column not in X_df_avto_categ.columns:
            X_df_avto_categ[column] = 0


    for column in X_df_avto_categ.columns:
        if column not in X_test_categ:
            print("****" * 10)
            print(column)
            print()
#    model_loaded = joblib.load(path_predict_model + f"svr_cv_{mark}.pkl")

    model_loaded = dict_model[mark]

    X_train = pd.concat([X_df_avto_numer, X_df_avto_categ], axis = 1)
    # print(X_train)
    try:
        predicted_price = model_loaded.predict(X_train)
        real_price = y_df_avto
        dif_price = real_price - predicted_price
        if dif_price.iloc[0] < 0:
            # print (df_avto_i['Марка_inf'].iloc[0], df_avto_i['Модель_inf'].iloc[0], ' пробег' , df_avto_i['Пробег_inf'].iloc[0], df_avto_i['Description_inf'].iloc[0])
            # print(*predicted_price,'-->', real_price.iloc[0])
            print("Цена предсказанная: ",*predicted_price )
            # print("Цена на сайте Avito:", real_price.iloc[0])
            # print('-' * 20)
            # print()

            price = real_price.iloc[0]
            price_pred = predicted_price
            vladeltsev = df_avto_i['vladeltsev_inf'].iloc[0]
            year = df_avto_i['Year_inf'].iloc[0]
            doors = df_avto_i['doors_inf'].iloc[0]
            complectation = df_avto_i['complectation_inf'].iloc[0]
            box = df_avto_i['box_inf'].iloc[0]
            model = df_avto_i['Модель_inf'].iloc[0]
            modification = df_avto_i['modification_inf'].iloc[0]
            pokolenie = df_avto_i['pokolenieinf'].iloc[0]
            privod = df_avto_i['privod_inf'].iloc[0]
            probeg = df_avto_i['Пробег_inf'].iloc[0]
            rull = df_avto_i['rull_inf'].iloc[0]
            sostoyanie = df_avto_i['sostoyanie_inf'].iloc[0]
            type_engine = df_avto_i['type_engine_inf'].iloc[0]
            type_kyzov = df_avto_i['type_kyzov_inf'].iloc[0]
            color = df_avto_i['color_inf'].iloc[0]
            cat_marka = df_avto_i['Марка_inf'].iloc[0]
            cat_mesto = df_avto_i['Местоосмотра_inf'].iloc[0]
            text = df_avto_i['Description_inf'].iloc[0]
            href = df_avto_i['referense'].iloc[0]
            image_href_0 = df_avto_i['image_href_0_inf'].iloc[0]
            image_href_1 = df_avto_i['image_href_1_inf'].iloc[0]
            image_href_2 = df_avto_i['image_href_2_inf'].iloc[0]

            Avto_pred.objects.create(price=price, price_pred = price_pred, vladeltsev=vladeltsev, year=year,
                                doors=doors, complectation=complectation,
                                box=box, model=model, modification=modification,
                                pokolenie=pokolenie, privod=privod, probeg=probeg,
                                rull=rull, sostoyanie=sostoyanie, type_engine=type_engine,
                                type_kyzov=type_kyzov, color=color, cat_marka=cat_marka,
                                cat_mesto=cat_mesto, href=href, text=text,
                                image_href_0=image_href_0, image_href_1=image_href_1,
                                image_href_2=image_href_2)
    except:
        pass
        
