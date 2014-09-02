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
		date_s = mktime(time_r)
		return localtime(date_s+(24*60*60))[0:3]


	def nextDay(date):
        	try:
                	date_sec = ymd2secs( date.split('/') )
        	except AttributeError:
                	date_sec = date
                	pass
		return "%04d/%02d/%02d" % localtime(date_sec+(24*60*60))[0:3]


