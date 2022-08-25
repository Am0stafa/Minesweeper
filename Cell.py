#! we are going to create a button instance that is going to belong to each cell object 
from tkinter import Button

class Cell:
    def __init__(self,isMine=False):
        self.isMine = isMine
        self.cell_btn_object = Button() #! this will carry reference to the button created to be able to place it on the grid add this will help us customize

    def createBtn(self,frame):
        btn = Button(frame,text="text")
        #* we bind the methods and firstly specify the keys that is clicked on
        btn.bind('<Button-1>', self.leftClk) # Left Click        
        btn.bind('<Button-2>', self.rightClk ) # Right Click
        self.cell_btn_object=btn
        return self
        
    #! we have will have two types of action when we right click and when we left click 
    
    def leftClk(self,e):
        pass
    def rightClk(self,e):
        print('click')