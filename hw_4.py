'''
Выберите веб-сайт с табличными данными, который вас интересует.
Напишите код Python, использующий библиотеку requests для отправки HTTP GET-запроса на сайт и получения HTML-содержимого страницы.
Выполните парсинг содержимого HTML с помощью библиотеки lxml, чтобы извлечь данные из таблицы.
Сохраните извлеченные данные в CSV-файл с помощью модуля csv.

Ваш код должен включать следующее:

Строку агента пользователя в заголовке HTTP-запроса, чтобы имитировать веб-браузер и избежать блокировки сервером.
Выражения XPath для выбора элементов данных таблицы и извлечения их содержимого.
Обработка ошибок для случаев, когда данные не имеют ожидаемого формата.
Комментарии для объяснения цели и логики кода.

Примечание: Пожалуйста, не забывайте соблюдать этические и юридические нормы при веб-скреппинге.
'''
import requests
import time
from lxml import html
import pandas as pd

url = 'https://worldathletics.org/records/toplists/road-running/5-kilometres/all/men/senior/2023'

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'

response = requests.get(url, headers={'User-Agent': user_agent})

tree = html.fromstring(response.content)

table_rows = tree.xpath('.//*[@id="toplists"]/div[3]/table/tbody/tr')

data = []
for row in table_rows:
    columns = row.xpath('.//td/text()')
    data.append(
    {'rank': columns[0].strip(),
     'mark': columns[1].strip(),
     'wind': columns[2].strip(),
     'competitor': row.xpath('.//a/text()')[0].strip(),
     'DOB': columns[5].strip(),
     'NAT': columns[7].strip(),
     'pos': columns[8].strip(),
     'venue': columns[9].strip(),
     'date': columns[10].strip(),
     'result_score': columns[11].strip()
     })
    
df = pd.DataFrame(data)
print(df.head(5))

df.to_csv('results.csv')
    





    


 

