import turtle


PART_OF_PATH = 'O'
TRIED = '.'
OBSTACLE = '+'
DEAD_END = '-'


class Maze:
    def __init__(self, maze_file):
        maze_rows = 0
        maze_cols = 0
        self.mazelist = []
        with open(maze_file) as maze:
            for line in maze:
                col = 0
                row_list = []
                for char in line:
                    if char == 'S':
                        self.start_row = maze_rows
                        self.start_col = col
                    if char != '\n':
                        row_list.append(char)
                    col += 1
                maze_rows += 1
                maze_cols = len(row_list)
                self.mazelist.append(row_list)

        self.rows = maze_rows
        self.cols = maze_cols
        self.x_trans = -maze_cols / 2
        self.y_trans = maze_rows / 2
        self.lost = turtle.Turtle(shape='turtle')
        self.screen = turtle.Screen()
        self.screen.setworldcoordinates(-(maze_cols-1) / 2 - .5,
                                        -(maze_rows-1) / 2 - .5,
                                        (maze_cols-1) / 2 + .5,
                                        (maze_rows-1) / 2 + .5)

    def __getitem__(self, idx):
        return self.mazelist[idx]

    def draw_maze(self):
        self.lost.speed(10)
        self.screen.tracer(0)
        for y in range(self.rows):
            for x in range(self.cols):
                if self.mazelist[y][x] == OBSTACLE:
                    self.draw_box(x + self.x_trans,
                                  -y + self.y_trans, 'orange')
        self.lost.color('black')
        self.lost.fillcolor('blue')
        self.screen.update()
        self.screen.tracer(1)

    def draw_box(self, x, y, color):
        self.lost.up()
        self.lost.goto(x-0.5, y+0.5)
        self.lost.color(color)
        self.lost.fillcolor(color)
        self.lost.begin_fill()
        for i in range(4):
            self.lost.forward(1)
            self.lost.right(90)
        self.lost.end_fill()

    def move(self, x, y):
        self.lost.up()
        self.lost.setheading(self.lost.towards(x + self.x_trans,
                             -y + self.y_trans))
        self.lost.goto(x + self.x_trans, -y+self.y_trans)

    def mark(self, color):
        self.lost.dot(10, color)

    def update_pos(self, row, col, val=None):
        if val:
            self.mazelist[row][col] = val
        self.move(col, row)

        if val == PART_OF_PATH:
            color = 'green'
        elif val == OBSTACLE:
            color = 'red'
        elif val == TRIED:
            color = 'black'
        elif val == DEAD_END:
            color = 'red'
        else:
            color = None

        if color:
            self.mark(color)

    def is_exit(self, row, col):
        return (row == 0 or
                row == self.rows-1 or
                col == 0 or
                col == self.cols-1)


def search(maze, start_row, start_col):
    maze.update_pos(start_row, start_col)
    # Check for base cases:
    # 1. We have run into an obstacle, return false
    if maze[start_row][start_col] == OBSTACLE:
        return False
    # 2. We have found a square that has already been explored
    if maze[start_row][start_col] == TRIED \
       or maze[start_row][start_col] == DEAD_END:
        return False

    # 3. We have found an outside edge not occupied by an obstacle
    if maze.is_exit(start_row, start_col):
        maze.update_pos(start_row, start_col, PART_OF_PATH)
        return True
    maze.update_pos(start_row, start_col, TRIED)
    # Otherwise, use logical short circuiting
    # to try each direction in turn (if needed)
    found = search(maze, start_row-1, start_col) \
        or search(maze, start_row+1, start_col) \
        or search(maze, start_row, start_col-1) \
        or search(maze, start_row, start_col+1)
    if found:
        maze.update_pos(start_row, start_col, PART_OF_PATH)
    else:
        maze.update_pos(start_row, start_col, DEAD_END)
    return found


my_maze = Maze('maze.txt')
my_maze.draw_maze()
my_maze.update_pos(my_maze.start_row, my_maze.start_col)
search(my_maze, my_maze.start_row, my_maze.start_col)
