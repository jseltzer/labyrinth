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
		print("It appears you didn't type [l/w/r]. Let's try again!\n")

	choice = input("Do you want to load a savefile [l], generate a new world [w], or create a random one [r]?  [l/w/r] ")
	choice = cases[choice] if in_case(cases, choice) else check_input(1)
	return choice

def get_filename(typo: int) -> str:
	"""Return file object given string w/ location."""

	if typo:
		print("It appears you didn't enter a proper save file location. Please try again.\n")
	
	filename = input("Please input the location of your save file: ")

	if is_file(filename):
		return filename
	else:
		return get_filename(1)

def encode_world(world: list, gdata) -> list:
	""""Pushes world to gdata[0]."""
	pass

def decode_world(gdata: list) -> list:
	"""Pushes gdata onto world."""
	pass

def load_file(filename: str) -> list:
	"""Load savefile using pickle."""

	file = open(filename, 'rb')
	gdata = pickle.load(file)
	file.close()
	return gdata

def save_file(gdata: list, filename: str) -> None:
	"""Create/overwrite savefile using pickle."""
	#note: filename should have already been confirmed valid/existent (depending) at this point

	file = open(filename, 'wb')
	pickle.dump(gdata, file, protocol=pickle.HIGHEST_PROTOCOL)
	file.close()

"""World Generation"""

def gen_world(config: list) -> list:
	"""Generate a new world, return gdata.
	config determined by user input and/or random and/or default values."""

	if not user_input:
		#generate random
		pass
	else:
		#generate based on user_input
		pass
#temp stuff vvv
	width = 6
	height = 7

	gdata = [(width, height), {1:(3,4), 2:[(3,2),(2,3)]}, ((2,4,6), set([0,1,2]), set(range(15)))]

	return gdata

def populate_world(gdata: list) -> list:
	"""Determine spawns and construct 2d array of world."""

	dimensions = gdata[0]
	spawns = gdata[1]
	
	world = create_array(dimensions[0], dimensions[1])
	
	world = inject_spawns(world, spawns)

	return world

def inject_spawns(world: list, spawns: dict or list) -> list:
	"""This could be better off as recursive, but assuming only 1 later of depth (as should be), all is well."""
	#iterate through and interpolate spawns

	print(spawns)
	for id in spawns:
		if isinstance(spawns[id], tuple):
			cors = spawns[id]
			world[cors[0]][cors[1]] = id
		else:
			for tup in spawns[id]:
				cors = tup
				world[cors[0]][cors[1]] = id
				print([cors[0],cors[1]])

		# check if spawn ID in unlocked_items
	return world


def create_array(width:int, height:int) -> list:
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

def in_bounds(dimensions: tuple, obj) -> bool:
	pass

def is_file(filename: str) -> bool:
	#i might want to implement actual code at some point
	#possibly
	if 'dat' in filename:
		return True
	else:
		return False

def in_case(cases: dict or list, choice: str or int) -> bool:
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
			gdata = load_file(filename)
		elif choice == 1:
			"""Generate gdata."""
			print('gen')
			gdata = gen_world(1)
		else:
			"""Generate random gdata."""
			print('randgen')
			gdata = gen_world(0)

		if gdata is not None:
			world = populate_world(gdata)
		else:
			break_game("the save file is corrupted")
			break
			#fix error handling for pickle
		print(world)
#		print_world(world)
		break






"""Procedural"""


init_game()


"""End"""
