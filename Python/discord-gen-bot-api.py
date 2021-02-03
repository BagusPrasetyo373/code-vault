import os

class Generator:
	def restock(accname,email,password):
		f = open(accname,"a+")
		if not f:
			f.close()
			f = open(accname,"x")
		f.write((email)+":"+str(password)+"\n")
		f.close()
	def gen(accname):
		f = open(accname,"r")
		if not f:
			f.close()
			# some error message
		lines = f.readlines()
		if not lines:
			f.close()
			# some error message
		f.close()
		to_ret = lines[0]
		del lines[0]
		f = open(accname,"w+")
		for line in lines:
			f.write(line)
		f.close()
		return to_ret
	def stock(accname):
		f = open(accname,"r")
		if not f:
			f.close()
			# some error message
		lines = f.readlines()
		f.close()
		count = 0
		for line in lines:
			count += 1
		return count
	def frestock(accname,filename):
		f = open(accname,"a+")
		if not f:
			f.close()
			f = open(accname,"x")
		f1 = open(filename,"r")
		if not f1:
			f1.close()
			# some error message
		for line in f1.readlines():
			f.write(line)
		f.close()
		f1.close()
	def flush(accname):
		f = open(accname,"a+")
		if not f:
			f.close()
			# some error message
		f.close()
		os.remove(accname)
		f = open(accname,"x")
		f.close()
