from django.core.management.base import BaseCommand
from avtoapp.models import Avto, Marks, Mesto
import json
import os
from django.conf import settings

# from blogapp.models import Poll

class Command(BaseCommand):

    def handle(self, *args, **options):
        # Считываем с файла cars_params_dict5.json
        path = os.path.join(settings.BASE_DIR,'fixtures','cars_params_skoda.json' )
        with open(path, 'r') as f:
            result = json.load(f)

        # Создание
        for i in range(len(result)):
            try:
                marka = result[i]['Марка']
                marks_obj = Marks.objects.filter(name = marka)
                if not marks_obj:
                    Marks.objects.create(name=marka)
            except:
                continue

            try:
                mesto = result[i]['Местоосмотра']
                mesto = mesto.split(',')
                mesto = mesto[0]
                mesto_obj = Mesto.objects.filter(name = mesto)
                if not mesto_obj:
                    Mesto.objects.create(name = mesto)
            except:
                continue

            try:
                price = result[i]['price']
                vladeltsev = result[i]['ВладельцевпоПТС']
                year = result[i]['Годвыпуска']
                doors = result[i]['Количестводверей']
                complectation = result[i]['Комплектация']
                box = result[i]['Коробкапередач']
                model = result[i]['Модель']
                modification = result[i]['Модификация']
                pokolenie = result[i]['Поколение']
                privod = result[i]['Привод']
                probeg = result[i]['Пробег']
                probeg = probeg.replace('\xa0км', '')
                probeg = int(probeg)
                rull = result[i]['Руль']
                sostoyanie = result[i]['Состояние']
                type_engine = result[i]['Типдвигателя']
                type_kyzov = result[i]['Типкузова']
                color = result[i]['Цвет']
                cat_marka = Marks.objects.get(name = result[i]['Марка'])
                cat_mesto = Mesto.objects.get(name = mesto)
                text = result['text']
                href = result['referense']
                image_href_0 = result['image_href_0']
                image_href_1 = result['image_href_1']
                image_href_2 = result['image_href_2']

                Avto.objects.create(price=price, vladeltsev = vladeltsev, year = year,
                                    doors= doors, complectation= complectation,
                                    box=box, model=model, modification=modification,
                                    pokolenie=pokolenie,privod=privod, probeg=probeg,
                                    rull=rull, sostoyanie=sostoyanie,type_engine= type_engine,
                                    type_kyzov=type_kyzov, color=color, cat_marka = cat_marka,
                                    cat_mesto=cat_mesto, href=href, text=text,
                                    image_href_0=image_href_0, image_href_1=image_href_1,
                                    image_href_2=image_href_2)
            except:
                continue







