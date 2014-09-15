import curses
from Common import Common
from Draw import Draw
from DirectoryHandler import DirectoryHandler


class OptsGeneral:

	def __init__(self, screen, info):

		self.opts = {
			"Ideas":["Ideas",[],[] ], 
			"Reminders":["Reminders",[],[] ],
			"Lists":["Lists",[],[] ],
		}


		# General Opts
		self.screen = screen
		self.info = info

		self.line_off = 3
		self.line_gap = 1
		self.margin = 3

		self.updateOpts( self.opts)	# Key, Contents

		user_sel = self.OptsSelector()

		if user_sel!=-2:		# Switch back to main otherwise
			direc = DirectoryHandler(user_sel).dir_tree
			self.opts[user_sel] = direc
			self.updateOpts( direc)	# Key, Contents

#		curses.endwin()
#		print res
#		exit(0)



	def	updateOpts( self, direc):

		self.opts_maxlen = len(
			reduce(
				lambda x,y: x if len(x)>len(y) else y, 
				direc.keys()
			))
		
		self.OptsDraw(direc)




	def OptsSelector(self):

		pos_y = self.line_off
		pos_x = self.margin

		str_new = ""

		while True:
			res = Common.moveSelector(self.screen, 
				pos_x, pos_y, 0, self.line_gap)

			if res==-2:return res				# Switch window
			if res==-1:return str_new			# 

			last_x = pos_x
			last_y = pos_y
			pos_x, pos_y = res

			str_old = self.screen.instr(last_y, last_x, self.opts_maxlen)
			str_new = self.screen.instr(pos_y, pos_x, self.opts_maxlen)

			if len(str_old) < self.opts_maxlen:
				str_old += ' '*(self.opts_maxlen - len(str_old))
			if len(str_new) < self.opts_maxlen:
				str_new += ' '*(self.opts_maxlen - len(str_new))

			self.screen.addstr(last_y, last_x, str_old, Draw.color_default())
			self.screen.addstr(pos_y, pos_x, str_new, Draw.color_active())

			self.screen.refresh()



	# Recursive Fn, prints contents of walk return map
	def OptsDraw(self, sublist, margin=0):
		line = self.line_off

#		sublist = list[:]	# clone list

		while len(sublist)!=0:

			item = sublist.keys()[0]
			try:
				root, dnames, fnames = sublist[item]
			except ValueError:
				curses.endwin()
				print sublist
				exit(-1)				

			if dnames:
				for d in dnames:
					self.OptsDraw( sublist[d], margin + 2 )
					sublist.remove(d)


			if fnames:
				for f in fnames:
					self.screen.addstr(line, self.margin + margin, f)
					line += self.line_gap

			sublist.remove(item)
		self.screen.refresh()
