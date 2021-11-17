# Program03.py
# Nick Mock and Antonio Ferree

from grid import Grid
from arraystack import ArrayStack

def get_maze_from_file():
    """Reads the maze from a text file and returns a grid that represents it"""
    name = input("Enter a file name for the maze: ")
    fileObj = open(name, 'r')
    firstline = list(map(int, fileObj.readline().strip().split()))
    rows = firstline[0]
    columns = firstline[1]
    maze = Grid(rows, columns, "*")
    for row in range(rows):
        line = fileObj.readline().strip()
        column = 0
        for ch in line:
            maze[row][column] = ch
            column += 1
    return maze

def find_start_position(maze):
    startRow = 0
    startCol = 0
    for i in maze:
        startRow += 1
        startCol = 0
        if "P" in i:
            return(startRow, startCol)
    


def get_out(row, column, maze):
    """(row, column) is the position of the start symbol in the maze. Returns True if the maze can be solved of False otherwise"""
    # States are tuples of coordinates of cells in the grid
    stack = ArrayStack()
    stack.push((row, column))
    while not stack.isEmpty():
        # Pop the current location
        (row, column) = stack.pop()
        # IF this locaiton is 'T', we're there
        if maze[row][column] == 'T':
            return True
        elif maze[row][column] != '.':
            # Cell has not been visited, so mark it and push adjacent unvisited positions onto the stack
            maze[row][column] = '.'
        
        # Trying north, opposite for south, and column -/+ 1 for east and west
        if row != 0 and not maze[row - 1][column] in ('*','.'):
            stack.push((row - 1, column))
        
        # Try South
        if row != 0 and not maze[row + 1][column] in ('*', '.'):
            stack.push((row + 1, column))
        
        # try East
        if row != 0 and not maze[row][column + 1] in ('*', '.'):
            stack.push((row, column + 1))
        
        # Try West
        if row != 0 and not maze[row][column - 1] in ('*', '.'):
            stack.push((row, column - 1))

# Main part
maze = get_maze_from_file()
print(maze)
(startRow, startCol) = find_start_position(maze)
success = get_out(startRow, startCol, maze)
if success:
    print("maze solved!")
    print(maze)
else:
    print("No path out of this maze")
    