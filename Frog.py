from tkinter import *
from Car import *
from Lane import *

class Frog():
    width = 20
    height = 20
    step=40
    def __init__(self, x, y,wx1,wy1,wx2,wy2,step):
        self.x=x
        self.y=y
        self.window_x1 = wx1
        self.window_y1 = wy1
        self.window_x2 = wx2
        self.window_y2 = y+self.height  #wy2
        self.step=step

    def finishReached(self):
        if self.y<=self.window_y1:
            #self.y=0
            return True
        return False
    def moveLeft(self):
        self.x-=self.step
        if self.x<self.window_x1:
            self.x=self.window_x1
    def moveRight(self):
        self.x+=self.step
        if self.x>self.window_x2-self.width:
            self.x=self.window_x2-self.width
    def moveUp(self):
        self.y-=self.step
        if self.y<self.window_y1:
            self.y=self.window_y1
    def moveDown(self):
        self.y+=self.step
        if self.y>self.window_y2-self.height:
            self.y = self.window_y2 - self.height;


    def draw(self, w):
        w.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height,fill="green")

    def collision(self,c):
        if c.y!=self.y:
            return False
        if c.x<=self.x<=c.x+c.width or c.x<=self.x+self.width<=c.x+c.width:
            print("Collision")
            #self.x=WIDTH/2,
            #self.y=Car[-1].y+LANE_HEIGHT+LANE_HEIGHT/4
            return True
        return False


    """def move(self,x,y):
        self.x+=x
        self.y+=y

    def moveX(self,x):
        self.x += x
    def moveY(self,y):
        self.y += y
    """