import tkinter as tk

root = tk.Tk()
root.title("Erasor tool by kashaf")
canvas = tk.Canvas(root,width=500,height=500, bg="pink")
canvas.pack()


def drow_grid():
    for row in range(0,500,50):
        for col in range(0,500,50):
            canvas.create_rectangle(col,row, col+50, row +50, fill="blue", outline="black")
            
drow_grid()

is_erasing = False
def start_erasing(event):
    global is_erasing
    is_erasing = True
def stop_erasing(event):
    global is_erasing
    is_erasing = False
def erase(event):
    if is_erasing:
        col = event.x // 50
        row = event.y//50
        canvas.create_rectangle(col* 50,row * 50, (col +1) * 50, (row +1)*50, fill="white", outline="black")
        
canvas.bind("<ButtonPress-1>", start_erasing)
canvas.bind("<ButtonRelease-1>", stop_erasing)
canvas.bind("<Motion>", erase)

root.mainloop()