#! we are going to create a button instance that is going to belong to each cell object 
from tkinter import Button
import setting
import random
class Cell:
    all = []
    def __init__(self,x,y,isMine=False):
        self.isMine = isMine
        self.cell_btn_object = Button(width=12,height=4) #! this will carry reference to the button created to be able to place it on the grid add this will help us customize
        self.x = x
        self.y = y
        Cell.all.append(self) #! store all instances inside a list to take further actions with them

    def createBtn(self,frame):
        btn = Button(frame,width=12,height=4)
        #* we bind the methods and firstly specify the keys that is clicked on
        btn.bind('<Button-1>', self.leftClk) # Left Click        
        btn.bind('<Button-2>', self.rightClk ) # Right Click
        self.cell_btn_object=btn
        return self
        
    #^ whenever we left click on a number we should display a number which represent how many mines surrounding that cell
    def leftClk(self,e):
        print('click shemal')
        
        
    def rightClk(self,e):
        print('click yemen')
    
    @staticmethod
    def genRandomMine():
        randCells = random.sample(Cell.all,setting.mines)
        
        for i in randCells:
            i.isMine = True

