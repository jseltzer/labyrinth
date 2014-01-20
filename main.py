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

"""File/Config Handling"""

def want_file_input(typo: int) -> str:
	"""Receive file string from user."""

	cases = {
		'y' : 1,
		'n' : 0,
	}

	if typo:
		print("It appears you didn't type 'y' or 'n'. Let's try again!\n")

	choice = input("Do you want to load your game from a file? [y/n] ")

	choice = cases[choice] if case_check(cases, choice) else want_file_input(1)

	return choice

def get_file_input(typo: int) -> 'file':
	"""Return file object given string w/ location."""

	if typo: print("It appears you didn't enter a proper save file location. Please try again.\n")

	location = input("Please input the location of your save file: ")

	file = open(location, 'r') if is_file(location) else get_file_input(1)

	return file

def decode_file(file: str) -> list:
	"""Construct config command from file input.

	structure of return list:
	[(width, height), [(id, x_cor, y_cor), (id, x_cor, y_cor)], [(skills_levels_list), set([inventory_list]), set([unlocked_items_list)]
	/// window_size \\\///			spawns		\\\///		player/game stats			\\\
	1 dict per item 
	"""

	config = []

	file_obj = file.read()
	file.close()
	file = file_obj


	#REDO PARSER

	#DO NOT check if the points make sense here

	return config


def encode_file():
	"""Mirrors decode_file
	turns map/items/stats into config list
	"""
	return config

def save_game(config, save):
	"""Dump config list into specified file."""

"""World Generation"""

def new_world() -> list:
	"""Construct a new world. (Outputs config similar to decode_file)"""
	pass


def populate_world(config: list) -> list:
	"""Construct and determine tiles of world.

	structure of return list:
	2d array
	"""

	dimensions = config[0]
	tiles = config[1]
	
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

def is_file(file) -> bool:
	#i might want to implement actual code at some point
	#possibly
	return True if ('.lab' or '.world') in file else False

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
	on = True
	game = on


	while True:
		if want_file_input(0):
			file = get_file_input(0)
			config = decode_file(file)
		else:
			config = new_world()

		if config is not None:
			pass
#			world = populate_world(config)
		else:
			break_game("the save file is corrupted")
			break

		break

	#file is opened in get_file_input and closed in decode_file - potential issue?


#	world = populate_world(config)
#	print_world(world)




"""Procedural"""


init_game()


"""End"""
