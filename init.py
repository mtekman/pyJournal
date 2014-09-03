#!/usr/bin/env python

import sys
import curses
import curses.ascii
#import curses.textpad
from Settings import Settings
from Monthly import Monthly
from TimeFuncs import TimeFns
from time import localtime

class Draw:
	@staticmethod
	def rectangle(win, uly, ulx, lry, lrx):
	    """Draw a rectangle with corners at the provided upper-left
	    and lower-right coordinates.
	    """
	    win.vline(uly+1, ulx, curses.ACS_VLINE, lry - uly - 1)
	    win.hline(uly, ulx+1, curses.ACS_HLINE, lrx - ulx - 1)
	    win.hline(lry, ulx+1, curses.ACS_HLINE, lrx - ulx - 1)
	    win.vline(uly+1, lrx, curses.ACS_VLINE, lry - uly - 1)
#	    win.addch(uly, ulx, curses.ACS_ULCORNER)
#	    win.addch(uly, lrx, curses.ACS_URCORNER)
#	    win.addch(lry, lrx, curses.ACS_LRCORNER)
#	    win.addch(lry, ulx, curses.ACS_LLCORNER)
	    win.addch(uly, ulx, '+')
	    win.addch(uly, lrx, '+')
	    win.addch(lry, lrx, '+')
	    win.addch(lry, ulx, '+')



class LifeMan:

	def __init__(self, height, width):
		self.screen = curses.initscr();
		self.width = width
		self.height = height

		curses.curs_set(0)
		curses.noecho()

		self.screen.border();
		self.screen.addstr(0,2,"a -left, s - down, d-right")
		
		self.date = localtime()

		self.monthly = Monthly(self.date)
		dow_order = Settings.dow_order
		self.dow_list = map(lambda x: x[0:Settings.dow_abrev_len], dow_order)		
#		self.dow_list = dow_order		

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
		for y in xrange(month_rows):
			cell_x = cell_x_off
			for x in xrange(len(self.dow_list)):
				Draw.rectangle(self.screen, cell_y, cell_x, cell_y+cell_height, cell_x + cell_width)

				if not counting and x==start_dow:
					counting=True
				
				if counting:
					if dom <= self.monthly.days:
						self.screen.addstr(cell_y+1, cell_x+1, str(dom))
						dom += 1
					else:
						counting = False


				cell_x += cell_width
			cell_y += cell_height
		

		cell_x = cell_x_off
		for dow in self.dow_list:
			self.screen.addstr(cell_y_off, cell_x + (cell_width/2), dow[0:(cell_width/2)])
			cell_x += cell_width

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
	LifeMan(int(sys.argv[1])-2, int(sys.argv[2])-2)
except KeyboardInterrupt:
	curses.endwin()
	exit(0)
