import os
from Settings import Settings

class DirectoryHandler:
	
	def __init__(self, type):

		if not os.path.exists(Settings.general_notes_dir): 
			os.mkdir(Settings.general_notes_dir)


		self.type_dir = Settings.general_notes_dir+'/'+type
		if not os.path.exists(self.type_dir):
			os.mkdir(self.type_dir)

		self.dir_tree = self.listNotes()
		

	def listNotes(self):
		current_root = ""
		for root, direc, files in os.walk(self.type_dir):
			if curren


	def getNoteDir(self, name):
		name = self.type_dir + '/' + name

		if not os.direxists(name):
			os.mkdir(name)
		return name



	def addNote(self, name, note, text):
		dir = self.getNoteDir(name)
		fnote = dir + '/' + note

		f = open(fnote,'w')
		f.write(text)
		f.close()



	def readNote(self, name, note):
		dir = self.getNoteDir(name)
		fnote = dir + '/' + note
		
		if not os.path.exists(fnote):
			return -1

		f = open(fnote,'r')
		return f.readlines()

