#!/usr/bin/env python

import sys
import curses, curses.ascii

from Settings import Settings
from Monthly import Monthly
from TimeFuncs import TimeFns
from Draw import Draw
from Screens import Screens

#from time import localtime
from datetime import date


class MonthHandler:

	@staticmethod
	def generalOpts(lman):
		lscreen = lman.screen_options

		lscreen.addstr(1,1, "Title")
		lscreen.addstr(3,1, "Mod1")
		lscreen.addstr(4,1, "Mod1")
		lscreen.addstr(5,1, "Mod1")

		lscreen.refresh()

	@staticmethod
	def addDaysOfWeek(lman):
		cell_x = lman.cell_x_off
		for dow in Settings.dow_order:
			lman.screen_main.addstr(0, cell_x + (lman.cell_width/2), 
				dow[0:Settings.dow_abrev_len], Draw.color_dow() )
			cell_x += lman.cell_width

		lman.screen_main.refresh()


	@staticmethod
	def drawMonth(lifeman, d):
		lifeman.reset(True,False,True)
		lifeman.updateMonthInfo()

		start_dow = lifeman.monthly.start_dow
		month_rows = lifeman.monthly.nrows

		today = date.today()
		dom = 99
		counting = False

		cell_y = lifeman.cell_y_off
		for y in xrange(month_rows):
			cell_x = lifeman.cell_x_off
			for x in xrange(len(Settings.dow_order)):

				if (lifeman.monthly.month,dom) == (today.month, today.day):
						Draw.rectangle(lifeman.screen_main, cell_y, cell_x,
							cell_y + lifeman.cell_height, cell_x + lifeman.cell_width, 
							Draw.color_today())

				else:
					Draw.rectangle(lifeman.screen_main, cell_y, cell_x, 
						cell_y + lifeman.cell_height, cell_x + lifeman.cell_width) #,
#						Draw.color_default())


				if not counting and x==start_dow:
					counting=True
					dom=1
				
				if counting:
					if dom <= lifeman.monthly.days:
						lifeman.screen_main.addstr(cell_y+1, cell_x+1, str(dom), Draw.color_dom())
						dom += 1
					else:
						counting = False



				cell_x += lifeman.cell_width
			cell_y += lifeman.cell_height

		lifeman.screen_main.refresh()

