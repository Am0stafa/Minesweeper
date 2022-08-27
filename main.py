import tkinter as tk
import setting
import utils
import Cell as cell


root = tk.Tk()
root.configure(bg="black")
root.geometry(f'{setting.WIDTH}x{setting.HEIGHT}')
root.title("Minesweeper Game")
root.resizable(False, False)

#^ frame is like a container which can contain more elements we use frames as we want to divide our window into some sections

topFrame = tk.Frame(root, bg="black", width=setting.WIDTH, height=utils.hightPrct(25))
topFrame.place(x=0,y=0)

game_title = tk.Label(
    topFrame,
    bg='black',
    fg='white',
    text='Minesweeper Game',
    font=('', 48)
)

game_title.place(x=utils.widthPrct(25), y=0)

leftFrame = tk.Frame(root, bg="black", width=utils.widthPrct(25), height=utils.hightPrct(75))
leftFrame.place(x=0,y=utils.hightPrct(25))

#* center frame for our game

centerFrame = tk.Frame(root, bg="black",width=utils.widthPrct(75), height=utils.hightPrct(75))
centerFrame.place(x=utils.widthPrct(25),y=utils.hightPrct(25))


for x in range(setting.GRID_SIZE):
    for y in range(setting.GRID_SIZE):
        c =  cell.Cell(x,y)
        c.createBtn(centerFrame)
        c.cell_btn_object.grid(column=x,row=y)


# Call the label from the Cell class
cell.Cell.create_cell_count_label(leftFrame)
cell.Cell.cell_count_label_object.place(x=0, y=0)
cell.Cell.genRandomMine();


# Run the window
root.mainloop() 