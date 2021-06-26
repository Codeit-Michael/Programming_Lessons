import os
class text_editor:
	def __init__(self):
		self.file = None

	def access_file(self,file_name):
		self.file = open(file_name,'r')
		content = self.file.read()
		print(content)
		self.file.close()

	def append_file(self,file_name,txt=None):
		if file_name in os.listdir():
			self.file = open(file_name,'a')
			content = self.file.write(f'\n{txt}')
			self.file.close()
		else:
			self.file = open(file_name,'a')
			self.file.close

	def overwrite_file(self,file_name,txt):
		self.file = open(file_name,'a')
		content = self.file.write(txt)
		self.file.close()


textbox = ("""agg""")

if __name__ == '__main__':
	f1 = text_editor()
	f1.append_file('untitled.txt',textbox)
	f1.access_file('untitled.txt')