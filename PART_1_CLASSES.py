
#let us create a room or location class. we create a constructor which has 4 wall. we will open doors later
class Place:
    def  __init__(self,name):
        self.name=name
        self.description=''
        self.north="wall"
        self.south = "wall"
        self.east = "wall"
        self.west = "wall"
        self.pickups = [] # objects in the room

    def  __str__(self):
        return f' {self.name}'

    def room_objects(self): # we need to see and allocate room objects
        item_text=""
        if not self.pickups:
            return f'there is nothing in the {self.name}\n'
        else:
            for item in self.pickups:
                item_text+=f'{item}\t,'
            return f'in {self.name}, you see {item_text}\n'

    def addPickup(self,x):      #we need to initialize room with objects
        self.pickups.append(x)

    def removePickup(self,x):
        self.pickups.remove(x)
        return x

#END PLACE CLASS
#CREATE PLAYER CLASS
# after we create a class later we can add new feature to player dynamically. now player just walks and take things
class Player:
    def  __init__(self,name):
        self.name=name
        self.inventory=[] # what player has
        self.location=None

    def move(self,direction):
        #we need to secure player moves to north AND there is no wall so we need check both 
        if direction=="north" and self.location.north !="wall":
            self.location=self.location.north
            return f"Moved to the north. Current location: {self.location.name}\n"
            
        elif direction=="south" and self.location.south !="wall":
            self.location=self.location.south
            return f"Moved to the south. Current location: {self.location.name}\n"
            
        elif direction == "east" and self.location.east != "wall":
            self.location = self.location.east
            return f"Moved to the east. Current location: {self.location.name}\n"

        elif direction == "west" and self.location.west != "wall":
            self.location = self.location.west
            return f"Moved to the west. Current location: {self.location.name}\n"

        else:
            print('There is a wall in that direction. You cannot go that way')
            return'There is a wall in that direction. You cannot go that way'

    def take(self,item): #player takes item
        if item in self.location.pickups:
            self.inventory.append(self.location.removePickup(item))
            print('Picked up'+item)
        else:
            print ("that item is not here  !")

    def look_around(self):  #player look around
        print(self.location.room_objects())
        return f'{self.location.room_objects()}\n'

    def show_inventory(self):
        if not self.inventory:
            print (f'Player {self.name} inventory is empty\n')
            return f' {self.name} inventory is empty\n'
        else:
            inventory_text=""
            for index,item in enumerate(self.inventory):
                inventory_text+=f'{index}-{item}\n'
            print(f'Player {self.name} inventory\n{inventory_text}')
            return f'{self.name} inventory\n{inventory_text}\n\n'
            
            
#END OF PLAYER CLASS

#initialize the rooms. we can now create rooms with objects. later add monster too.

def create_place(name,description, pickups=None, north='wall',south='wall',east='wall',west='wall'):
    place=Place(name) # create an instance of place class.
    place.description=description
    place.north=north
    place.south=south
    place.east=east
    place.west=west

    #and objects
    if pickups is not None:
        for pickup in pickups:
            place.addPickup(pickup)

    return place

garden=create_place(
    "a garden",
    "a beatiful garden with flowers",
    pickups=['rose','grass','tulip']
    )
living_room=create_place(
    "a living room",
    "a fancy decorated living room",
    pickups=['glasses','ball']
    )

kitchen=create_place(
    "a kitchen",
    "an old style nice kitchen",
    pickups=['cup','bread','chicken']
    )

library=create_place(
    "a library",
    "a library with books",
    pickups=['book','binocular','globe','lenses']
    )

#connect whole rooms
    #LIVING ROOM MAPPING
living_room.north=garden
living_room.east=kitchen
living_room.west=library
    #GARDEN MAPPING
garden.south=living_room
    #KITCHEN MAPPING
kitchen.west=living_room
    #LIBRARY MAPPING
library.east=living_room 
