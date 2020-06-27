from maze_game import MazeGame
from maze import Room, Wall


# ConcreteProductRoomWithABomb
class RoomWithABomb(Room):
    pass


# ConcreteProductBombedWall
class BombedWall(Wall):
    pass


# ConcreteCreatorBombedMazeGame
class BombedMazeGame(MazeGame):
    def make_wall(self) -> Wall:
        print("BombedMazeGame -> make_wall -> BombedWall")
        return BombedWall()

    def make_room(self, n: int) -> Room:
        print("BombedMazeGame -> make_room -> RoomWithABomb")
        return RoomWithABomb(n)


if __name__ == "__main__":
    maze = BombedMazeGame().create_maze()
    print(maze)
    