from iniparser import * # https://github.com/HugeBrain16/iniparser/

inventory = []
max_slot = 8
file = 'inventory.ini'

class Inventory:
	def ret_empty_slot():
		counter = -1
		for slot in inventory:
			counter += 1
			if not slot: return counter
		return counter

	def ret_item(slot):
		return inventory[slot]

	def ret_list_item(min,max):
		ret = []
		for i in range(min,max):
			if inventory[i] == None: ret.insert(i,None)
			else: ret.insert(i,inventory[i])
		return ret

	def clear_slot(slot):
		inventory[slot] = None

	def put_item(slot, item):
		inventory[slot] = item

	def put_list_item(item: list):
		item_len = len(item)
		for i in range(max_slot):
			if i < item_len:
				inventory[i] = item[i]
			else: continue

	def clear():
		for i in range(max_slot):
			inventory[i] = None

	def save():
		counter = -1
		if(ini_exists(file) < 1): ini_create(file)
		for slot in inventory:
			counter += 1
			ini_set(file,f'slot{counter}',slot)

	def load():
		if(ini_exists(file) < 1): ini_create(file)
		for i in range(max_slot):
			inventory[i] = ini_get(file,f'slot{i}')

	def reset_database():
		if(ini_exists(file) < 1): ini_create(file)
		for i in range(max_slot):
			if(ini_isset(file,f'slot{i}')): ini_unset(file,f'slot{i}')

	def refresh_database():
		temp = []
		for i in range(max_slot):
			temp.insert(i,inventory[i])
		Inventory.load()
		Inventory.save()
		for i in range(max_slot):
			inventory[i] = temp[i]

	def refresh():
		temp = []
		for i in range(max_slot):
			temp.insert(i,inventory[i])
		for i in range(max_slot):
			inventory[i] = temp[i]

	def sort():
		temp = sorted(inventory)
		for i in range(max_slot):
			inventory[i] = temp[i]

	def init():
		for i in range(max_slot):
			inventory.insert(i,None)

# init API
Inventory.init()
