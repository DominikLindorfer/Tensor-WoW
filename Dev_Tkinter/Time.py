# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 10:58:58 2021

@author: dl
"""

from datetime import date
today = date.today()
today

today.month
today.year
nextmonth = today + 30

def closest_date_next_month(year, month, day):
    month = month + 1
    if month == 13:
        month = 1
        year  = year + 1


    condition = True
    while condition:
        try:
            return date(year, month, day)
        except ValueError:
            day = day-1
        condition = day > 26

    raise Exception('Problem getting date next month')

paid_until = date(2021, 1, 30)

paid_until = closest_date_next_month(today.year, today.month, today.day)

for i in range(15):
    paid_until = closest_date_next_month(paid_until.year, paid_until.month, paid_until.day)
    print(paid_until)

import datetime

end_date = date(2021, 1, 30) + datetime.timedelta(days=120)


paid_until = closest_date_next_month(
                 last_paid_until.year, 
                 last_paid_until.month, 
                 original_purchase_date.day)  # The trick is here, I'm using the original date, that I started adding from, not the last one




d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)

d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)

d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)

d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)