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

"""Classes"""

class Player():
	pass

class Game():
	def __init__(self, filename):
		self.filename = filename

	def build_wdata(self: 'Game', wdata: list) -> list:
		"""Generate gdata from wdata."""
		gdata = []
		return gdata


	def load_gdata(self: 'Game', gdata: list):
		"""Pass gdata to game."""
		pass


class World():
	pass

class Utility():
	pass

class File_Handler():
	def __init__(self):
		pass

		






"""File/Config Handling"""

def check_input(typo: int) -> str:
	"""Receive file string from user."""

	cases = {
		'l' : 0,
		'w' : 1,
		'r' : 2,
	}

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

def encode_game(world: list, gdata: list) -> list:
	wdata = encode_world(world)
	gdata[0] = wdata
	return gdata

def encode_world(world: list) -> list:
	""""Converts world array to wdata."""
	#implement!
	pass
	return wdata

def decode_game(gdata: list) -> list:
	"""Create world from game data."""

	wdata = gdata[0]
	world = decode_world(wdata)
	#check spawn ID's against unlocked_items
	return world

def decode_world(wdata: list) -> list:
	"""Convert wdata to world array."""
	pass

def load_file(filename: str) -> list:
	"""Load savefile using pickle."""

	file = open(filename, 'rb')
	gdata = pickle.load(file)
	file.close()
	return gdata

def save_file(gdata: list, world: list, filename: str) -> None:
	"""Create/overwrite savefile using pickle."""
	#note: filename should have already been confirmed valid/existent (depending) at this point

	wdata = encode_world(gdata)
	gdata[0] = wdata

	file = open(filename, 'wb')
	pickle.dump(gdata, file, protocol=pickle.HIGHEST_PROTOCOL)
	file.close()

"""World Generation"""

def gen_world(config: list) -> list:
	"""Generate a new world, return gdata.
	config determined by user input and/or random and/or default values."""


#make sure stuff is in unlocked_items
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

def gen_game(wdata: list) -> list:
	"""Given generated world/world instructions, construct gdata."""

	gdata = []
	return gdata


def populate_world(wdata: list) -> list:
	"""Determine spawns and construct 2d array of world."""

	dimensions = wdata[0]
	spawns = wdata[1]
	
	world = create_array(dimensions[0], dimensions[1])
	
	world = inject_spawns(world, spawns)

	return world

def inject_spawns(world: list, spawns: dict or list) -> list:
	"""This could be better off as recursive, but assuming only 1 later of depth (as should be), all is well."""
	#iterate through and interpolate spawns

	for id in spawns:
		if isinstance(spawns[id], tuple):
			cors = spawns[id]
			world[cors[0]][cors[1]] = id
		else:
			for tup in spawns[id]:
				cors = tup
				world[cors[0]][cors[1]] = id

		# check if spawn ID in unlocked_items
	return world


def create_array(width:int, height:int) -> list:
	"""Construct a 2d array from dimensions."""
	array = [[0 for i in range(width)] for i in range(height)]
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

	while True:
		"""Init loop."""

		choice = check_input(0)

		if not choice:
			"""Load gdata and decode from savefile."""
			filename = get_filename(0)
			gdata = load_file(filename)
			world = decode_game(gdata)
		elif choice == 1:
			"""Generate gdata and decode."""
			#uhoh
			print('gen')
			#involve config somehow
			gdata = gen_world()
		else:
			"""Generate random gdata and decode."""
			#uhoh
			print('randgen')
			gdata = gen_world()

		if gdata is not None:
			wdata = gdata[:2]
			world = populate_world(wdata)
		else:
			break_game("the save file is corrupted")
			break
			#fix error handling for pickle
		print_world(world)

		#while True:
		"""User input loop."""



"""Procedural"""


init_game()


"""End"""
