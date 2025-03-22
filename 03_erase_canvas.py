import tkinter as tk

# Constants for the grid
CELL_SIZE = 20
GRID_WIDTH = 20
GRID_HEIGHT = 15
ERASER_SIZE = 40

class EraserCanvas:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=GRID_WIDTH * CELL_SIZE, height=GRID_HEIGHT * CELL_SIZE, bg='white')
        self.canvas.pack()
        
        self.cells = []  # Store cell references
        self.create_grid()
        
        # Create the eraser rectangle
        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, outline='black', fill='gray')
        
        # Bind mouse events
        self.canvas.bind("<B1-Motion>", self.erase)
        self.canvas.bind("<Button-1>", self.erase)  # Also erase on click
    
    def create_grid(self):
        """Create a grid of blue cells."""
        for row in range(GRID_HEIGHT):
            row_cells = []
            for col in range(GRID_WIDTH):
                x1, y1 = col * CELL_SIZE, row * CELL_SIZE
                x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
                cell = self.canvas.create_rectangle(x1, y1, x2, y2, fill='blue', outline='white')
                row_cells.append(cell)
            self.cells.append(row_cells)
    
    def erase(self, event):
        """Erase cells within the eraser rectangle."""
        x, y = event.x, event.y
        
        # Move the eraser to the new position
        self.canvas.coords(self.eraser, x - ERASER_SIZE//2, y - ERASER_SIZE//2, x + ERASER_SIZE//2, y + ERASER_SIZE//2)
        
        # Erase cells within eraser area
        for row in self.cells:
            for cell in row:
                x1, y1, x2, y2 = self.canvas.coords(cell)
                if x1 < x < x2 and y1 < y < y2:
                    self.canvas.itemconfig(cell, fill='white')

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Canvas Eraser")
    app = EraserCanvas(root)
    root.mainloop()