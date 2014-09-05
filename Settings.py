import curses

class Settings:

	dow_order = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
	dow_abrev_len = 3
	daily_logdir = '../dailies/'
	daily_logfmt = '%04d-%02d-%02d_log'
	daily_logext = 'txt'

	color_defaultbg = curses.COLOR_BLACK

	color_default = (curses.COLOR_WHITE, color_defaultbg)     # Default
	color_active  = (curses.COLOR_WHITE, curses.COLOR_BLUE)    # Active Selection
	color_today  =  (curses.COLOR_CYAN, color_defaultbg)      # Today
	color_dow    =  (curses.COLOR_CYAN, color_defaultbg)      # DOW
	color_dom    =  (curses.COLOR_YELLOW, curses.COLOR_BLUE)     # DOM
