num = ['1','2','3','4','5','6','7','8','9','0']
alpnum = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
sym = ['`','~','!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}','\\','|',';',':','\'','"',',','<','.','>','/','?']
class _STR:
	def __init__(self,max_str_buffer):
		self.max_str_buffer = max_str_buffer
_STR.max_str_buffer = 4028
def strcmp(str1,str2,ignorecase=False):
	"""
		compare between 2 strings
		example:
				>>> strcmp('me','you')
				False

				>>> strcmp('Me','me')
				False

				>>> strcmp ('Me','me',True) # ignore cases
				True 
	"""
	ct = 0
	tmp = [[],[]]
	for s in str1:
		tmp[0].append(s)
	for s in str2:
		tmp[1].append(s)
	for i in range(_STR.max_str_buffer):
		try:
			if ignorecase == False:
				if tmp[0][i] == tmp[1][i]: ct += 1
			else:
				if tmp[0][i].lower() == tmp[1][i].lower(): ct += 1
		except: pass
	if ct == len(str1) or ct == len(str2): return True
	else: return False
def strmid(str,min,max):
	"""
		example:
				>>> strmid('mike hawk',0,4)
				mike
	"""
	tmp = list()
	ret = list()
	for s in str:
		tmp.append(s)
	for i in range(min,max):
		ret.append(tmp[i])
	return ''.join(ret)
def numeric(char):
	if len(char) > 1: return
	if char in num: return True
	else: return False
def symbol(char):
	if len(char) > 1: return
	if char in sym: return True
	else: return False
def alphanumeric(char):
	if len(char) > 1: return
	if char in alpnum: return True
	else: return False

class extr:
	"""
	Extract/Remove specific datatypes from string
	example:
			>>> extr.num('h1 my n4m3 i5 j05h')
			143505

			>>> extr.alpnum('h1 my n4m3 i5 j05h')
			h my nm i jh

			>>> extr.symb('https://github.com/HugeBrain16')
			://./

			>>> extr.symb_('https://github.com/HugeBrain16')
			httpsgithubcomHugeBrain16
	"""
	def num(str):
		c = int()
		tmp = list()
		for s in str:
			tmp.append(s)
		for i in range(len(tmp)):
			if not numeric(tmp[i]): tmp[i] = ''
		return ''.join(tmp)
	def alpnum(str):
		c = int()
		tmp = list()
		for s in str:
			tmp.append(s)
		for i in range(len(tmp)):
			if numeric(tmp[i]): tmp[i] = ''
		return ''.join(tmp)
	def alpnum_(str):
		c = int()
		tmp = list()
		for s in str:
			tmp.append(s)
		for i in range(len(tmp)):
			if not alphanumeric(tmp[i]): tmp[i] = ''
		return ''.join(tmp)
	def symb(str):
		c = int()
		tmp = list()
		for s in str:
			tmp.append(s)
		for i in range(len(tmp)):
			if not symbol(tmp[i]): tmp[i] = ''
		return ''.join(tmp)
	def symb_(str):
		c = int()
		tmp = list()
		for s in str:
			tmp.append(s)
		for i in range(len(tmp)):
			if symbol(tmp[i]): tmp[i] = ''
		return ''.join(tmp)
def strtok(string, key):
	"""
	
	example:
			>>> x = strtok('name=josh','name')
			=josh

			>>> x = strtok(x,'=')
			josh

	"""
	sm = int()
	ctr = -1
	keys = list()
	for k in key: keys.append(k)
	for s in string:
		ctr += 1
		if s != keys[ctr-len(keys)]: break
	if ctr == len(key): return strmid(string,ctr,len(string))
def sscanf(string, format, errmsg=None, delim=' '):
	"""

	return formated list from raw string
	example: 
			>>> sscanf('eat apple 10', 'ssi')
			['eat','apple',10]

			# //

			>>> sscanf('eat apple 10', 'ssi', errmsg=True) # this will print error messages if error occurred
			['eat','apple',10]

			>>> sscanf('eat-apple-10', 'ssi', delim='-') # custom delimiter
			['eat','apple',10]

	"""
	ctr = -1
	ctrr = int()
	ret = list()
	strf = string.split(delim)
	frc = 0
	for f in format: frc += 1
	if frc < len(strf):
		if errmsg: print(f'SSCANF_ValueError: string length is longer than the format')
		return
	elif frc > len(strf):
		if errmsg: print(f'SSCANF_ValueError: format length is longer than the string')
		return
	for f in format:
		ctr += 1
		if not f in ['s','f','x','i','d','c']:
				if errmsg: print(f'SSCANF_TypeError: Invalid data type for {f}')
		else:
			if f == 's':
				try:
					str(strf[ctr])
					ctrr += 1
					ret.append(str(strf[ctr]))
				except:
					if errmsg: print(f'SSCANF_TypeError: Invalid string `{strf[ctr]}` for datatype `{f}`')
			elif f == 'i':
				try:
					int(strf[ctr])
					ctrr += 1
					ret.append(int(strf[ctr]))
				except:
					if errmsg: print(f'SSCANF_TypeError: Invalid string `{strf[ctr]}` for datatype `{f}`')
			elif f == 'f':
				try:
					float(strf[ctr])
					ctrr += 1
					ret.append(float(strf[ctr]))
				except:
					if errmsg: print(f'SSCANF_TypeError: Invalid string `{strf[ctr]}` for datatype `{f}`')
			elif f == 'x':
				try:
					bool(strf[ctr])
					ctrr += 1
					ret.append(bool(strf[ctr]))
				except:
					if errmsg: print(f'SSCANF_TypeError: Invalid string `{strf[ctr]}` for datatype `{f}`')
			elif f == 'c':
				try:
					str(strf[ctr])
					if len(strf[ctr]) > 1:
						if errmsg: print(f'SSCANF_TypeError: Invalid string `{strf[ctr]}` for datatype `{f}`')
						return
					ctrr += 1
					ret.append(str(strf[ctr]))
				except:
					if errmsg: print(f'SSCANF_TypeError: Invalid string `{strf[ctr]}` for datatype `{f}`')
	if ctrr == frc: return ret

if __name__ == '__main__':
	pass
