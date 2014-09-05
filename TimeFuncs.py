from time import localtime, mktime

class TimeFns:

	@staticmethod
	def daysInMonth(month):
		today = list(localtime())
		today[1]= month
		today[2]= 1
		yyyy,mm,dd  = today[0:3]

		curr_mm = mm
		max_day = dd

		while curr_mm == mm:
			yyyy,mm,dd = TimeFns.nextDayTime(yyyy,mm,dd)
			if dd > max_day:max_day=dd
			#print yyyy,mm,dd
		return max_day


	@staticmethod
	def nextDayTime(yyyy,mm,dd):
		time_r = list(localtime())
		time_r[0] = int(yyyy)
		time_r[1] = int(mm)
		time_r[2] = int(dd)
		return TimeFns.nextDate[0:3]


	@staticmethod
	def nextMonth(date):
		month = date[1]+1; year = date[0]

		if month==13:
			month=1;year += 1
		return TimeFns.makeDate(year, month, 1)


	@staticmethod
	def prevMonth(date):
		month = date[1]-1; year = date[0]

		if month==0:
			month=12;year -= 1
		return TimeFns.makeDate(year, month, 1)
			

	@staticmethod
	def makeDate(yyyy,mm,dd):

		today = localtime()

		def isPast():
			if yyyy - today[0] > 0: return False
			if yyyy - today[0] == 0:
				if mm - today[1] > 0:return False
				if mm - today[1] == 0:
					if dd - today[2] > 0:return False
					return True
				return True
			return True



		if not isPast():
			while list(today[0:3]) != [yyyy,mm,dd]:
				today = TimeFns.nextDate(today)
		else:
#			c = 0
			while list(today[0:3]) != [yyyy,mm,dd]:
#				print today
#				c += 1
				today = TimeFns.previousDate(today)
#				if c== 4:break

		return today


	@staticmethod
	def nextDate(time_r, days=1):
		date_s = mktime(time_r)
		return localtime(date_s+(days*24*60*60))

	@staticmethod
	def previousDate(time_r, days=1):
		date_s = mktime(time_r)
		return localtime(date_s-(days*24*60*60))




