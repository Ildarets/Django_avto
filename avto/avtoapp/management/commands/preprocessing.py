
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
    # df.drop('Местоосмотра', axis = 1, inplace = True)
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
    df['vladeltsev_inf'] = df['ВладельцевпоПТС']
    df['doors_inf'] = df['Количестводверей']
    df['complectation_inf'] = df['Комплектация']
    df['box_inf'] = df['Коробкапередач']
    df['modification_inf'] = df['Модификация']
    df['pokolenieinf'] = df['Поколение']
    df['privod_inf'] = df['Привод']
    df['rull_inf'] = df['Руль']
    df['sostoyanie_inf'] = df['Состояние']
    df['type_engine_inf'] = df['Типдвигателя']
    df['type_kyzov_inf'] = df['Типкузова']
    df['color_inf'] = df['Цвет']
    df['href_inf'] = df['referense']
    df['image_href_0_inf'] = df['image_href_0']
    df['image_href_1_inf'] = df['image_href_1']
    df['image_href_2_inf'] = df['image_href_2']
    df['Year_inf'] = df['Year']
    df['Пробег_inf'] = df['Пробег']
    df['horse_inf'] = df['horse']
    df['Марка_inf'] = df['Марка']
    df['Модель_inf'] = df['Модель']
    df['Description_inf'] = df['text']
    df['Местоосмотра_inf'] = df['Местоосмотра']
    df['referense_inf'] = df['referense']
    
    return df