from django.core.management.base import BaseCommand
from avtoapp.models import Avto, Marks, Mesto
import json
import os
import keras
import tensorflow as tf
from django.conf import settings
from keras.models import load_model
# from tensorflow.keras.models import load_model
# from blogapp.models import Poll
import pandas as pd
import pprint
from sklearn.model_selection import train_test_split
import numpy as np

from sklearn.linear_model import Ridge, RidgeCV, ElasticNet, LassoCV, LassoLarsCV, LinearRegression, ElasticNetCV
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, make_scorer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# import tensorflow as tf


# %%
def fill_top(column_top):
    # Возвращает топовые значения
    val_series = column_top.value_counts()[0:]
    val_str = str(val_series)
    val_list = val_str.split('   ')
    val_top = val_list[0]
    return val_top


# %%
def preprocess_data(avto):
    for i in range(len(avto)):
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
            # print(price)
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
            # print(type(avto[i]['horse']))
            # print(type(avto[i]['Модификация']))

        except:
            continue

        try:
            adress = avto[i]['Поколение']
            adress = adress.split('(')
            adress = adress[0]
            # print(adress)
            avto[i]['Поколение'] = adress
        except:
            continue

    return avto


# %%
def clear_data(df):
    # Удалаяем ненужные колонки
    df.drop('price', axis=1, inplace=True)
    df.drop('Годвыпуска', axis=1, inplace=True)
    df.drop('VINилиномеркузова', axis=1, inplace=True)
    df.drop('Местоосмотра', axis=1, inplace=True)
    # df.drop('Модификация', axis = 1, inplace = True)

    # Удаляем строки где нет цены
    df = df.dropna(how='any')

    df = df.replace({'ВладельцевпоПТС': {'4+': '5'}})

    # Добавляем новые признаки комбинированием
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

    return df

class Command(BaseCommand):

    def handle(self, *args, **options):
        # Считываем с файла cars_params_dict5.json
        path = os.path.join(settings.BASE_DIR,'fixtures','cars_params_vaz_lada2.json')
        with open(path, 'r') as f:
            result_test = json.load(f)
        print('*' * 50)
        print(result_test[0])
        print('*' * 50)

        # path = os.path.join(settings.BASE_DIR, 'fixtures', 'cars_params_vaz_lada3.json')
        # with open(path, 'r') as f:
        #     result = json.load(f)


        path = os.path.join(settings.BASE_DIR, 'fixtures', 'cars_params_vaz_lada3.json')
        with open(path, 'r') as f:
            result_train = json.load(f)


        print('*' * 50)
        print(result_test[0])
        print('*' * 50)
        # %% делаем предобработку данных
        avto_train = preprocess_data(result_train)
        avto_test = preprocess_data(result_test)
        # %% Преобразуем в датафрейм
        df_avto_train = pd.DataFrame(avto_train)
        df_avto_test = pd.DataFrame(avto_test)
        # print(df_avto.info())
        # %%
        # Очистка  данных и заполнение пустых значений и добавление новых признаков
        df_avto_train = clear_data(df_avto_train)
        df_avto_test = clear_data(df_avto_test)

        # print(df_avto.info())

        # %%
        # # Разделяем на тренировочные и тестовые
        # train, test = train_test_split(df_avto, test_size=0.2, random_state=42)
        # # test.info()

        # %%
        # Создаем метку для тренировочных и тестовых
        y_test = df_avto_test['price_int']
        y_train = df_avto_train['price_int']
        # Убираем из тренировочных и тестовых цену
        X_test_sel = df_avto_test.drop('price_int', axis=1)
        X_train_sel = df_avto_train.drop('price_int', axis=1)

        # print(X_test_sel.info())

        # %%
        # Разделяем на числовые и категориальные
        categ_features = X_train_sel.select_dtypes(include=["object"]).columns
        numer_features = X_train_sel.select_dtypes(exclude=["object"]).columns
        # print(numer_features)
        # print(categ_features)

        # %%
        X_train_numer = X_train_sel[numer_features]
        X_train_categ = X_train_sel[categ_features]
        # print(X_train_categ)
        X_test_numer = X_test_sel[numer_features]
        X_test_categ = X_test_sel[categ_features]

        # %%
        stdSc = StandardScaler()
        X_train_numer.loc[:, numer_features] = stdSc.fit_transform(X_train_numer.loc[:, numer_features])
        X_test_numer.loc[:, numer_features] = stdSc.transform(X_test_numer.loc[:, numer_features])

        # %%
        """
        # Нормализум числовые признаки
        # TODO сделать цена, пробег и год в этом месте
        mean = X_train_numer.mean(axis = 0)
        std = X_train_numer.std(axis = 0)
        X_train_numer -= mean
        X_train_numer /= std

        X_test_numer -= mean
        X_test_numer /= std

        #stdSc = StandardScaler()
        #X_train.loc[:, numerical_features] = stdSc.fit_transform(X_train.loc[:, numerical_features])
        #X_test.loc[:, numerical_features] = stdSc.transform(X_test.loc[:, numerical_features])
        """
        # %%
        #  Предварительная обработка категориальных признаков
        X_train_categ = pd.get_dummies(X_train_categ)

        X_test_categ = pd.get_dummies(X_test_categ)

        X_train_categ.info()

        # %%
        # Готовим общий  тренировочный набор
        additional_train_columns = []
        for column in X_test_categ:
            if column not in X_train_categ.columns:
                additional_train_columns.append(column)
                X_train_categ[column] = 0
        #
        # %%
        # Готовим общий тестовый набор
        additional_test_columns = []
        for column in X_train_categ:
            if column not in X_test_categ.columns:
                additional_test_columns.append(column)
                X_test_categ[column] = 0

        # %%
        X_train = pd.concat([X_train_numer, X_train_categ], axis=1)

        X_test = pd.concat([X_test_numer, X_test_categ], axis=1)

        # %%
        # print(additional_train_columns)
        # # %%
        # for y in y_train:
        #     if y < 0:
        #         print(y)
        # # %%
        # print(X_train.info())
        print(X_test.info())
        print('8' * 50)

        model = Sequential()
        model.add(Dense(1600, activation='relu', input_shape=(X_train.shape[1],)))
        model.add(Dense(800, activation='relu'))
        model.add(Dense(400, activation='relu'))
        model.add(Dense(200, activation='relu'))
        model.add(Dense(100, activation='relu'))
        model.add(Dense(1, activation='relu'))

        print(model.summary())

        model_dict = os.path.join(settings.BASE_DIR, 'fixtures', 'vaz_lada.h5')
        print(model_dict)
        print('//' * 50)
        # model = load_model(model_dict)

        model = tf.keras.models.load_model('vaz_lada.h5')

        print('XXX' * 50)
        predictions = model.predict(X_test)

        print(predictions[:20])












