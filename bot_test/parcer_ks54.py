from bs4 import BeautifulSoup
import requests
import pprint

def all_week(URL):
    page = requests.get(URL)
    if page.status_code == 200:
        soup = BeautifulSoup(page.text, 'html.parser')

        time_sheet_site = soup.findAll('div', id='inner')  # отделили нужный нам кусок

        




    else:
        print('ERROR')


URL = 'https://www.ks54.ru/%D0%A1%D1%82%D1%83%D0%B4%D0%B5%D0%BD%D1%82%D1%83/%D0%A0%D0%B0%D1%81%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5_On-Line?group=2-%D0%98%D0%A1%D0%9F11-6'

all_week(URL)

