###########################################################################################
# Name: Alex Reed, Christopher Smith, Jonathan Frank
# Date: 3/30/17
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
                # r1 through r4 are the four rooms in the mansion
                # currentRoom is the room the player is currently in (which
                # can be one of r1 through r4)
                # create the rooms and give them meaningful names and an
                # image in the current directory
                r1 = Room("Room 1", "room1.gif")
                r2 = Room("Room 2", "room2.gif")
                r3 = Room("Room 3", "room3.gif")
                r4 = Room("Room 4", "room4.gif")
                r5= Room("Room 5", "room5.gif")
                r6 = Room("Room 6", "room6.gif")
                r7 = Room("Room 7", "room7.gif")
                

                # add exits to room 1
                r1.addExit("east", r2) # to the east of room 1 is room 2
                r1.addExit("south", r3)
                r1.addGrabbable("key")#Adding the key to Room 1

                #Adding the furniture
                r1.addItem("ladder", "A ladder leading straight up into the ceiling. \
  Light seems to be pouring down from the top.")
                r1.addItem("chair", "It is made of rich mahogany and, as you may have suspected,\
 no one is sitting on it.")
                r1.addItem("table", "It is made of oak and is covered in an array of\
 scattered papers and maps.Underneath the mess, you can see a golden key.")

                # add exits to room 2
                r2.addExit("west", r1)
                r2.addExit("south", r4)
                r2.addItem("rug", "It is what might be expected of a rug in a mysterious mansion:\
 ancient, dusty, and bearing a mysterious stain which slightly resembles Zack Galafanakis")
                r2.addItem("fireplace", "A half-scorched log lies in under the mantle, it looks as \
if it was put out in a hurry.")
                r2.addItem("door", "It is a door")

                # add exits to room 3
                r3.addExit("north", r1)
                r3.addExit("east", r4)
                # add grabbables to room 3
                r3.addGrabbable("book")

                r3.addItem("bookshelves", "The shelves are stocked full of books, all without titles. \
Upon further inspection, you find that all of the books' pages are riddled with symbols \
you cannot identify. This seems like a mystery to solve when you aren't trapped in a room.")
                r3.addItem("statue", "The statue, which stands directly in the southwest corner of the \
room at about 6ft tall, appears to be a woman. Although it seems that she is meant to be portrayed in beauty, \
her face seems very distorted; her hollow eyes seem to be tracing you around the room.")
                r3.addItem("desk", "This desk, unlike most areas of the house, is exceptionally clean. \
There rests on it only a single piece of paper. It reads 'I'm so sorry {}, if that's even your real name. I never meant for it \
to be like this. It was you or me, and I have a family to look after. I left you a little present in the cabinet to make things \
a little easier on you. Consider it our last Coup de Gras.'")

                # add exits to room 4
                r4.addExit("north", r2)
                r4.addExit("west", r3)
                r4.addExit("south", None) # DEATH!
                # add grabbables to room 4
                r4.addGrabbable("bottle")

                r4.addItem("window", "Through the south-facing window, you can see the sun setting quickly over the \
horizon. Forest is the only thing in sight for miles. \
The window is open, and you appear to be very high from the ground.")
                r4.addItem("cabinet", "A glass cabinet lies half open, revealing its only \
contents to be a half finished bottle of dark, unmarked liquid")

                r5.addExit("down", r1)  
                r5.addGrabbable("bat")
                r5.addItem("mannequins", "A number of mannequins are scattered within the attic. All of them donning tattered \
 women's clothing and old wigs, some of them even sport crudely-applied make-up. They are all facing the entrance, leaving you feeling \
 very unsettled. A wooden baseball bat lies in the hands of the closest 'woman.'")

                r6.addExit("south", r2)
                r6.addExit("downstairs", r7)

                r6.addItem("stairs", "The stairs lead down to a door. There is no other exit except the way in which you came.")

                # set room 1 as the current room at the beginning of the
                # game
                Game.currentRoom = r1
                # initialize the player's inventory
                Game.inventory = []

        # sets up the GUI
        def setupGUI(self):
                # organize the GUI
                self.pack(fill=BOTH, expand=1)

                # setup the player input at the bottom of the GUI
                # the widget is a Tkinter Entry
                # set its background to white and bind the return key to the
                # function process in the class
                # push it to the bottom of the GUI and let it fill
                # horizontally
                # give it focus so the player doesn't have to click on it
                Game.player_input = Entry(self, bg="white")
                Game.player_input.bind("<Return>", self.process)
                Game.player_input.pack(side=BOTTOM, fill=X)
                Game.player_input.focus()

                # setup the image to the left of the GUI
                # the widget is a Tkinter Label
                # don't let the image control the widget's size
                img = None
                Game.image = Label(self, width=WIDTH / 2, image=img)
                Game.image.image = img
                Game.image.pack(side=LEFT, fill=Y)
                Game.image.pack_propagate(False)

                # setup the text to the right of the GUI
                # first, the frame in which the text will be placed
                text_frame = Frame(self, width=WIDTH / 2)
                # the widget is a Tkinter Text
                # disable it by default
                # don't let the widget control the frame's size
                Game.text = Text(text_frame, bg="lightgrey", state=DISABLED)
                Game.text.pack(fill=Y, expand=1)
                text_frame.pack(side=RIGHT, fill=Y)
                text_frame.pack_propagate(False)

        # sets the current room image
        def setRoomImage(self):
                if (Game.currentRoom == None):
                        # if dead, set the skull image
                        Game.img = PhotoImage(file="skull.gif")

                else:
                        # otherwise grab the image for the current room
                        Game.img = PhotoImage(file=Game.currentRoom.image)

                # display the image on the left of the GUI
                Game.image.config(image=Game.img)
                Game.image.image = Game.img

        # sets the status displayed on the right of the GUI
        def setStatus(self, status):
                # enable the text widget, clear it, set it, and disabled it
                Game.text.config(state=NORMAL)
                Game.text.delete("1.0", END)
                if (Game.currentRoom == None):
                        # if dead, let the player know
                        Game.text.insert(END, "You are dead.  The only thing you can do now is quit.\n")

                else:
                        # otherwise, display the appropriate status
                        Game.text.insert(END, str(Game.currentRoom) +\
                                         "\nYou are carrying: " + str(Game.inventory) +\
                                         "\n\n" +  status)
                Game.text.config(state=DISABLED)


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
                # grab the player's input from the input at the bottom of
                # the GUI
                action = Game.player_input.get()
                # set the user's input to lowercase to make it easier to
                # compare the verb and noun to known values action = action.lower()
                # set a default response
                response = "I don't understand.  Try verb noun.  Valid verbs are go, look, and take"

                # exit the game if the player wants to leave (supports quit,
                # exit, and bye)
                if (action == "quit" or action == "exit" or action == "bye"\
                    or action == "sionara!"): exit(0)

                # if the player is dead if goes/went south from room 4
                if (Game.currentRoom == None):
                        # clear the player's input
                        Game.player_input.delete(0, END)
                        return

                # split the user input into words (words are separated by
                # spaces) and store the words in a list
                words = action.split()

                # the game only understands two word inputs
                if (len(words) == 2):
                        # isolate the verb and noun
                        verb = words[0]
                        noun = words[1]

                        # the verb is: go
                        if (verb == "go"):
                                # set a default response
                                response = "Invalid exit."

                                # check for valid exits in the current room
                                if (noun in Game.currentRoom.exits):
                                        # if one is found, change the current room to
                                        # the one that is associated with the
                                        # specified exit
                                        Game.currentRoom = Game.currentRoom.exits[noun]
                                        # set the response (success)
                                        response = "Room changed."

                                # the verb is: look
                        elif (verb == "look"):
                                # set a default response
                                response = "I don't see that item."
                                # check for valid items in the current room
                                if (noun in Game.currentRoom.items):
                                        # if one is found, set the response to the
                                        # item's description
                                        response = Game.currentRoom.items[noun]

                        # the verb is: take
                        elif (verb == "take"):
                                # set a default response
                                response = "I don't see that item."
                                # check for valid grabbable items in the current
                                # room
                                for grabbable in Game.currentRoom.grabbables:
                                        # a valid grabbable item is found
                                        if (noun == grabbable):
                                                # add the grabbable item to the player's
                                                # inventory
                                                Game.inventory.append(grabbable)
                                                # remove the grabbable item from the
                                                # room
                                                Game.currentRoom.delGrabbable(grabbable)
                                                # set the response (success)
                                                response = "Item grabbed."
                                                # no need to check any more grabbable
                                                # items
                                                break


                # display the response on the right of the GUI
                # display the room's image on the left of the GUI
                # clear the player's input
                self.setStatus(response)
                self.setRoomImage()
                Game.player_input.delete(0, END)
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
