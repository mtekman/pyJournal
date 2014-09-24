#from time import localtime, mktime
from datetime import date, timedelta

class TimeFns:

	@staticmethod
	def daysInMonth(mm):
		yyyy = date.today().year
		dd = 20 # at least 20 days in a month... right?

		while True:
			try:
				date(yyyy,mm,dd)
				dd +=1
			except ValueError:
				return dd



	@staticmethod
	def nextMonth(d):
		month = d.month+1;
		year = d.year

		if month==13:
			month=1;year += 1
#		return TimeFns.makeDate(year, month, 1)
		return date(year, month, 1)

	@staticmethod
	def prevMonth(d):
		month = d.month-1; 
		year = d.year

		if month==0:
			month=12;year -= 1
		#return TimeFns.makeDate(year, month, 1)
		return date(year,month,1)
	
	@staticmethod
	def makeDate(yyyy,mm,dd):

		return date(yyyy,mm,dd)
#
#		today = localtime()
#
#		def isPast():
#			if yyyy - today[0] > 0: return False
#			if yyyy - today[0] == 0:
#				if mm - today[1] > 0:return False
#				if mm - today[1] == 0:
#					if dd - today[2] > 0:return False
#					return True
#				return True
#			return True
#
#
#
#		if not isPast():
#			while list(today[0:3]) != [yyyy,mm,dd]:
#				today = TimeFns.nextDate(today)
#		else:
##			c = 0
#			while list(today[0:3]) != [yyyy,mm,dd]:
##				print today
##				c += 1
#				today = TimeFns.previousDate(today)
##				if c== 4:break
#
#		return today


	@staticmethod
	def nextDate(datearg, days=1):
#		date_s = mktime(time_r)
#		return localtime(date_s+(days*24*60*60))
		return datearg + timedelta(days)

	@staticmethod
	def previousDate(datearg, days=1):
#		date_s = mktime(time_r)
#		return localtime(date_s-(days*24*60*60))
		return datearg - timedelta(days)



