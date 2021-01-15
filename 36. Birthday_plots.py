# In this exercise, use the bokeh Python library to plot a
# histogram of which months the scientists have birthdays in!
# Because it would take a long time for you to input the months
# of various scientists, you can use my scientist birthday JSON
# file. Just parse out the months (if you don’t know how, I
# suggest looking at the previous exercise or its solution)
# and draw your histogram.

import bokeh
from bokeh.plotting import figure, show, output_file
import json
import datetime
from collections import Counter

output_file("plot.html")
with open("names.json", "r") as f:
    names = json.load(f)

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

x = [x for x in count.keys()]
y = [y for y in count.values()]
print(x)
print(y)

p = figure(x_range = x)
p.vbar(x=x, top=y, width=0.5)
show(p)