#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys

def dateinput():
        date = raw_input('please input the first date: ')
        return date

def datetrans(tdate):
        spdate = tdate.replace("/","-")
        try:
                datesec = time.strptime(spdate,'%Y-%m-%d')
        except ValueError:
                print "%s is not a rightful date!!" % tdate
                sys.exit(1)
        return time.mktime(datesec)

def daysdiff(d1,d2):
        daysec = 24 * 60 * 60
        return int(( d1 - d2 )/daysec)

date1 = dateinput()
date2 = dateinput()

date1sec = datetrans(date1)
date2sec = datetrans(date2)

print "The number of days between two dates is: ",daysdiff(date1sec,date2sec)
