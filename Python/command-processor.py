import os # a module for os thingy
import re # regex

# every printed error message is pretty self explanatory, just read whats the cause of getting the error message
# just a bit lazy of explaining if its actually self explanatory

args = [] # command arguments
get_args = None # get arguments
max_cmd_args = 1024
cmdlist = ["exit","quit","help"] # list of commands

while True: # while loop ;\
	get_args = input("Command: ") # get args ?
	if not get_args: print("command is empty!") # if command is empty
	else:
		get_args.lower() # to lowercase
		args = re.split(" +",get_args) # split the arguments then put them on the list
		for i in range(len(get_args),max_cmd_args):
			args.insert(i,None)
		if(args[0] == "exit" or args[0] == "quit"): # command example for quit or exit
			break
		elif(args[0] == "help"): # -
			print("list of available commands:")
			for cmd in cmdlist:
				print('-'+cmd)
		elif(args[0] == "clear"): # clear console screen
			os.system('cls') # clear screen :\
		else: print("unknow command, see `help`") # if command is unknown
