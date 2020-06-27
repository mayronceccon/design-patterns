from abc import ABC, abstractmethod
from maze_game import MazeGame
from maze import Room, Door


class Spell(ABC):
    @abstractmethod
    def spell(self):
        pass


class CastSpell(Spell):
    def spell(self):
        print("CastSpell")
        return super().spell()


# ConcreteProductEnchantedRoom
class EnchantedRoom(Room):
    def __init__(self, room_no, cast_spell: Spell):
        super().__init__(room_no)
        cast_spell.spell()


# ConcreteProductDoorNeedingSpell
class DoorNeedingSpell(Door):
    pass


# ConcreteCreatorEnchantedMazeGame
class EnchantedMazeGame(MazeGame):
    def make_door(self, room_1: Room, room_2: Room) -> Door:
        print("EnchantedMazeGame -> make_door -> DoorNeedingSpell")
        return DoorNeedingSpell(room_1, room_2)

    def make_room(self, n: int) -> Room:
        print("EnchantedMazeGame -> make_room -> EnchantedRoom")
        return EnchantedRoom(n, CastSpell())


if __name__ == "__main__":
    maze = EnchantedMazeGame().create_maze()
    print(maze)
    