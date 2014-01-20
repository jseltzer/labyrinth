"""
Labyrinth (C) 2014 by Josh Samson-Seltzer

Structure of save file:
Opening (0th) line = (width, height)
1st line = [(ID, x_cor, y_cor), (ID, x_cor, y_cor)]
2nd line = (skill_levels_tuple)
3rd line = [inventory_list]
4th line = [unlocked_items_list] #Note: custom save games don't have to include default unlocked_items

IDs:
0 = blank_tile
1 = player_tile
2 = lvl_tile



concerning save file {
	will store skills_levels + inventory + unlocked_items 
	the rest of the game will build itself dependent upon map/skill_levels/unlocked_items

	world decoder wont bother to check if two IDs allocated to same point
	(the latter will override)

	for the love of rms DO NOT put '\n' anywhere in the file you pleb
}

no substantial error checking, yet.
input assumed to always be well-formed

"""

"""Import and..."""

import random, os, pickle




"""File/Config Handling"""

def check_file_input(typo: int) -> str:
	"""Receive file string from user."""

	cases = {
		'y' : 1,
		'n' : 0,
	}

	if typo:
		print("It appears you didn't type 'y' or 'n'. Let's try again!\n")

	choice = input("Do you want to load your game from a file? [y/n] ")
	choice = cases[choice] if case_check(cases, choice) else check_file_input(1)
	return choice

def get_filename(typo: int) -> str:
	"""Return file object given string w/ location."""

	if typo:
		print("It appears you didn't enter a proper save file location. Please try again.\n")
	filename = input("Please input the location of your save file: ")
	return filename

def decode_file(filename: str) -> list:
	"""Load savefile using pickle."""

	file = open(filename, 'rb') if is_file(filename) else get_filename(1)
	wdata = pickle.load(file)
	file.close()
	return wdata

def encode_file(wdata: list, filename: str):
	"""Create/overwrite savefile using pickle."""
	#note: filename should have already been confirmed valid/existent (depending) at this point

	file = open(filename, 'wb')
	pickle.dump(wdata, file, protocol=pickle.HIGHEST_PROTOCOL)
	file.close()

	return wdata

def save_game(wdata, save):
	"""Dump wdata list into specified file."""

"""World Generation"""

def new_world() -> list:
	"""Construct a new world. (Outputs wdata similar to decode_file)"""

	width = 6
	height = 7

	wdata = [(width, height), {1:(3,4), 2:[(3,2),(2,3)]}, ((2,4,6), set([0,1,2]), set(range(15)))]

	return wdata

def populate_world(wdata: list) -> list:
	"""Construct and determine tiles of world.

	structure of return list:
	2d array
	"""

	dimensions = wdata[0]
	tiles = wdata[1]
	
	world = spawn_array(dimensions[0], dimensions[1])
	
	#iterate through and interpolate tiles

	for dict in tiles:
		pass
		# check if tile in unlocked_items

	return world


def spawn_array(width: int, height: int) -> list:
	"""Construct a 2d array from dimensions."""
	array = [[0] * width] * height
	return array


"""World Manipulation"""

def print_world(array: list):
	"""Print 2d array."""
	x = 'x'
	for row in array:
		print(row)

"""User Input"""
#not important

"""Status Declaration"""

def is_file(filename) -> bool:
	#i might want to implement actual code at some point
	#possibly
	return True if '.dat' in filename else False

def case_check(cases: dict or list, choice: str or int) -> bool:
	return True if choice in cases else False

"""(Nearly) Abstract Game Init Level"""

def break_game(crash_msg: str) -> bool:
	print("Labyrinth has crashed: {:s}.".format(crash_msg))

def init_game():
	"""
	try to avoid calling nested functions within init_game()
	to allow for easier module debugging: just use intermediate assignment
	"""


	"""Variable declarations"""

	default_unlocked_items = set(range(10))
	#define in default file?
	on = True
	game = on


	while True:
		"""Get user input"""
		if check_file_input(0):
			filename = get_filename(0)
			wdata = decode_file(filename)
		else:
			wdata = new_world()

		print(wdata)
		if wdata is not None:
			pass
#			world = populate_world(wdata)
		else:
			break_game("the save file is corrupted")
			break

		break


#	world = populate_world(wdata)
#	print_world(world)




"""Procedural"""


init_game()


"""End"""
