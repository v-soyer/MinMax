from config import *

def evaluation(grid):
    for column in range(NB_SQUARES):
        for line in range(NB_SQUARES):
            if (grid[line][column] == '0'):
                return(line, column)