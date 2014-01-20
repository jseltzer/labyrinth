"""
Labyrinth (C) 2014 by Josh Samson-Seltzer

IDs:
0 = blank_tile
1 = player_tile
2 = lvl_tile

no substantial error checking, yet.
input assumed to always be well-formed

"""

"""Import and..."""

import random, os, pickle




"""File/Config Handling"""

def check_input(typo: int) -> str:
	"""Receive file string from user."""

	cases = {
		'l' : 0,
		'w' : 1,
		'r' : 2,
	}

	print("youre running check_input")

	if typo:
		print("It appears you didn't type 'y' or 'n'. Let's try again!\n")

	choice = input("Do you want to load a savefile [l], generate a new world [w], or create a random one [r]?  [l/w/r] ")
	choice = cases[choice] if case_check(cases, choice) else check_input(1)
	return choice

def get_filename(typo: int) -> str:
	"""Return file object given string w/ location."""

	if typo:
		print("It appears you didn't enter a proper save file location. Please try again.\n")
	filename = input("Please input the location of your save file: ")
	return filename

def encode_world(world: list) -> list:
	pass

def decode_world(wdata: list) -> list:
	pass

def load_file(filename: str) -> list:
	"""Load savefile using pickle."""

	file = open(filename, 'rb') if is_file(filename) else get_filename(1)
	wdata = pickle.load(file)
	file.close()
	return wdata

def save_file(wdata: list, filename: str):
	"""Create/overwrite savefile using pickle."""
	#note: filename should have already been confirmed valid/existent (depending) at this point

	file = open(filename, 'wb')
	pickle.dump(wdata, file, protocol=pickle.HIGHEST_PROTOCOL)
	file.close()

	return wdata

"""World Generation"""

def gen_world(user_input) -> list:
	"""Generate a new world, return wdata."""

	if not user_input:
		#generate random
		pass
	else:
		#generate based on user_input
		pass
#temp stuff vvv
	width = 6
	height = 7

	wdata = [(width, height), {1:(3,4), 2:[(3,2),(2,3)]}, ((2,4,6), set([0,1,2]), set(range(15)))]

	return wdata

def populate_world(wdata: list) -> list:
	"""Determine spawns and construct 2d array of world."""

	dimensions = wdata[0]
	spawns = wdata[1]
	
	world = spawn_array(dimensions[0], dimensions[1])
	
	world = inject_spawns(world, spawns)


def inject_spawns(world: list, spawns: dict or list) -> list:

	#iterate through and interpolate spawns

	for id in spawns:
		i = 0
		if type(spawns) == dict:
			coors = spawns[id]
		else:
			coors = spawns[i]

		i += 1

		if type(coors) == tuple:
			print(coors)
			x, y = coors[0], coors[1]
			world[x][y] = id
			print(type(world))
		else:
			inject_spawns(world, coors)

		# check if spawn ID in unlocked_items
	print(world)
	return world


def spawn_array(width:int, height:int) -> list:
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

def check_in_bounds(dimensions: tuple, obj) -> bool:
	pass

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
	#define in default file
	on = True
	game = on


	while True:
		"""Get user input"""
		choice = check_input(0)

		if not choice:
			"""Load savefile"""
			filename = get_filename(0)
			wdata = load_file(filename)
		elif choice == 1:
			print('gen')
			#generate
			wdata = gen_world(1)
		else:
			print('randgen')
			#randgen
			wdata = gen_world(0)

		if wdata is not None:
			world = populate_world(wdata)
		else:
			break_game("the save file is corrupted")
			break
			#fix error handling for pickle

		print_world(world)
		break






"""Procedural"""


init_game()


"""End"""
