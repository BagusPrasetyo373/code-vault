class Clipboard:
	def __init__(self,text):
		self.text = text
	def copy(text):
		if text:
			if(not isinstance(text, list) or not isinstance(text, tuple) or not isinstance(text, dict)):
				text_tmp = text
				
				# data types
				if(isinstance(text, str)): str(text_tmp)
				elif(isinstance(text, int)): int(text_tmp)
				elif(isinstance(text, bool)): bool(text_tmp)
				elif(isinstance(text, float)): bool(text_tmp)

				Clipboard.text = text_tmp
	def paste():
		if Clipboard.text:
			return Clipboard.text
	def clear():
		if Clipboard.text:
			Clipboard.text = None
