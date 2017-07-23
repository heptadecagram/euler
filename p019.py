#!/usr/local/bin/python

def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 != 0:
            return true
        else if year % 400 == 0:
            return true
        else:
            return false
