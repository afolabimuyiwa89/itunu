# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 18:21:18 2022

@author: 1030 G2
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
 
df=pd.read_csv('C:/Users/1030 G2/Downloads/archive/time-series-19-covid.csv')
print(df)
df = df.drop('Province/State', axis = 1)
df['date'] = pd.to_datetime(df['Date'])
df['weekofyear'] = pd.DatetimeIndex(df['date']).weekofyear
df['month'] = pd.DatetimeIndex(df['date']).month
df['day'] = pd.DatetimeIndex(df['date']).day
df['weekday'] = pd.DatetimeIndex(df['date']).weekday
df['weekofyear'] = pd.DatetimeIndex(df['date']).weekofyear
data = df[['Country/Region', 'Confirmed', 'Deaths', 'Recovered','date', 'month', 'day', 'weekday', 'weekofyear']]
summary = [df['Confirmed'].sum(),df['Deaths'].sum(),df['Recovered'].sum()]
summary_table = pd.DataFrame(summary,['Confirmed','Deaths','Recovered'],columns=['Sum'])
print(summary_table)
plt.bar(summary_table.index,summary_table['Sum'])
def bar_chart(x_axis, list,title):
    plt.figure(figsize=(8,5))
    plt.bar(x_axis,list)
    plt.title(title, fontsize= 8)
    plt.show()
    return
x_axis = summary_table.index
my_list = summary_table['Sum']
title = 'A Bar Chart showing the total number of confirmed cases, Deaths abd Recovered cases'

bar_chart(x_axis,my_list,title)

month_group = data.groupby('month')[['Confirmed','Deaths','Recovered']].sum()
month_group
                                   
plt.figure()
plt.plot(month_group.index,month_group['Confirmed'],label = 'Confirmed')
plt.plot(month_group.index,month_group['Deaths'],label = 'Deaths')
plt.plot(month_group.index,month_group['Recovered'],label = 'Recovered')

plt.legend()

plt.show()
                                   
def line_plot(x_axis,my_list,xticks,label,title):
    plt.figure(figsize=(8,5))
    for i in range(len(my_list)):
        plt.plot(x_axis,my_list[i],label=label[i])
        plt.legend()
        plt.xticks()
        plt.title(title,fontsize=6)
        plt.show()
    
x_axis = month_group.index
my_list = [month_group['Confirmed'],month_group['Deaths'],month_group['Recovered']]
xticks = ['Jan','Feb','Mar','Apr','May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct']
label = ['Confirmed', 'Deaths', 'Recovered']
title = 'A line plot of confirmed cases, deaths and recovered casesfrom Jan to July'
line_plot(x_axis,my_list,xticks,label,title)

'The line chart above is a graphical representation of the Covid 19 trend from Jan 2020 to Otober 2020. The chart above shows the number of confirmed cases, deaths and recovered cases for each month in that period'
'As we can see,the cases across all three categories grew as the month passed, some at a rate faster than other due several interventions from the government of each country'

region_group = data.groupby('month')[['Confirmed','Deaths','Recovered']].sum()
region_group


plt.figure(figsize=(15,15))


plt.subplot(2,2,1).set_title('confirmed cases')
plt.pie(region_group['Confirmed'],labels=region_group.index)

plt.subplot(2,2,2).set_title('Deaths')
plt.pie(region_group['Deaths'],labels=region_group.index)

plt.subplot(2,2,3).set_title('Recovered')
plt.pie(region_group['Recovered'],labels=region_group.index)

plt.show()

def subplot_pie_chart(x_axis,label,title):
    plt.figure(figsize=(15,10))
    for i in range(len(x_axis)):
        plt.subplot(2,2,i+1).set_title(title[i])
        plt.pie(x_axis[i],labels=label)
        plt.show()
        
        x_axis = [region_group['Confirmed'],region_group['Deaths'],region_group['Recovered']]
        label = region_group.index
        title = ['Confirmed','Deaths','Recovered']
        subplot_pie_chart(x_axis,label,title)
        
