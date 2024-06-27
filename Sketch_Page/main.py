import tkinter as tk
root = tk.Tk()
root.title('Sketch Page')
canvas_width = 900
canvas_height = 500
root.geometry(f'{canvas_width}x{canvas_height}')

canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)

def sketch(event):
    x1, y1, x2, y2 = (event.x - 3), (event.y - 3), (event.x + 3), (event.y +3)
    canvas.create_line(x1, y1, x2, y2, fill='blue')

canvas.bind('<B1-Motion>',sketch)

tk.Label(text='Double click and drag to scketch!',font='Ariel 16 bold', fg='green').pack()
canvas.pack()

root.mainloop()