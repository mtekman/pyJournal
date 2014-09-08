#!/usr/bin/env python

from time import localtime

from TimeFuncs import TimeFns
from Settings import Settings


class Monthly:

	month_map = {
		1: "January",	2: "February",	3: "March",		4: "April",		
		5: "May",		6: "June",		7: "July",		8: "August",
		9: "September",	10: "October",	11: "November",	12: "December"
	}


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
		self.year = ldate[0]

		self.name = Monthly.month_map[self.month]
		if Settings.mon_abrev_len!=0:
			self.name = self.name[:Settings.mon_abrev_len]

		self.days_in_month = Monthly.daysInMonth(self.month)
		self.days = len(self.days_in_month)

		self.start_dow = self.days_in_month[0][-3]

#		self.nrows = ( (self.days/len(Settings.dow_order))
		temp_days = self.days + self.start_dow
		self.nrows = temp_days / len(Settings.dow_order)
		self.nrows += (0 if temp_days % self.nrows == 0 else 1)


