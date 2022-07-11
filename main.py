# Структура данных будет всегда:
# lastname,firstname,surname,organization,position,phone,email
# Предполагается, что телефон и e-mail у человека может быть только один.
# Необходимо:
# поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно.
# В записной книжке изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О;
# привести все телефоны в формат +7(999)999-99-99. Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999;
# объединить все дублирующиеся записи о человеке в одну.
import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding='UTF-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
#pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# 1 поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname
l = []
for i in contacts_list:
  k = []
  for id, text in enumerate(i):
    if id in (0,1,2) and len(text.split()) > 1:
      k.extend(text.split())
    else:
      k.append(text)
  l.append(k)
pprint(l)
print('_____________________________________________')

# 2 привести все телефоны в формат +7(999)999-99-99. Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999;
l1 = []
for i in l:
  k1 = []
  for text in i:
    pattern = r'(\+7|8)?\s*\(?(\d{3})\)?[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})\s*\(?([доб.]*\s*\d*)\)?'
    if re.search(pattern,text):
      k1.append(re.sub(pattern, r'+7(\2)\3-\4-\5 \6', text))
    else:
      k1.append(text)
  l1.append(k1)
pprint(l1)

# 3 объединить все дублирующиеся записи о человеке в одну.


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding='UTF-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(l1)




























