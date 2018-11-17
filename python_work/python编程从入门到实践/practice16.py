import csv
from matplotlib import pyplot as plt
from datetime import datetime
filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
	dates,highs=[],[]
	for row in reader:
		dates.append(datetime.strptime(row[0],"%Y-%m-%d"))
		high = int(row[1])
		highs.append(high)
		
fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red')

plt.title("Daily high temperatures,July 2014",fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Tempeature(F)",fontsize=16)


plt.show()
