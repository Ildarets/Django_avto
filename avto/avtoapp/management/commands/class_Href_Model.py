import requests
from bs4 import BeautifulSoup
import time
import json

domain = 'https://www.avito.ru/rossiya/avtomobili'


class Href_Model:
    def __init__(self, DEEP):
        # self.url_model = url_model
        self.number_page = DEEP

    # https: // www.avito.ru / rossiya / avtomobili?p = 1
    def href_models(self):
        list_href_cars = []
        for i in range(1, self.number_page):
            page = i
            url = f'{domain}?p={page}'

            headers = {
                'authority': 'www.avito.ru',
                'method': 'GET',
                'path': '/moskva/avtomobili/ferrari_360_2000_1775773846',
                'scheme': 'https',
                'accept': 'ext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
                'cache-control': 'max-age=0',
                'cookie': 'u=2jz6x3tn.ot9948.gbx8z94gis; __cfduid=d9f8be2869150d70f00b679b5542a54041581761435; buyer_selected_search_radius0=200; _ga=GA1.2.575084678.1581761446; _gid=GA1.2.1061643092.1581761446; buyer_tooltip_location=0; _ym_uid=1573753899360583882; _ym_d=1581761451; sessid=cd575aa2a65cba3b5af23ca42ef5317c.1581863787; abp=2; no-ssr=1; f=5.0c4f4b6d233fb90636b4dd61b04726f147e1eada7172e06c47e1eada7172e06c47e1eada7172e06c47e1eada7172e06cb59320d6eb6303c1b59320d6eb6303c1b59320d6eb6303c147e1eada7172e06c8a38e2c5b3e08b898a38e2c5b3e08b890df103df0c26013a0df103df0c26013a2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b91772440e04006def90d83bac5e6e82bd59c9621b2c0fa58f897baa7410138ead3de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe207b7a18108a6dcd6f8ee35c29834d631c9ba923b7b327da71caed3f5220ce0ab049e6584365a0f6c2985db2d99140e2db186abe826e3b1d140e001317c4d7c0e38f0f5e6e0d2832ec5987b837f8da9d1e31784d6ce1af7c75dcded8022a3c9fccbf1a5019b899285164b09365f5308e731f2b7daefd09fa0ccd5569c3c25a82e2da10fb74cac1eab2da10fb74cac1eab3069315ebaf9ae7f8012e98924060d02; _ym_isad=1; buyer_popup_location=640310; _nfh=f2147bdfa8a1446d34273c6d84ef1521; __utma=99926606.575084678.1581761446.1581867800.1581867800.1; __utmc=99926606; __utmz=99926606.1581867800.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __gads=ID=a9e34cdf279ff99f:T=1581867800:S=ALNI_MbFVuSHi5-bTyg4lijEZFNzklSU8A; buyer_selected_search_radius4=0_general; buyer_location_id=621540; luri=rossiya; sx=H4sIAAAAAAACA53STXLqMAwA4Ltk3YXsKLHCbUAEEQRjqAqCdHr3pyzog22TmWxifdbfd9NTf5oJ8vXmIuRIDK5aqzWr7%2BbWrJpuGol0RxnjL7uZoLKyiyk4ePPRjM0qdZSGkoYOfz4a3HB71se8Sa7MsrwQIaBP0sb5cbztUCfD0NBJtBKBVKyO9YXsIFEJkvc%2B8aafRqFKwCKuhBYpPEm52jYdrPT7uFKFtSKBuzBSdec3ss0pSDrkTTkd9XhmIHKvpmKRCP6Sl%2FlruOB2vntUblE8s1HU4tEgk1cSoR%2BCHHdT3Xz2pV0DEzpGGigG%2Bpslz%2BPA%2B3UtQSJU0rhYDGut0c9Kb2Rq%2ByBbaneXdb5e7qeYidcg4ySq%2F4kcFrLPN6nnlnR5JEJ8iYvp%2FoXMeSl8uy80bYc5jhMbuMkCqtCTTKkeLe%2Fbz3R3i%2B0BsFifaGV8YkqvZFcoB7nm6VC%2Bhv7yqGAShccuGdn%2FXhYcykya1wPTkj0v%2BwBQQQRE30jqYuI%2F%2FwCKk%2FoR7AIAAA%3D%3D; dfp_group=6; buyer_from_page=catalog',
                'referer': 'https://www.avito.ru/rossiya/avtomobili/ferrari?cd=1',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
            }

            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')

            avtos = soup.find_all('a', class_='snippet-link')

            time.sleep(0.5)
            for avto in avtos:
                href = avto.get('href')
                list_href_cars.append(href)

        return list_href_cars
