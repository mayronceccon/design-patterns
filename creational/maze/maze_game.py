from maze import Maze, Room, Door, Direction, Wall


class MazeGame:
    def create_maze(self) -> Maze:
        maze = Maze()

        room_1 = Room(1)
        room_2 = Room(2)

        door = Door(room_1, room_2)

        room_1.set_side(Direction.NORTH, Wall())
        room_1.set_side(Direction.EAST, door)
        room_1.set_side(Direction.SOUTH, Wall())
        room_1.set_side(Direction.WEST, Wall())

        room_2.set_side(Direction.NORTH, Wall())
        room_2.set_side(Direction.EAST, Wall())
        room_2.set_side(Direction.SOUTH, Wall())
        room_2.set_side(Direction.WEST, door)

        maze.add_room(room_1)
        maze.add_room(room_2)

        return maze


if __name__ == "__main__":
    maze = MazeGame().create_maze()
    print(maze)