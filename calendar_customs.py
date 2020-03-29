# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 13:50:30 2020

@author: ganapathy
"""

import calendar
c=calendar.TextCalendar()

def Sundays(month,year):
    calendar_days=[x for x in c.itermonthdays(year,month)]
    days_of_month=[day for day in range(len(calendar_days)) if calendar_days[day]!=0]
    #print(days_of_month)
    Sundays=[6,13,20,27,34,41,48]
    return sum([1 if day in Sundays else 0 for day in days_of_month])

year=2018
months=[month for month in range(12)]
months_ge_5S_list=[]
months_list=[x+1 for x in range(12)]
for month in months_list:
    if Sundays(month,year)>=5:
        months_ge_5S_list.append(calendar.month_abbr[month])
print(months_ge_5S_list)