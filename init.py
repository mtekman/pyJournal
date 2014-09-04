#!/usr/bin/env python

import sys
import curses
import curses.ascii
#import curses.textpad
from Settings import Settings
from Monthly import Monthly
from TimeFuncs import TimeFns
from Draw import Draw

from time import localtime



class LifeMan:

	def __init__(self, screen, height, width):
		self.screen = screen

		self.width = width
		self.height = height

		self.screen.border();
		self.screen.addstr(0,2,"a -left, s - down, d-right")
		
		self.date = localtime()

		self.monthly = Monthly(self.date)
		dow_order = Settings.dow_order
		self.dow_list = map(lambda x: x[0:Settings.dow_abrev_len], dow_order)		

		self.drawGrid(self.date)

		res = self.getInput()
		curses.endwin()
		print res


	def drawGrid(self, date):

		start_dow = self.monthly.days_in_month[0][-3]
		month_rows = (self.monthly.days/len(self.dow_list)) + (0 if self.monthly.days%len(self.dow_list)==0 else 1)

		cell_width = self.width/len(self.dow_list) 
		cell_height = self.height/month_rows 

		dom=1
		counting = False

		cell_y_off = (self.height%(self.monthly.days/len(self.dow_list)))
		cell_x_off =  (self.width%len(self.dow_list))/2

		cell_y = cell_y_off

		today = localtime()

		for y in xrange(month_rows):
			cell_x = cell_x_off
			for x in xrange(len(self.dow_list)):

				# Draw boxes (except today) in default color
				if dom == today[2]:
					Draw.rectangle(self.screen, cell_y, cell_x, cell_y+cell_height, cell_x + cell_width, Draw.color_today())

#					today_store_x = cell_x
#					today_store_y = cell_y
				else:
					Draw.rectangle(self.screen, cell_y, cell_x, cell_y+cell_height, cell_x + cell_width)

				if not counting and x==start_dow:
					counting=True
				
				if counting:
					if dom <= self.monthly.days:
						self.screen.addstr(cell_y+1, cell_x+1, str(dom), Draw.color_dom())
						dom += 1
					else:
						counting = False


				cell_x += cell_width
			cell_y += cell_height
		

		# Add Days of Week
		cell_x = cell_x_off
		for dow in self.dow_list:
			self.screen.addstr(cell_y_off, cell_x + (cell_width/2), dow[0:(cell_width/2)], Draw.color_dow())
			cell_x += cell_width

		# Add Today
#		Draw.rectangle(self.screen, today_store_y, today_store_x, 
#					today_store_y+cell_height, today_store_x + cell_width,
#					Draw.color_today())
		

		self.screen.refresh()




	def getInput(self):
		inp=ord('f')
		try:
			inp = self.screen.getch()
		except IOError:
			pass
		return chr(inp)



#class Reminders:
#	

class Daily:
	log_dir = Settings.daily_logdir

	def __init__(self, date):
		self.date = date  # yyyy, mm, dd (tuple)
		self.log = Daily.log_dir + '/' + (Settings.daily_logfmt % self.date[0:3]) + '.' + Settings.daily_logext

		self.events = Daily.readDate(self.date)
		self.daily_log = Daily.parseLog(self.events)
		self.rem_completed, self.rem_pending = Daily.parseReminders(self.events)



#class Calendar:
#
#	def ():
#		c = Calendar()
#		for data in c


try:
	LifeMan(Draw.screen, int(sys.argv[1])-2, int(sys.argv[2])-2)
except KeyboardInterrupt:
	curses.endwin()
	exit(0)
