# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 09:36:10 2020

@author: ildar
"""
import os
import pandas as pd 
import json
#from sklearn.externals import joblib
from . model_loaded import dict_model_pred
from . sts_loaded import dict_model_sts
from django.conf import settings

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
     #TODO Сделать загрузку модели в другом месте и сделать шкаливраоние каждой модели       
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
    except:
        pass
        
        
#%%
#numer_features = ['Year', 'horse', 'price_int', 'Пробег', 'probeg_god', 'probeg_god_del',
#       'year_sqv2', 'year_sqv3', 'probeg_sqv2', 'probeg_sqv3', 'Year2020',
#       'year2020_sqv2', 'year2020_sqv3', 'probeg_god_del_sqv2', 'horse_sqv2']
#
#categ_features = ['ВладельцевпоПТС', 'Количестводверей', 'Комплектация', 'Коробкапередач',
#       'Марка', 'Модель', 'Модификация', 'Поколение', 'Привод', 'Руль',
#       'Состояние', 'Типдвигателя', 'Типкузова', 'Цвет']
#
#column_info = ['price_inf', 'Year_inf', 'Пробег_inf', 'horse_inf', 'Марка_inf', 'Модель_inf']
#
##%%
#stdSc = StandardScaler()
##%%
#stsSc_pkl = stdSc.fit(X_df_avto.loc[:, numer_features])
##%%
#joblib.dump(stsSc_pkl, "sts_pkl_test.pkl")
##%%
#stsSc_loaded = joblib.load(path_stsSc + "sts_pkl_test.pkl")
#X_df_avto.loc[:, numer_features] = stsSc_loaded.transform(X_df_avto.loc[:, numer_features])
###%%
##X_df_avto.loc[:, numer_features] = stdSc.fit_transform(X_df_avto.loc[:, numer_features])
#X_df_avto_numer = X_df_avto[numer_features]
##X_df_avto_numer
##%%
#X_df_avto_categ = X_df_avto[categ_features]
#X_df_avto_column_info = X_df_avto[column_info]
##%%
#X_df_avto = pd.concat([X_df_avto_numer, X_df_avto_categ, X_df_avto_column_info], axis = 1) 
##%%
#X_df_avto.info()