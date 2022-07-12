
import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding='UTF-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
pprint(contacts_list)


# TODO 1: выполните пункты 1-3 ДЗ
# 1 поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname

right_list = []
for in_list in contacts_list:
  fio_list = ' '.join(in_list[:3]).split()
  while len(fio_list) < 3:
    fio_list.append('')
  new_in_list = fio_list + in_list[3:]
  right_list.append(new_in_list)

# 2 привести все телефоны в формат +7(999)999-99-99. Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999;

l1 = []
for i in right_list:
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
d = {}
for in_list in l1:
  if ' '.join(in_list[:2]) not in d.keys():
    d[' '.join(in_list[:2])] = in_list[2:]
  else:
    l = []
    for id, elem in enumerate(d[' '.join(in_list[:2])]):
      if elem:
        l.append(elem)
      else:
        l.append(in_list[2:][id])
    d[' '.join(in_list[:2])] = l
pprint(d)

new_right_list = []
for key, val in d.items():
  new_right_list.append(key.split() + val)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding='UTF-8') as f:
  datawriter = csv.writer(f, delimiter=',',lineterminator = '\n')
  datawriter.writerows(new_right_list)




























