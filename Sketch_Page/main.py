import tkinter as tk
root = tk.Tk()
# Create Title
root.title('Sketch Page')
# Specify size
canvas_width = 900
canvas_height = 500
root.geometry(f'{canvas_width}x{canvas_height}')
# Create canvas widget
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)

#event parameter will contain information about the mouse event
def sketch(event):
    # These coordinates create a small box around the current mouse position (event.x, event.y).
    x1, y1, x2, y2 = (event.x - 3), (event.y - 3), (event.x + 3), (event.y +3)
    # specify type of display
    canvas.create_line(x1, y1, x2, y2, fill='blue')

# Binds the 'sketch' function to the <B1-Motion> event on the canvas.
# And the <B1-Motion> event occurs when the left mouse button (Button 1) is held down and the mouse is moved.
canvas.bind('<B1-Motion>',sketch)
# Create a Label
tk.Label(text='Double click and drag to scketch!',font='Ariel 16 bold', fg='green').pack()
canvas.pack()

root.mainloop()
