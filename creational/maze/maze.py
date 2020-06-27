from enum import Enum
from abc import ABC, abstractmethod


class Direction(Enum):
    NORTH = 'north'
    SOUTH = 'south'
    EAST = 'east'
    WEST = 'west'

# Product
class MapSite(ABC):
    @abstractmethod
    def enter(self):
        pass


# ConcreteProduct
class Room(MapSite):
    def __init__(self, room_no: int):
        self.__room_no = room_no
        self.__side = {}

    def enter(self):
        return super().enter()

    def get_side(self, direction: Direction):
        return self.__side[direction]
    
    def set_side(self, direction: Direction, map_site: MapSite):
        self.__side[direction] = map_site


# ConcreteProduct
class Wall(MapSite):
    def enter(self):
        return super().enter()


# ConcreteProduct
class Door(MapSite):
    def __init__(self, room_1: Room, room_2: Room):
        self.__room_1 = room_1
        self.__room_2 = room_2
        self.__is_open = False

    def enter(self):
        return super().enter()

    def other_side_from(self, room: Room):
        pass


class Maze:
    def __init__(self):
        self.__rooms = []

    def add_room(self, room: Room):
        self.__rooms.append(room)

    def room_no(self, room_no: int):
        pass
