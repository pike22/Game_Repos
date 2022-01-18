

class Menu_Events():
	def __init__(self, ):
		pass

	def New_File(self):
		filetypes = [(("TXT", "*.txt"), ("All Files", "*.*"))]
		file = filedialog.askopenfilename(title='Level Import', filetypes=filetypes, initialdir=self.__mapFiles)
		if file == '':
			print('No File Selected')
			return
		self.__newFile = open(file, 'w')
	
