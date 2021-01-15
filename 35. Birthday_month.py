import json
import datetime
from collections import Counter

months = {
    'january' : 1,
    'febrary' : 2,
    'march' : 3,
    'april' : 4,
    'may' : 5,
    'june' : 6,
    'july' : 7,
    'august' : 8,
    'september' : 9,
    'october' : 10,
    'november' : 11,
    'december' : 12
}

# def count_months():
with open("names.json", "r") as f:
        names = json.load(f)
dates = [(datetime.datetime.strptime(x, '%d/%m/%Y')).date() for x in names.values() ]
month = []

for x,y in months.items():
    for i in dates:
        if i.month == y:
            month.append(x)
count = Counter(month)
for x,y in count.items():
    print(f'{x} = {y}')
# print(count)

# if __name__ == '__main':
#     count_months()
