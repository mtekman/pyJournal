from Common import Common
from Draw import Draw

class OptsGeneral:

	def __init__(self, screen, info):

		self.opts = {"ideas":"Ideas", "rems":"Reminders", "lists":"Lists"}
		self.opts_maxlen = len(
			reduce(
				lambda x,y: x if len(x)>len(y) else y, 
				self.opts.values()
			))


		# General Opts
		self.screen = screen
		self.info = info

		self.line_off = 3
		self.line_gap = 1
		self.margin = 3

		self.OptsDraw()
		res = self.OptsSelector()

		curses.endwin()
		print res
		exit(0)


	def OptsSelector(self):

		pos_y = self.line_off
		pos_x = self.margin

		str_new = ""

		while True:
			res = Common.moveSelector(self.screen, 
				pos_x, pos_y, 0, self.line_gap)

			if res==-2:return res				# Switch window
			if res==-1:return str_new

			last_x = pos_x
			last_y = pos_y
			pos_x, pos_y = res

			str_old = self.screen.instr(last_y, last_x)
			str_new = self.screen.instr(pos_y, pos_x).strip()

			self.screen.addstr(last_y, last_x, str_old, Draw.color_default())
			self.screen.addstr(pos_y, pos_x, str_new, Draw.color_active())

			self.screen.refresh()



	def OptsDraw(self):
		line = self.line_off

		for optkey, val in self.opts.iteritems():
			self.screen.addstr(line, self.margin, val)
			line += self.line_gap

		self.screen.refresh()
