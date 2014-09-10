import curses

class Settings:

	dow_order = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
	dow_abrev_len = 3
	mon_abrev_len = 0
	daily_logdir = '../dailies/'
	daily_logfmt = '%04d-%02d-%02d_log'
	daily_logext = 'txt'

	color_defaultbg = curses.COLOR_BLACK

	color_default = (curses.COLOR_WHITE, color_defaultbg)     # Default
	color_active  = (curses.COLOR_WHITE, curses.COLOR_BLUE)    # Active Selection
	color_today  =  (curses.COLOR_CYAN, color_defaultbg)      # Today
	color_dow    =  (curses.COLOR_GREEN, color_defaultbg)      # DOW
	color_dom    =  (curses.COLOR_YELLOW, curses.COLOR_BLUE)     # DOM

	panel_width_fract = 0.3
	panel_height_fract = 0.2

	panel_width_min = 10
	panel_height_min = 4

	general_notes_dir = '/home/user/MyDocs/Notes/'
