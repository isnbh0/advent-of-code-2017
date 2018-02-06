from functions import get_coord


class SpiralGrid():
	def __init__(self, rule_func):
		self.grid = dict()
		self.rule = rule_func
		self.grid[(0, 0)] = 1 
		return

	def step(self):
		grid_size = len(self.grid)
		new_coord = get_coord(grid_size+1)
			
		self.grid[new_coord]\
		= self.rule(self.grid, new_coord)

		return self.grid[new_coord]

