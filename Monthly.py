#!/usr/bin/env python

from TimeFuncs import TimeFns
from time import localtime


class Monthly:

	@staticmethod
	def daysInMonth(mm):
		today = localtime()
		yyyy = today[0]
		today = TimeFns.makeDate(yyyy,mm,1)

		daylist=[]
		curr_mm = mm

		while curr_mm == mm:
			daylist.append(today)
                	today = TimeFns.nextDate(today)
			curr_mm = today[1]

		return daylist



	def __init__(self, ldate):
		self.month = ldate[1]
		self.days_in_month = Monthly.daysInMonth(self.month)
#		self.days = map(lambda x: x[2], self.days_in_month)
		self.days = len(self.days_in_month)
