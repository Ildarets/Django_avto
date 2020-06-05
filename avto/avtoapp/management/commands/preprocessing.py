# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 09:06:40 2020

@author: ildar
"""
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




def rmse_cv_train(model):
    rmse= np.sqrt(-cross_val_score(model, X_train, y_train, scoring = scorer, cv = 10))
    return(rmse)

def rmse_cv_test(model):
    rmse= np.sqrt(-cross_val_score(model, X_test, y_test, scoring = scorer, cv = 10))
    return(rmse)
 #%%
def fill_top(column_top):
    #Возвращает топовые значения
    val_series = column_top.value_counts()[0:]
    val_str = str(val_series)
    val_list = val_str.split('   ')
    val_top = val_list[0]
    return val_top
#%%
def preprocess_data(avto):
    for i in range(len (avto)):
        try:
            rep = avto[i]['Пробег']
            avto[i]['Пробег'] = int(rep.replace('\xa0км', ''))
        except KeyError:
            continue
        
        try:
            rep = avto[i]['Годвыпуска']
            avto[i]['Year'] = int(rep)
        except KeyError:
            continue
        
        try:
            price = avto[i]['price']
            #print(price)
            avto[i]['price_int'] = int(price)
        except:
            print(i)
            
        try:
            modification_pr = avto[i]['Модификация']
            modification_pr = modification_pr.split('(')
            modification = modification_pr[0]
            horse_pr = modification_pr[1]
            horse_pr = horse_pr.split('л')
            horse = horse_pr[0]
            avto[i]['horse'] = int(horse)
            avto[i]['Модификация'] = modification
            #print(type(avto[i]['horse']))
            #print(type(avto[i]['Модификация']))
            
        except:
            continue
        
        try:
            adress = avto[i]['Поколение']
            adress = adress.split('(')
            adress = adress[0]
            #print(adress)
            avto[i]['Поколение'] = adress
        except:
            continue
    
    return avto
#%%
def clear_data(df):
    # Удалаяем ненужные колонки
    df.drop('price', axis = 1, inplace = True)
    df.drop('Годвыпуска', axis = 1, inplace = True)
    df.drop('VINилиномеркузова', axis = 1, inplace = True)
    df.drop('Местоосмотра', axis = 1, inplace = True)
    # df.drop('image_list', axis = 1, inplace = True)
    # df.drop('referense', axis = 1, inplace = True)
    # df.drop('text', axis = 1, inplace = True)
    
    
    # Удаляем строки где нет цены
    df = df.dropna(how = 'any')
    
    df = df.replace({'ВладельцевпоПТС' : {'4+' : '5'}})
    
     
    #Добавляем новые признаки комбинированием
    df['probeg_god'] = df['Year'] * df['Пробег']
    df['probeg_god_del'] = df['Пробег'] / df['Year']
    df['year_sqv2'] = df['Year'] ** 2
    df['year_sqv3'] = df['Year'] ** 3
    df['probeg_sqv2'] = df['Пробег'] ** 2
    df['probeg_sqv3'] = df['Пробег'] ** 3
    df['Year2020'] = 2020 - df['Year']
    df['year2020_sqv2'] = df['Year2020'] ** 2
    df['year2020_sqv3'] = df['Year2020'] ** 3
    df['probeg_god_del_sqv2'] = df['probeg_god_del'] ** 2
    df['horse_sqv2'] = df['horse'] ** 2
    
    #Колники таблицы для вывода результатов
    df['price_inf'] = df['price_int']
    df['Year_inf'] = df['Year']
    df['Пробег_inf'] = df['Пробег']
    df['horse_inf'] = df['horse']
    df['Марка_inf'] = df['Марка']
    df['Модель_inf'] = df['Модель']
    df['Description_inf'] = df['text']
    
    return df