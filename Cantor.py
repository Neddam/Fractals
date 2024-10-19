from tkinter import *


def cantor_set(x_cord,y_cord,leng):
    if leng > 1: #keep doing this while the line is > 1 pixel lon
        win.create_line(x_cord,y_cord,x_cord+leng,y_cord) #draw horizontal lin
        y_cord = y_cord + 50 #move 50 pixels down for next generation
        cantor_set(x_cord,y_cord,leng/3) #left hand offspring
        cantor_set(x_cord+2/3*leng,y_cord,leng/3) #right hand offspring


width,height = 1500,500
root = Tk()
win = Canvas(root,width=width,height=height)
win.pack()
cantor_set(10,10,width-20)

root.mainloop()