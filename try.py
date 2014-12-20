#!/usr/bin/env python

import sys
import curses

screen = curses.initscr()
curses.start_color()

curses.init_pair(1,curses.COLOR_RED, curses.COLOR_WHITE)

screen.addstr(9,9,"smoke", curses.color_pair(1))

screen.refresh()
curses.napms(2000)

res = screen.getch()
curses.endwin()
print (res, chr(res))

exit(0)


