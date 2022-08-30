#! we are going to create a button instance that is going to belong to each cell object 
from tkinter import *
import setting
import random
import ctypes
import sys

class Cell:
    all = []
    cellsLeft = setting.CELL_COUNT
    cell_count_label_object = None
    def __init__(self,x,y,isMine=False):
        self.isMine = isMine
        self.cell_btn_object = Button(width=12,height=4) #! this will carry reference to the button created to be able to place it on the grid add this will help us customize
        self.x = x
        self.y = y
        self.isClicked = False
        self.is_mine_candidate= False
        Cell.all.append(self) #! store all instances inside a list to take further actions with them

    def createBtn(self,frame):
        btn = Button(frame,width=12,height=4,bg="white")
        #* we bind the methods and firstly specify the keys that is clicked on
        btn.bind('<Button-1>', self.leftClk) # Left Click        
        btn.bind('<Button-2>', self.rightClk ) # Right Click
        self.cell_btn_object=btn
        return self
        
        
        
    #^ whenever we left click on a number we should display a number which represent how many mines surrounding that cell
    def leftClk(self,e):
        if self.isMine:
            self.showMine()
        else:
            if self.surroundingCounter() == 0:
                for cell_obj in self.surrounding():
                    if cell_obj.surroundingCounter() == 0:
                        cell_obj.showCell()
                        for x in cell_obj.surrounding():
                            x.showCell()
                            if x.surroundingCounter() == 0:
                                for y in x.surrounding():
                                    y.showCell()
                    else:
                        cell_obj.showCell()
            self.showCell()
            #! If Mines count is equal to the cells left count, player won
            if Cell.cellsLeft == setting.MINES_COUNT:
                ctypes.windll.user32.MessageBoxW(0, 'Congratulations! You won the game!', 'Game Over', 0)
    
    def showMine(self):
        self.cell_btn_object.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0, 'You clicked on a mine', 'Game Over', 0)
        sys.exit()

    #! each time its called we decrease the count
    def showCell(self):
        #^ to make it idempotent
        if not self.isClicked:
            num = self.surroundingCounter()
            self.cell_btn_object.configure(text=num,bg='black')
            Cell.cellsLeft-=1
            #! replace the text of the cell count label with the newer count refresh
            Cell.cell_count_label_object.configure(text=f"Cells Left:{Cell.cellsLeft}")
        self.isClicked = True


    #& the way we will calculate the number of mines is by getting all the cells and checking to see if they are a mine
    def getCellByAxis(self,x,y):
        for i in Cell.all:
            if i.x == x and i.y == y:
                return i
    
    def surrounding(self):
        #! get every possible surrounding then filter when it return None
        surround = [
            self.getCellByAxis(self.x - 1, self.y -1),
            self.getCellByAxis(self.x - 1, self.y),
            self.getCellByAxis(self.x - 1, self.y + 1),
            self.getCellByAxis(self.x, self.y - 1),
            self.getCellByAxis(self.x + 1, self.y - 1),
            self.getCellByAxis(self.x + 1, self.y),
            self.getCellByAxis(self.x + 1, self.y + 1),
            self.getCellByAxis(self.x, self.y + 1)
        ]
        
        cells = [cell for cell in surround if cell is not None]
        return cells
        
    #* we can make it a readOnly attribute by using the property decorator
    def surroundingCounter(self):
        counter = 0
        
        for cell in self.surrounding():
            if cell.isMine:
                counter+=1

        return counter
    

    def rightClk(self,e):
       if not self.is_mine_candidate:
            self.cell_btn_object.configure(bg='orange')
            self.is_mine_candidate = True
       else:
            self.cell_btn_object.configure(bg='SystemButtonFace')
            self.is_mine_candidate = False
        
        
        
    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg='black',
            fg='white',
            text=f"Cells Left:{Cell.cellsLeft}",
            font=("", 30)
        )
        Cell.cell_count_label_object = lbl
        
    @staticmethod
    def genRandomMine():
        randCells = random.sample(Cell.all,setting.mines)
        
        for i in randCells:
            i.isMine = True

