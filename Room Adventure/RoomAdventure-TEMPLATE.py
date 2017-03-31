###########################################################################################
# Name:
# Date:
# Description:
###########################################################################################
from Tkinter import *

# the room class
# note that this class is fully implemented with dictionaries as illustrated in the lesson "More on Data Structures"
class Room(object):
	# the constructor
	def __init__(self, name, image):
		# rooms have a name, an image (the name of a file), exits (e.g., south), exit locations
		# (e.g., to the south is room n), items (e.g., table), item descriptions (for each item),
		# and grabbables (things that can be taken into inventory)
		self.name = name
		self.image = image
		self.exits ={}
		self.items = {}
		self.grabbables = []

	# getters and setters for the instance variables
	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, value):
		self._name = value

	@property
	def image(self):
		return self._image

	@image.setter
	def image(self, value):
		self._image = value

	@property
	def exits(self):
		return self._exits

	@exits.setter
	def exits(self, value):
		self._exits = value

	@property
	def items(self):
		return self._items

	@items.setter
	def items(self, value):
		self._items = value

	@property
	def grabbables(self):
		return self._grabbables

	@grabbables.setter
	def grabbables(self, value):
		self._grabbables = value

	# adds an exit to the room
	# the exit is a string (e.g., north)
	# the room is an instance of a room
	def addExit(self, exit, room):
		# append the exit and room to the appropriate dictionary
		self._exits[exit] = room

	# adds an item to the room
	# the item is a string (e.g., table)
	# the desc is a string that describes the item (e.g., it is made of wood)
	def addItem(self, item, desc):
		# append the item and description to the appropriate dictionary
		self._items[item] = desc

	# adds a grabbable item to the room
	# the item is a string (e.g., key)
	def addGrabbable(self, item):
		# append the item to the list
		self._grabbables.append(item)

	# removes a grabbable item from the room
	# the item is a string (e.g., key)
	def delGrabbable(self, item):
		# remove the item from the list
		self._grabbables.remove(item)

	# returns a string description of the room
	def __str__(self):
		# first, the room name
		s = "You are in {}.\n".format(self.name)

		# next, the items in the room
		s += "You see: "
		for item in self.items.keys():
			s += item + " "
		s += "\n"

		# next, the exits from the room
		s += "Exits: "
		for exit in self.exits.keys():
			s += exit + " "

		return s

# the game class
# inherits from the Frame class of Tkinter
class Game(Frame):
	# the constructor
	def __init__(self, parent):
		# call the constructor in the superclass
		Frame.__init__(self, parent)

	# creates the rooms
	def createRooms(self):

	# sets up the GUI
	def setupGUI(self):

	# sets the current room image
	def setRoomImage(self):

	# sets the status displayed on the right of the GUI
	def setStatus(self, status):

	# plays the game
	def play(self):
		# add the rooms to the game
		self.createRooms()
		# configure the GUI
		self.setupGUI()
		# set the current room
		self.setRoomImage()
		# set the current status
		self.setStatus("")

	# processes the player's input
	def process(self, event):

##########################################################
# the default size of the GUI is 800x600
WIDTH = 800
HEIGHT = 600

# create the window
window = Tk()
window.title("Room Adventure")

# create the GUI as a Tkinter canvas inside the window
g = Game(window)
# play the game
g.play()

# wait for the window to close
window.mainloop()
