from config import *
from evaluation import * 

def Max(grid, depth):
    if (depth <= 0):
        return (evaluation(grid))
    return (Min(grid, depth -1))

def Min(grid, depth):
    if (depth <= 0):
        return (evaluation(grid))
    return (Max(grid, depth - 1))

def ia_turn(grid, depth):
    return (Min(grid, depth - 1))
