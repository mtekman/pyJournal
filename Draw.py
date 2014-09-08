#!/usr/bin/env python

import curses
import curses.ascii
from Settings import Settings
from TimeFuncs import TimeFns
from time import localtime

class Draw:

	screen = curses.initscr();
	curses.start_color()
	curses.curs_set(0)
	curses.noecho()

	curses.init_pair(1, Settings.color_default[0], Settings.color_default[1]) # Default
	curses.init_pair(2, Settings.color_active[0],  Settings.color_active[1])  # Active Selection
	curses.init_pair(3, Settings.color_today[0],  Settings.color_today[1])	  # Today
	curses.init_pair(4, Settings.color_dow[0],  Settings.color_dow[1])	  # Days of week
	curses.init_pair(5, Settings.color_dom[0],  Settings.color_dom[1])	  # Days of mon

	@staticmethod
	def color_default():return curses.color_pair(1)

	@staticmethod
	def color_active():return curses.color_pair(2)

	@staticmethod
	def color_today():return curses.color_pair(3)

	@staticmethod
	def color_dow():return curses.color_pair(4)

	@staticmethod
	def color_dom():return curses.color_pair(5)


	@staticmethod
	def rectangle(win, uly, ulx, lry, lrx, bg=1, pair=0):
	    """Draw a rectangle with corners at the provided upper-left
	    and lower-right coordinates.
	    """
	    if bg!=1:
			for y in xrange(1,lry-uly):
				win.addstr(uly+y,ulx, (" "*(lrx-ulx)), curses.color_pair(bg))


	    win.vline(uly+1, ulx, curses.ACS_VLINE, lry - uly - 1, curses.color_pair(pair))
	    win.hline(uly, ulx+1, curses.ACS_HLINE, lrx - ulx - 1, curses.color_pair(pair))
	    win.hline(lry, ulx+1, curses.ACS_HLINE, lrx - ulx - 1, curses.color_pair(pair))
	    win.vline(uly+1, lrx, curses.ACS_VLINE, lry - uly - 1, curses.color_pair(pair))
#	    win.addch(uly, ulx, curses.ACS_ULCORNER)
#	    win.addch(uly, lrx, curses.ACS_URCORNER)
#	    win.addch(lry, lrx, curses.ACS_LRCORNER)
#	    win.addch(lry, ulx, curses.ACS_LLCORNER)
	    win.addch(uly, ulx, '+', curses.color_pair(pair))
	    win.addch(uly, lrx, '+', curses.color_pair(pair))
	    win.addch(lry, lrx, '+', curses.color_pair(pair))
	    win.addch(lry, ulx, '+', curses.color_pair(pair))
