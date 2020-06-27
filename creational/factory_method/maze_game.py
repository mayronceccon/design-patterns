from maze import Maze, Direction, Room, Wall, Door


# CreatorMazeGame
class MazeGame:
    def create_maze(self) -> Maze:
        maze = self.make_maze()

        room_1 = self.make_room(1)
        room_2 = self.make_room(2)

        door = self.make_door(room_1, room_2)

        room_1.set_side(Direction.NORTH, self.make_wall())
        room_1.set_side(Direction.EAST, door)
        room_1.set_side(Direction.SOUTH, self.make_wall())
        room_1.set_side(Direction.WEST, self.make_wall())

        room_2.set_side(Direction.NORTH, self.make_wall())
        room_2.set_side(Direction.EAST, self.make_wall())
        room_2.set_side(Direction.SOUTH, self.make_wall())
        room_2.set_side(Direction.WEST, door)

        maze.add_room(room_1)
        maze.add_room(room_2)

        return maze

    # factory method
    def make_maze(self) -> Maze:
        print("MazeGame -> make_maze -> Maze")
        return Maze()

    # factory method
    def make_room(self, n: int) -> Room:
        print("MazeGame -> make_room -> Room")
        return Room(n)

    # factory method
    def make_wall(self) -> Wall:
        print("MazeGame -> make_wall -> Wall")
        return Wall()

    # factory method
    def make_door(self, room_1: Room, room_2: Room) -> Door:
        print("MazeGame -> make_door -> Door")
        return Door(room_1, room_2)


if __name__ == "__main__":
    maze = MazeGame().create_maze()
    print(maze)