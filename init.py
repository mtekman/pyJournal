#!/usr/bin/env python

import sys
import curses
import curses.ascii
#import curses.textpad
from Settings import Settings
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
		self.populateMonthGrid(width, height, self.date)
		self.drawGrid()

		res = self.getInput()
		curses.endwin()
		print res


	def populateMonthGrid(self, width, height, date): #offX, offY, date):
		self.monthly = Monthly(date)
		dow_order = Settings.dow_order
		dow_list = map(lambda x: x[0:Settings.dow_abrev_len], dow_order)		

		cell_width = width/len(dow_list) 
#		width_buff =  width%len(dow_list)/2

		cell_height = height/(self.monthly.days_in_month/len(dow_list)) 
#		height_buff = height%len(dow_list)/2

		dow_count=0

		self.grid=[]
		for y in xrange(height):
			row = []
			for x in xrange(width):
				cell=""
				if x%cell_width==0:cell='|'
				if y%cell_height==0:cell='-'

				if y==0 and x%cell_width==cell_width/2:
					cell=dow_list[dow_count%len(dow_list)]
					dow_count += 1

				if x%cell_width==1 and y%cell_height==1:
					cell='name'
	
				row.append(cell)
			self.grid.append(row)


	def drawGrid(self):
		cell_width = self.width/7
		cell_height = self.height/(self.monthly.days_in_month/7)

		cell_y = 0
		for y in xrange(4):
			cell_x = 0
			for x in xrange(7):
				Draw.rectangle(self.screen, cell_y, cell_x, cell_y+cell_height, cell_x + cell_width)
				cell_x += cell_width
			cell_y += cell_height
		self.screen.refresh()

#		for y in xrange(len(self.grid)):
#			for x in xrange(len(self.grid[0])):
#				res = self.screen.getch(y,x)
#				curses.endwin()
#				print res
#				self.screen.addstr(y,x, self.grid[y][x])
#		self.screen.refresh()



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



class Monthly:

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



	def __init__(self, ldate):
		self.month = ldate[1]
		self.days_in_month = Monthly.daysInMonth(self.month)


#class Calendar:
#
#	def ():
#		c = Calendar()
#		for data in c



l = LifeMan(int(sys.argv[1])-2, int(sys.argv[2])-2)
