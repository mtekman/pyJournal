#!/usr/bin/env python

from time import localtime

from TimeFuncs import TimeFns
from Settings import Settings


class Monthly:

	month_map = {}
	month_map[1] = "Jan";
	month_map[2] = "Feb";
	month_map[3] = "Mar";
	month_map[4] = "Apr";
	month_map[5] = "May";
	month_map[6] = "Jun";
	month_map[7] = "Jul";
	month_map[8] = "Aug";
	month_map[9] = "Sep";
	month_map[10] = "Oct";
	month_map[11] = "Nov";
	month_map[12] = "Dec";


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
		self.name = Monthly.month_map[self.month]

		self.days_in_month = Monthly.daysInMonth(self.month)
		self.days = len(self.days_in_month)

		self.nrows = ( (self.days/len(Settings.dow_order)) 
						+ (0 if self.days%len(Settings.dow_order)==0 else 1) )

		self.start_dow = self.days_in_month[0][-3]

