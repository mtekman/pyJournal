
class Common:

	@staticmethod
	def getInput(screen):
		inp=ord('v')
		try:
			inp = screen.getch()
		except IOError:
			pass
		return chr(inp)


	@staticmethod
	def moveSelector(screen, pos_x, pos_y, x_amount, y_amount):
		inp = Common.getInput(screen)
		if inp == 'a':pos_x -= x_amount
		elif inp == 's':pos_y += y_amount
		elif inp == 'd':pos_x += x_amount
		elif inp == 'w':pos_y -= y_amount
		elif inp == ' ':return -1
		elif inp == 'p':return -2

		return pos_x, pos_y

