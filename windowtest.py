# program = testcurses
import curses, sys
stdscr = curses.initscr()

height = int( sys.argv[1] )
width  = int( sys.argv[2] )

border = 0

left_win_x = width/3
top_win_y = 5

top_win_x = left_win_x
right_win_x = width - left_win_x
right_win_y = height
left_win_y = height - top_win_y

right_window = stdscr.subwin(right_win_y, right_win_x, 
	0, left_win_x)

left_window = stdscr.subwin(left_win_y, left_win_x, 
	top_win_y , 0)

top_window = stdscr.subwin(top_win_y, top_win_x, 0, 0)




right_window.box()
right_window.refresh()

left_window.box()
left_window.addstr(1,2,"General:")
left_window.addstr(4,3,"Reminders")	# Each general option creates a
left_window.addstr(5,3,"Ideas")		# directory for every unique idea
left_window.addstr(6,3,"Lists")		# or list (e.g. shopping)
left_window.refresh()

top_window.box()
top_window.addstr(1,2,"Sep 2014")
top_window.refresh()

#subtext = right_window.subwin(5, 10, 2, 10)
right_window.box()
right_window.refresh()
subtext = right_window.subwin(5, 5, 1, 1)

#subtext.addstr(0,0,"This is my") # line of text.\
# I can hold Calendar views, Daily views (logs,reminders),\
# and General view lists (reminders, ideas, lists) which are simply\
# folder managers ")

#right_window.addstr(4,20,"What happened? ")
right_window.refresh()

curses.napms(3000)
#mystr = right_window.instr(2,12,6)

curses.endwin()
