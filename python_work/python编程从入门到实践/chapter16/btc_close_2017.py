import json
import pygal

filename = 'btc_close_2017.json'
with open(filename) as f:
	btc_date = json.load(f)

dates = []
months = []
weeks = []
weekdays = []
close = []



for btc_dict in btc_date:
	dates.append(btc_dict['date'])
	months.append(int(btc_dict['month']))
	weeks.append(int(btc_dict['week']))
	weekdays.append(btc_dict['weekday'])
	close.append(int(float(btc_dict['close'])))
	
line_chart = pygal.Line(x_label_roation=20,show_minor_x_labels=False)
line_chart.title ="收盘价"
line_chart.x_labels = dates
N = 20
line_chart.x_labels_major = dates[::N]
line_chart.render_to_file('收盘价折线图.svg')
