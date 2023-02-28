from math import sqrt

class Puzzle:
    def __init__(self, grid: list) -> None:
        self.grid = grid
        self.grid_size = len(grid)  # must be a square number
        self.box_size = sqrt(self.grid_size)

        if not int(sqrt(self.grid_size))**2 == self.grid_size:
            raise ValueError('Grid size is not a square number.')

    def row_checker(self, index: int) -> bool:
        """ finds the current row, counts the unique values, then compares that number with the length of the original row """
        return len(set(int(x) for x in self.grid[index//self.grid_size * self.grid_size:(index//self.grid_size + 1) * self.grid_size] if x)) == len([x for x in self.grid[index//self.grid_size * self.grid_size:(index//self.grid_size + 1) * self.grid_size] if x])

    def column_checker(self, index: int) -> bool:
        """ finds the current column, counts the unique values, then compares that number with the length of the original column """
        return len(set(int(x) for x in self.grid[index % self.grid_size::self.grid_size] if x)) == len([x for x in self.grid[index % self.grid_size::self.grid_size] if x])

    def box_checker(self, index: int) -> bool:
        """ finds the current box, counts the unique values, then compares that number with the length of the original box """
        gs, bs = self.grid_size, self.box_size
        start = index//gs//bs * (bs * gs) + (index % gs)//bs * bs   # start = box level * box size + box column * box size 
        box = []
        [[box.append(x) for x in self.grid[start+i*gs:start+i*gs+bs]] for i in range(0,3)]
        return len(set(int(x) for x in box if x)) == len([x for x in box if x])

    def is_valid(self, index: int) -> bool:
        return self.row_checker(index) and self.column_checker(index) and self.box_checker(index)

    def solve(self, index=0) -> list:
        """ fills the puzzle blank-by-blank, verifying answers recursively"""
        x = 1
        if index == self.grid_size**2:  # checks if puzzle is already solved
            return True
        if self.grid[index]:
            if index:
                return self.solve(index+1)  # skips to next square if already filled
            if self.solve(index+1):
                return self.grid
        while x <= 9:
            self.grid[index] = x
            if self.is_valid(index) and self.solve(index+1):
                return True if index else self.grid
            x +=1
        self.grid[index] = 0
        return False

def cli(self, grid_size=9) -> Puzzle:
    grid = []
    print('Please enter all given numbers in the puzzle.')
    for row in range(grid_size):
        for column in range(grid_size):
            resp = input('Row ', row+1, ', Column ', column+1, ": ")
            resp = 0 if resp is None else resp
            grid.append(resp)
    return Puzzle(grid)
