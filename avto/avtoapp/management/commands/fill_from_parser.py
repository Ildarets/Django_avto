from django.core.management.base import BaseCommand
from avtoapp.models import Avto, Marks, Mesto
import json
import os
from django.conf import settings
from .class_Href_Model import Href_Model
# from .class_list_models import List_Models
from .Deep_parser import Deep_Parser
import pprint
import time
import json


# from blogapp.models import Poll

class Command(BaseCommand):

    def handle(self, *args, **options):
        # Считываем с файла cars_params_dict5.json
        # path = os.path.join(settings.BASE_DIR,'fixtures','cars_params_dict5.json' )
        # with open(path, 'r') as f:
        #     result = json.load(f)

        # Создаем парсер и качаем оттуда
        # count_mark = 20000
        # global result
        DEEP = 50
        # MARK_NAME = 'mitsubishi'
        # NAME_FILE = f'cars_params_{MARK_NAME}.json'

        # parametrs_cars = []
        # list_models = List_Models()
        # all_list_models = list_models.list_models()
        #
        # def write_json(cars_dict):
        #     try:
        #         data = json.load(open(NAME_FILE))
        #     except:
        #         data = []
        #     data.append(cars_dict)
        #     with open(NAME_FILE, 'w') as file:
        #         json.dump(data, file, ensure_ascii=False)

        # #РАбочй код

        href_ = Href_Model(DEEP)
        list_cars_href = href_.href_models()
        print(list_cars_href)
        for href_model in list_cars_href:
            time.sleep(0.7)
            result = None
            try:
                params = Deep_Parser(href_model)
                result = params.parsing()
                # parametrs_cars.append(car_params)
                # pprint.pprint(car_params)
                # write_json(car_params)
            except:
                time.sleep(30)

        # Создание
            print(result)
            try:
                marka = result['Марка']
                marks_obj = Marks.objects.filter(name = marka)
                if not marks_obj:
                    Marks.objects.create(name=marka)
            except:
                continue

            try:
                mesto = result['Местоосмотра']
                mesto = mesto.split(',')
                mesto = mesto[0]
                mesto_obj = Mesto.objects.filter(name = mesto)
                if not mesto_obj:
                    Mesto.objects.create(name = mesto)
            except:
                continue

            try:
                price = result['price']
                print(price)
                vladeltsev = result['ВладельцевпоПТС']
                year = result['Годвыпуска']
                doors = result['Количестводверей']
                complectation = result['Комплектация']
                box = result['Коробкапередач']
                model = result['Модель']
                modification = result['Модификация']
                pokolenie = result['Поколение']
                privod = result['Привод']
                probeg = result['Пробег']
                probeg = probeg.replace('\xa0км', '')
                probeg = int(probeg)
                rull = result['Руль']
                sostoyanie = result['Состояние']
                type_engine = result['Типдвигателя']
                type_kyzov = result['Типкузова']
                color = result['Цвет']
                cat_marka = Marks.objects.get(name = result['Марка'])
                cat_mesto = Mesto.objects.get(name = mesto)
                text = result['text']
                href = result['referense']
                image_href_0 = result['image_href_0']
                image_href_1 = result['image_href_1']
                image_href_2 = result['image_href_2']
            except:
                continue


            Avto.objects.create(price=price, vladeltsev = vladeltsev, year = year,
                                doors= doors, complectation= complectation,
                                box=box, model=model, modification=modification,
                                pokolenie=pokolenie,privod=privod, probeg=probeg,
                                rull=rull, sostoyanie=sostoyanie,type_engine= type_engine,
                                type_kyzov=type_kyzov, color=color, cat_marka = cat_marka,
                                cat_mesto=cat_mesto, href = href, text = text,
                                image_href_0 = image_href_0, image_href_1 = image_href_1,
                                image_href_2 = image_href_2)








