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

	def reset(self):
		self.screen.border();
		self.screen.addstr(self.height+1,2,"a -left, s -down, d -right, w -up ")


	def __init__(self, screen, height, width):
		self.screen = screen
		self.width = width - 5; 
		self.height = height -2

		self.date = localtime()
		self.monthly = Monthly(self.date)

		self.cell_width = self.width/len(Settings.dow_order) 
		self.cell_height = self.height/self.monthly.nrows

		self.cell_y_off = self.height%(self.monthly.days/len(Settings.dow_order)) 
		self.cell_x_off = (self.width%len(Settings.dow_order))

		self.monthView()



	def drawMonth(self, date):
		start_dow = self.monthly.start_dow
		month_rows = self.monthly.nrows

		today = date
		dom=1
		counting = False

		cell_y = self.cell_y_off
		for y in xrange(month_rows):
			cell_x = self.cell_x_off
			for x in xrange(len(Settings.dow_order)):

				# Draw boxes (except today) in default color
				if dom == today[2]:
					Draw.rectangle(self.screen, cell_y, cell_x, 
						cell_y+self.cell_height, cell_x + self.cell_width, 
						Draw.color_today())
				else:
					Draw.rectangle(self.screen, cell_y, cell_x, 
						cell_y+self.cell_height, cell_x + self.cell_width)

				if not counting and x==start_dow:counting=True
				
				if counting:
					if dom <= self.monthly.days:
						self.screen.addstr(cell_y+1, cell_x+1, str(dom), Draw.color_dom())
						dom += 1
					else:
						counting = False

				cell_x += self.cell_width
			cell_y += self.cell_height

		self.screen.refresh()
		self.addDaysOfWeek()		# Add Days of Week
		


	def monthView(self):
		res = self.monthPrompt(self.date)

		# Change month or bring up a daily.
		while res!='end':
			if res=="next":
				ndate = TimeFns.nextMonth(self.date)
				res = self.monthPrompt(ndate)

			elif res=="prev":
				ndate = TimeFns.prevMonth(self.date)
				res = self.monthPrompt(ndate)



	def monthPrompt(self,date):
		self.date = date
		self.monthly = Monthly(date)
		self.drawMonth(date)
		return self.selectDay()


	def addDaysOfWeek(self):
		cell_x = self.cell_x_off
		for dow in Settings.dow_order:
			self.screen.addstr(0, cell_x + (self.cell_width/2), dow[0:Settings.dow_abrev_len], Draw.color_dow())
			cell_x += self.cell_width

		self.screen.addstr(0, 0, self.monthly.name, Draw.color_active())
		self.screen.refresh()


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
		dom = self.screen.instr(by+1, bx+1,2)

		if dom:
			return int(dom)

		
		if by > self.height - self.cell_height or  bx > self.width - self.cell_width :
			return "next"
		if by < self.cell_height or  bx < self.cell_width :
			return "prev"


	def selectDay(self):
		bounds_x, bounds_y = self.drawDaySelector()
		return self.getDaySelect(bounds_x, bounds_y)


	def getInput(self):
		inp=ord('v')
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


try:
	LifeMan(Draw.screen, int(sys.argv[1]), int(sys.argv[2]))
except KeyboardInterrupt:
	curses.endwin()
	exit(0)
