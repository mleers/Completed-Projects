import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt

data = pd.read_csv('2013sdweather.csv', parse_dates = ['DATE'])

data['normalized_date'] = data['DATE'].dt.date		#normalized date to remove 00:00:00

x = data.loc[:, 'DATE']		#csv headers
y1 = data.loc[:, 'TMAX']
y2 = data.loc[:, 'TMIN']
y3 = data.loc[:, 'PRCP']

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y1, label = 'Max Temp')
ax.plot(x, y2, label = 'Min Temp')

ax2 = ax.twinx()	#initiate independent y-axis with shared x-axis 
ax2.bar(x, y3, width = 1, color='r', label = 'Rainfall')
ax2.set_ylim(0, 10)

h1, l1 = ax.get_legend_handles_labels()		#gather lables for all data 
h2, l2 = ax2.get_legend_handles_labels()

ax.legend(h1+h2, l1+l2, loc = "best")		#combine labels for all data into 1 legend
ax.grid()

plt.title('Max/Min Temperatures and Precipitaion at SAN Airport During 2013 (GHCND:USW00023188)', fontsize = 15)
plt.xlabel('Date', fontsize = 10)
ax.set_ylabel('Temperature (F)')
ax2.set_ylabel('Precipitation (in)')

maxTMAX = np.nanmax(data.loc[:, 'TMAX'].values)
minTMAX = np.nanmin(data.loc[:, 'TMAX'].values)
maxTMIN = np.nanmax(data.loc[:, 'TMIN'].values)
minTMIN = np.nanmin(data.loc[:, 'TMIN'].values)

max_total = data.loc[data['TMAX'].idxmax()]		#max date time fetched by idxmax()
max_total_indexed = max_total['normalized_date']	#max date time indexed

min_max = data.loc[data['TMAX'].idxmin()]		#lowest high date fetched by idxmin()
min_max_indexed = min_max['normalized_date']

max_min = data.loc[data['TMIN'].idxmax()]
max_min_indexed = max_min['normalized_date']

min_total = data.loc[data['TMIN'].idxmin()]
min_total_indexed = min_total['normalized_date']

print("The highest temperature recorded was {} on {}".format(maxTMAX, max_total_indexed))
print("The lowest 'high' recorded was {} on {}".format(minTMAX, min_max_indexed))
print("The highest 'low' recorded was {} on {}".format(maxTMIN, max_min_indexed))
print("The lowest temperature recorded was {} on {}".format(minTMIN, min_total_indexed))

plt.show()


