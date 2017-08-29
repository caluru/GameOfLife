from backend import *
import Tkinter as tk

COLS = int(raw_input('Enter Width of Board: '))
ROWS = int(raw_input('Enter Height of Board: '))
#board =  np.zeros((ROWS+2, COLS+2), dtype=int)
board = [[0 for i in range(ROWS+2)] for j in range(COLS+2)]
tiles = [[None for i in range(ROWS)] for j in range(COLS)]

def callback(event):
    # Get rectangle diameters
    col_width = c.winfo_width()/COLS
    row_height = c.winfo_height()/ROWS
    # Calculate column and row number
    col = event.x//col_width
    row = event.y//row_height
    # If the tile is not filled, create a rectangle
    if not tiles[row][col]:
        tiles[row][col] = c.create_rectangle(col*col_width, row*row_height, (col+1)*col_width, (row+1)*row_height, fill="green")
        board[row+1][col+1] = 1
    # If the tile is filled, delete the rectangle and clear the reference
    else:
        c.delete(tiles[row][col])
        tiles[row][col] = None
        board[row+1][col+1] = 0
    printBoard(board)

def buttonCallback(board = board):
	col_width = c.winfo_width()/COLS
	row_height = c.winfo_height()/ROWS
	temp = iterate(board)
	c.delete('all')

	#Redraw Grid Lines
	for i in range(0, c.winfo_width(), c.winfo_width()/COLS):
		c.create_line([(i,0), (i,c.winfo_width())], tag='grid_line')
	for j in range(0, c.winfo_height(), c.winfo_height()/ROWS):
		c.create_line([(0,j), (c.winfo_height(),j)], tag='grid_line')

	#Draw new rectangles on grid
	for row in range(ROWS):
		for col in range(COLS):
			board[row+1][col+1] = temp[row+1][col+1]
			if board[row+1][col+1] == 1:
				tiles[row][col] = c.create_rectangle(col*col_width, row*row_height, (col+1)*col_width, (row+1)*row_height, fill="green")
			elif board[row+1][col+1] == 0:
				c.delete(tiles[row][col])
        		tiles[row][col] = None

	c.update_idletasks()


root = tk.Tk()
c = tk.Canvas(root, width=500, height=500, borderwidth=0, background='white')
c.pack()
c.update_idletasks()

for i in range(0, root.winfo_width(), root.winfo_width()/COLS):
	c.create_line([(i,0), (i,root.winfo_width())], tag='grid_line')

for j in range(0, root.winfo_height(), root.winfo_height()/ROWS):
	c.create_line([(0,j), (root.winfo_height(),j)], tag='grid_line')
c.pack()
d = tk.Button(root, text='Iterate', command=lambda x=board: buttonCallback(x))
d.pack(side='right')
c.bind("<Button-1>", callback)

root.mainloop()