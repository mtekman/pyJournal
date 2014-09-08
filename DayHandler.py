#!/usr/bin/env python

import sys
import curses, curses.ascii

from Settings import Settings
from Monthly import Monthly
from TimeFuncs import TimeFns
from Draw import Draw
from Screens import Screens

from time import localtime


class DayHandler:

	@staticmethod
	def drawDaySelector(lifeman):
		pos_x = lifeman.cell_x_off
		pos_y = lifeman.cell_y_off

		f=-1
		while f==-1:
			last_x = pos_x
			last_y = pos_y

			inp = lifeman.getInput()
			if inp == 'a':pos_x -= lifeman.cell_width
			elif inp == 's':pos_y += lifeman.cell_height
			elif inp == 'd':pos_x += lifeman.cell_width
			elif inp == 'w':pos_y -= lifeman.cell_height
			elif inp == 'q':
				return pos_x, pos_y

			if pos_x < lifeman.cell_x_off:	# Left of month
				pos_x=last_x
				return "prev"
			elif pos_x > (lifeman.info_main.width - lifeman.cell_width)+2: # Right of month
				pos_x=last_x
				return "next"

			if pos_y < lifeman.cell_y_off:	# Up(prev) of month
				pos_y=last_y
				return "prev"
			elif pos_y > (lifeman.cell_y_off 
				+ (lifeman.cell_height*(lifeman.monthly.nrows-1))): 
				# Down(next) of month
				pos_y=last_y
				return "next"

			Draw.rectangle(lifeman.screen_main, last_y, last_x,
				last_y+lifeman.cell_height, 
				last_x + lifeman.cell_width)

			Draw.rectangle(lifeman.screen_main, pos_y, pos_x,
				pos_y+lifeman.cell_height, 
				pos_x + lifeman.cell_width, 
				1, Draw.color_dom())

			lifeman.screen_main.refresh()

	@staticmethod
	def getDaySelect(lifeman, bx, by):
		dom = lifeman.screen_main.instr(by+1, bx+1,2)
		curses.endwin()
		print dom
		exit(0)

		try:
			return int(dom)
		except ValueError:
			pass
		
		if (by >= lifeman.height - (lifeman.cell_height + 5)) or (bx >= lifeman.width - (lifeman.cell_width + 5)):
			return "next"
		if by < lifeman.cell_height or  bx < lifeman.cell_width :
			return "prev"


	@staticmethod
	def selectDay(lifeman):
		bounds = DayHandler.drawDaySelector(lifeman)
		if len(bounds)!=2:return bounds

		bounds_x, bounds_y = bounds

		return DayHandler.getDaySelect(lifeman, bounds_x, bounds_y)
