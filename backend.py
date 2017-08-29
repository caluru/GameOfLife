import numpy as np

COLS, ROWS = 0,0

def getParams():
	COLS = int(raw_input('Enter Width of Board: '))
	ROWS = int(raw_input('Enter Height of Board: '))
	return np.zeros((ROWS+2, COLS+2), dtype=np.int)

def printBoard(board):
	for i in range(1, len(board)-1):
		for j in range(1, len(board[i])-1):
			print board[i][j], 
		print ''

def neighborCount(x, y, board):
	neighbors = 0
	for i in range(x-1, x+2):
		for j in range(y-1, y+2):
			if x == i and y == j:
				continue
			neighbors += board[i][j]

	return neighbors

def iterate(board):
	#newBoard = np.zeros((len(board), len(board[0])), dtype=int)
	newBoard = [[0 for i in range(len(board))] for j in range(len(board))]

	for i in range(1,len(newBoard)-1):
		for j in range(1, len(newBoard)-1):
			neighbors = neighborCount(i, j, board)
			if board[i][j] == 0:
				newBoard[i][j] = 1 if neighbors == 3 else 0
			else:
				newBoard[i][j] = 1 if neighbors in [2,3] else 0

	return newBoard

if __name__ == '__main__':
	ROWS, COLS = 0,0
	board = getParams()

	i = raw_input('Enter a live starting position: ')
	while(i != ''):
		a = map(lambda x: int(x), i.split())
		board[a[0]+1][a[1]+1] = 1
		i = raw_input('Enter a live starting position: ')
	iterations = int(raw_input('Enter number of iterations: '))

	print 'Starting Board:'
	printBoard(board)

	for i in range(iterations):
		print 'Iteration Number: ' + str(i+1)
		board = iterate(board)
		printBoard(board)



