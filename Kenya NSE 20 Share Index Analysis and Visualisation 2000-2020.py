# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 16:06:08 2020

@author: KIRIMI
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.animation import FuncAnimation
df = pd.read_csv(r'C:\Users\KIRIMI\.spyder-py3\My Projects\NSE 20 Share Index 20 Year Analysis Visualization (2000-2020)\Data\Kenya NSE 20 Historical Data.csv')
#Kindly note that the data above is the latest data as of 22nd March 2020
df.tail(5)
df.columns
df.index
df.dtypes
df['Dates'] = pd.to_datetime(df['Date'].str.replace(' ', '_').str.replace(',', '_'), errors='raise', format='%b_%d__%Y')
df['Dates'].dtypes
df.columns = df.columns.str.replace(' ', '_').str.replace('.', '_')
df2 = df[['Price', 'Open', 'High', 'Low', 'Dates']]
df2.replace(',', '', regex=True, inplace=True)
df2[['Price', 'Open', 'High', 'Low']] = df2[['Price', 'Open', 'High', 'Low']].apply(pd.to_numeric, errors ='raise')
df2.dtypes
df2.isnull().sum()
fig, ax1 = plt.subplots(figsize=(9,19))
plt.style.use('ggplot')

#PLOT NO1-NSE 20 Share Index 20-year Data Analysis and Visualisation
ax1.plot(df['Dates'], df2['Price'], color = 'brown', label='Price')
date_formatter_1 = mdates.DateFormatter('%Y')
locator1 = mdates.YearLocator(2)
ax1.set(xlabel='Dates', ylabel='Price')
ax1.xaxis.set_major_locator(locator1)
ax1.xaxis.set_major_formatter(date_formatter_1)
ax1.set_title('NSE 20 Share Index 20-year Performance Analysis (2001-2020)')

#PLOT NO2-Kenya's 2nd President, President Mwai Kibaki Tenure NSE 20 Share Index Performance (2003-2013)
fig, ax2 = plt.subplots(figsize=(11,11))
ax2.plot(df['Dates'], df2['Price'], color = 'blue', label='Price')
date_formatter_2 = mdates.DateFormatter('%Y')
locator2 = mdates.YearLocator()
ax2.set(xlabel='Dates', ylabel='Price', xlim = ['2003-01-01', '2013-04-01'])
ax2.xaxis.set_major_locator(locator2)
ax2.xaxis.set_major_formatter(date_formatter_2)
ax2.set_title('President Mwai Kibaki Tenure (January 2003-April 2013)')

#PLOT NO3-Kenya's 3rd President Uhuru Kenyatta Tenure April 2013-March 2020)
fig, ax3 = plt.subplots(figsize=(9,19))
ax3.plot(df['Dates'], df2['Price'], color = 'blue', label='Price')
ax3.set(xlabel='Dates', ylabel='Price', xlim = ['2013-04-01', '2020-03-19'])
date_formatter_3 = mdates.DateFormatter('%Y')
locator3 = mdates.YearLocator()
ax3.xaxis.set_major_locator(locator3)
ax3.xaxis.set_major_formatter(date_formatter_3)
ax3.set_title('President Uhuru Kenyatta Tenure (April 2013-March 2020)')

#PLOT NO4-President Uhuru Kenyatta Tenure (March 2019-March 2020)
fig, ax4 = plt.subplots(figsize=(7, 7))
ax4.plot(df['Dates'], df2['Price'], color = 'blue', label='Price')
ax4.set(xlabel='Dates', ylabel='Price', xlim = ['2019-03-04', '2020-03-19'])
date_formatter_4 = mdates.DateFormatter('%B\n%Y')
locator4 = mdates.MonthLocator()
ax4.xaxis.set_major_locator(locator4)
ax4.xaxis.set_major_formatter(date_formatter_4)
ax4.set_title('President Uhuru Kenyatta Tenure (March 2019-March 2020)')
#ax4.set_xticklabels(rotation=90)
plt.tight_layout()
plt.show()
