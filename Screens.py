#!/usr/bin/env python

import curses

from Settings import Settings
from Draw import Draw


class Info:
	def __init__(self, h,w, offy, offx):
		self.height = h;  self.width = w
		self.offX = offx; self.offY = offy



class Panel:

	def clear(self):
		for y in xrange(1,self.info.height-1):	# Skip border
			self.screen.addstr(y,1, (' '*(self.info.width - 2)))


	def __init__(self, parent, h, w, offy, offx):
		self.parent = parent
		self.info = Info(h,w,offx,offy)
		self.screen = self.parent.subwin(h,w,offy,offx)
#		self.screen = self.parent.subpad(h,w,offy,offx)



class Screens:

	# Just Data to clear
	def clear(self, right=True, left=False, top=False):
		if right:self.right.clear()
		if left:self.left.clear() 
		if top:self.top.clear()
		

	# Full clean
	def initiate(self, right=True, left=True, top=True):

		if right:
			self.right.screen.clear()
			self.right.screen.box()
			self.right.screen.refresh(); 

		if left:
			self.left.screen.clear() 
			self.left.screen.box()
			self.left.screen.refresh(); 

		if top:
			self.top.screen.clear()
			self.top.screen.box()
			self.top.screen.refresh()



	def __init__(self, height, width):

		self.total_height = height
		self.total_width = width

		screen = Draw.screen

		topwin_h = int(height * Settings.panel_height_fract)
		if topwin_h < Settings.panel_height_min:
			topwin_h = Settings.panel_height_min

		leftwin_w = int(width * Settings.panel_width_fract )
		if leftwin_w < Settings.panel_width_min:
			leftwin_h = Settings.panel_width_min

		leftwin_h = height - topwin_h
		rightwin_h = height
		rightwin_w = width - leftwin_w;		
		topwin_w = leftwin_w;				

		leftwin_offx = 0;					leftwin_offy = topwin_h
		rightwin_offx = leftwin_w;			rightwin_offy = 0	# Keep aligned 
		topwin_offx = leftwin_offx;			topwin_offy = 0


		self.right = Panel(screen, rightwin_h, rightwin_w, 
			rightwin_offy, rightwin_offx)

		self.left = Panel(screen, leftwin_h, leftwin_w, 
			leftwin_offy, leftwin_offx)

		self.top = Panel(screen, topwin_h, topwin_w, 
			topwin_offy, topwin_offx)

		self.initiate()

