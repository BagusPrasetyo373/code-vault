from array import * # array module

# list of character
charlist = [[]]

# character classes
class Character:
	def view(slot): # view character information by slot
		if(charlist[slot]): print(f"----------\nSlot: {slot}\nName: {charlist[slot][0]}\nAge: {charlist[slot][1]}\nDescription: {charlist[slot][2]}\n----------") # print character information from specified slot
		else: print("slot is empty") # if slot is empty

	def list(): # list of all character
		count = -1 # counter
		for i in charlist:
			try: # idky
				count += 1 # counter adds 1 on every list
				print(f"----------\nSlot: {count}\nName: {charlist[count][0]}\nAge: {charlist[count][1]}\nDescription: {charlist[count][2]}\n----------") # print all character inside the list
			except: pass # exception :/
		print(f"found {count} characters on the list") # msg

	def create(name,age,description): # create new character, autodetect empty slot
		count = -1 # counter
		for i in charlist:
			count += 1 # counter adds 1 on every list
			if(not charlist[count]): # if list/slot is empty
				charlist.insert(count,[name,age,description]) # insert character information array
				print(f"character has been created in slot {count}")
				break # break the loop

	def delete(slot): # delete character by slot
		if(not charlist[slot]): print("slot is empty") # if slot is empty
		else: # if slot is not empty
			del charlist[slot] # delete character information array
			print(f"character in slot {slot} has been deleted") # message

	def update(slot,name,age,description): # update character information by slot
		if(not charlist[slot]): print("slot is empty") # if slot is empty
		else: # if slot is not empty
			# update character information in speficied slot
			charlist[slot][0] = name
			charlist[slot][1] = age
			charlist[slot][2] = description
			print(f"character in slot {slot} has been updated") # message
