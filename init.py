#!/usr/bin/env python

import sys
import curses, curses.ascii

from Settings import Settings
from Monthly import Monthly
from TimeFuncs import TimeFns
from Draw import Draw
from Screens import Screens

from MonthHandler import MonthHandler
from DayHandler import DayHandler
from Common import Common

from OptsGeneralHandler import OptsGeneral


from datetime import date


class LifeMan:

	def setPanels(self):
		panels.initiate()
		self.reset = panels.clear

		self.screen_main = panels.right.screen
		self.screen_options = panels.left.screen
		self.screen_info = panels.top.screen

		self.info_main = panels.right.info
		self.info_options = panels.left.info
		self.info_info = panels.top.info


	def setDimensions(self,panels):
		self.width = panels.total_width
		self.height = panels.total_height

		self.cell_width = (self.info_main.width/len(Settings.dow_order)) -1
		self.cell_height = (self.info_main.height /self.monthly.nrows )

		self.cell_y_off = (
			self.info_main.height - (self.cell_height*self.monthly.nrows) ) / 2
		if self.cell_y_off == 0:
			self.cell_y_off = 1
		#	self.cell_height -= 1


		self.cell_x_off = (
			self.info_main.width - (self.cell_width*len(Settings.dow_order)) ) / 2



	def __init__(self, panels):
		self.date = date.today()
		self.monthly = Monthly(self.date)

		self.setPanels()
		self.setDimensions(panels)

		self.monthView()



	def monthView(self):

#		MonthHandler.generalOpts(self)
		MonthHandler.addDaysOfWeek(self)

		res = ""
		ndate = self.date
		# Change month or bring up a daily.
		while not (res=='end' or res==-2):
			if res=="next":
				ndate = TimeFns.nextMonth(self.date)
			elif res=="prev":
				ndate = TimeFns.prevMonth(self.date)

			res = self.monthPrompt(ndate)

			if res == -2:
				OptsGeneral(self.screen_options, self.info_options)

#			curses.endwin()
#			print res
#			exit(0)


	def monthPrompt(self,date):
		self.date = date
		self.monthly = Monthly(date)

		MonthHandler.drawMonth(self, date)
		pp = DayHandler.selectDay(self)
		print pp
		return pp


	def updateMonthInfo(self):
		# Month/year
		self.screen_info.addstr(1, 1, self.monthly.name, Draw.color_active())
		self.screen_info.addstr(2, 1, str(self.monthly.year), Draw.color_active())
		self.screen_info.refresh()


	def drawDaySelector(self):
		pos_x = self.cell_x_off
		pos_y = self.cell_y_off

		f=-1
		while f==-1:
			last_x = pos_x
			last_y = pos_y

			inp = Common.getInput(self.screen_main)
			if inp == 'a':pos_x -= self.cell_width
			elif inp == 's':pos_y += self.cell_height
			elif inp == 'd':pos_x += self.cell_width
			elif inp == 'w':pos_y -= self.cell_height
			elif inp == 'q':
				return pos_x, pos_y

			if pos_x < self.cell_x_off:	# Left of month
				pos_x=last_x
				return "prev"
			elif pos_x > (self.info_main.width - self.cell_width)+2: # Right of month
				pos_x=last_x
				return "next"

			if pos_y < self.cell_y_off:	# Up(prev) of month
				pos_y=last_y
				return "prev"
			elif pos_y > (self.cell_y_off 
				+ (self.cell_height*(self.monthly.nrows-1))): 
				# Down(next) of month
				pos_y=last_y
				return "next"

			Draw.rectangle(self.screen_main, last_y, last_x,
				last_y+self.cell_height, 
				last_x + self.cell_width)

			Draw.rectangle(self.screen_main, pos_y, pos_x,
				pos_y+self.cell_height, 
				pos_x + self.cell_width, 
				1, Draw.color_dom())

			self.screen_main.refresh()



try:
	height = int(sys.argv[1])
	width = int(sys.argv[2])

	panels = Screens(height, width)

#	while True:
#		curses.napms(2000)

	LifeMan(panels)
except KeyboardInterrupt:
	curses.endwin()
	exit(0)
