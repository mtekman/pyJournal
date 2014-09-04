#!/usr/bin/env python

import sys
import curses
import curses.ascii

from Settings import Settings
from Monthly import Monthly
from TimeFuncs import TimeFns
from Draw import Draw

from time import localtime

class LifeMan:

	def __init__(self, screen, height, width):
		self.screen = screen
		self.width = width; self.height = height

		self.screen.border();
		self.screen.addstr(self.height+1,2,"a -left, s -down, d -right, w -up ")
		
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

		self.cell_width = self.width/len(self.dow_list) 
		self.cell_height = self.height/month_rows 

		dom=1
		counting = False

		self.cell_y_off = self.height%(self.monthly.days/len(self.dow_list))
		self.cell_x_off =  (self.width%len(self.dow_list))/2

		today = localtime()

		cell_y = self.cell_y_off
		for y in xrange(month_rows):
			cell_x = self.cell_x_off
			for x in xrange(len(self.dow_list)):

				# Draw boxes (except today) in default color
				if dom == today[2]:
					Draw.rectangle(self.screen, cell_y, cell_x, cell_y+self.cell_height, cell_x + self.cell_width, Draw.color_today())
				else:
					Draw.rectangle(self.screen, cell_y, cell_x, cell_y+self.cell_height, cell_x + self.cell_width)

				if not counting and x==start_dow:
					counting=True
				
				if counting:
					if dom <= self.monthly.days:
						self.screen.addstr(cell_y+1, cell_x+1, str(dom), Draw.color_dom())
						dom += 1
					else:
						counting = False


				cell_x += self.cell_width
			cell_y += self.cell_height
		

		# Add Days of Week
		cell_x = self.cell_x_off
		for dow in self.dow_list:
			self.screen.addstr(0, cell_x + (self.cell_width/2), dow[0:(self.cell_width/2)], Draw.color_dow())
			cell_x += self.cell_width

		self.screen.refresh()
		res = self.selectDay()
		curses.endwin()
		print res
		exit(0)


	def drawDaySelector(self):
		pos_x = self.cell_x_off
		pos_y = self.cell_y_off

		f=-1
		while f==-1:
			last_x = pos_x
			last_y = pos_y

			inp = self.getInput()
			if inp == 'a':pos_x -= self.cell_width
			elif inp == 's':pos_y += self.cell_height
			elif inp == 'd':pos_x += self.cell_width
			elif inp == 'w':pos_y -= self.cell_height
			elif inp == ' ':
				return pos_x, pos_y

			if pos_x < self.cell_x_off:pos_x=last_x
			elif pos_x > (self.width - self.cell_width)+2:pos_x=last_x

			if pos_y < self.cell_y_off:pos_y=last_y
			elif pos_y > (self.height - self.cell_height)+2:pos_y=last_y

			Draw.rectangle(self.screen, last_y, last_x,
				last_y+self.cell_height, 
				last_x + self.cell_width)

			Draw.rectangle(self.screen, pos_y, pos_x,
				pos_y+self.cell_height, 
				pos_x + self.cell_width, 
				1, Draw.color_dom())

			self.screen.refresh()


	def getDaySelect(self,bx,by):
		dom = self.screen.getch(by+1, bx+1)
		return dom, int(dom)


	def selectDay(self):
		bounds_x, bounds_y = self.drawDaySelector()
		return self.getDaySelect(bounds_x, bounds_y)


	def getInput(self):
		inp=ord('?')
		try:
			inp = self.screen.getch()
		except IOError:
			pass
		return chr(inp)


#class Calendar:
#
#	def ():
#		c = Calendar()
#		for data in c



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



try:
	LifeMan(Draw.screen, int(sys.argv[1])-2, int(sys.argv[2])-2)
except KeyboardInterrupt:
	curses.endwin()
	exit(0)
