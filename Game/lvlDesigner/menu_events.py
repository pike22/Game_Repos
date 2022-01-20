

class Menu_Events():
	"""
	Events for menu options that are spacific to here. Some Events for the menu are inside of the GUI_Events class
	"""
	def __init__(self, ):
		pass

	def New_File(self):
		"""
		Creates a new file to be edited for both maps, button loadouts or anything needed.
		"""
		filetypes = [(("TXT", "*.txt"), ("All Files", "*.*"))]
		file = filedialog.askopenfilename(title='Level Import', filetypes=filetypes, initialdir=self.__mapFiles)
		if file == '':
			print('No File Selected')
			return
		self.__newFile = open(file, 'w')
