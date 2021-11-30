import random

def create_rand_pos() -> tuple:
	return (random.randint(0, SCALE-1), random.randint(0, SCALE-1))

def get_valid_neighbors(pos, arr):
	neighbors = []
	if pos[0]+1 >= 0 and pos[0]+1 < SCALE:
		if arr[pos[0]+1][pos[1]] != 1:
			neighbors.append((pos[0]+1, pos[1]))
	if pos[0]-1 >= 0 and pos[0]-1 < SCALE:	
		if arr[pos[0]-1][pos[1]] != 1:
			neighbors.append((pos[0]-1, pos[1]))
	if pos[1]+1 >= 0 and pos[1]+1 < SCALE:
		if arr[pos[0]][pos[1]+1] != 1:
			neighbors.append((pos[0], pos[1]+1))
	if pos[1]-1 >= 0 and pos[1]-1 < SCALE:
		if arr[pos[0]][pos[1]-1] != 1:
			neighbors.append((pos[0], pos[1]-1))
	return neighbors

def pathfinding() -> list:
	completed_paths = []
	paths = [[player_pos]]
	pf_arr[player_pos[0]][player_pos[1]] = 1
	found = False

SCALE = 10
level = [['_']*SCALE for i in range(SCALE)]
pf_arr = [[0]*SCALE for i in range(SCALE)]
player_pos = create_rand_pos()
target_pos = create_rand_pos()

i = 0
while i < SCALE**2/5:
	pos = create_rand_pos()
	if level[pos[0]][pos[1]] == '_':
		level[pos[0]][pos[1]] = '.'
		pf_arr[pos[0]][pos[1]] = 1
		i += 1

path = pathfinding()

print(path)

level[player_pos[0]][player_pos[1]] = '▣'
level[target_pos[0]][target_pos[1]] = '▦'