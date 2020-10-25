from Frog import *
from Car import *
from Lane import *
from tkinter import *
import time
import keyboard
from datetime import datetime
"""
    #TASK 5:
    - implement one of:
        - problem with keys: too fast -> Leave 0.2sg    ->game.py
        - Pause when pressing "p" alternate between pause/no pause -> game.py
    - save scores and records in a file, and read the file when the game starts placiing all the scores into a list. 
            - functions open, etc. to save/read the scores.-> read/write from a List of scores.
        - Optional: To have the records sorted, lists in python have a function named "sort" to sort a list: https://www.w3schools.com/python/ref_list_sort.asp
        - Optional: save the records with an associated name. The content of the file may be:
            John,33
            Doe,44
            ...

            You can read the file using a dictionnary to save the scores and names.
            To separate a string by a "," , you can use the function "split" of string.
     
"""

tk=Tk()
WIDTH=800
HEIGHT=400
w = Canvas(tk, width=WIDTH, height=HEIGHT)
tk.title("Juego")
var = StringVar()
myLabel1=Label(w,textvariable=var )
myLabel1.place(x=50,y=0)
myLabel2=Label(w,text="Score: ")
myLabel2.place(x=0,y=0)
myLabel3=Label(w,text="Pulsa p per pausar ")
myLabel3.place(x=0,y=30)

w.pack()

#x,y,type,numOfCars,carsSpeed)

LANE_HEIGHT=60
TOP_WINDOW_SPACE=60
speeds=[5,-14,8,-9,11]
lanes=[None]*5
for i in range(len(lanes)):
    if i==4:
        lanes[i] = Lane(0, TOP_WINDOW_SPACE + LANE_HEIGHT * i, 2, 3, speeds[i], LANE_HEIGHT)
    else:
        lanes[i] = Lane(0,TOP_WINDOW_SPACE + LANE_HEIGHT*i,1,4,speeds[i],LANE_HEIGHT)



frog=Frog(WIDTH/2,lanes[-1].y+LANE_HEIGHT+LANE_HEIGHT/4,0,30,WIDTH,HEIGHT,step=LANE_HEIGHT)
now = datetime.now()
Game=TRUE


name=input("Tell me your name:")
#dictionary={"Key":"Value"}
paused=False

def orden(e):
    return e["Puntuacion"]
while Game:

    if keyboard.is_pressed("p"):
        paused=not paused

    if not paused:
        for lane in lanes:
            lane.moveCars()

            # move the frog
        if keyboard.is_pressed("up arrow"):
            frog.moveUp()
            if frog.finishReached():
                print("0 reached by the frog")
                archivo_texto = open("archivo.txt","a")
                archivo_texto.write("\n"+name+","+str(score))
                archivo_texto.close()
                archivo_texto=open("archivo.txt", "r")
                records=archivo_texto.readlines()
                archivo_texto.close()
                records.remove("\n")

                print(records)
                dictionary={}
                listaordenada=[]
                for line in records:
                    x=line.split(",")

                    #dictionary[x[0]]=x[1]
                    dictionary={"Nombre":x[0],"Puntuacion":float(x[1])}
                    listaordenada.append(dictionary)
                    #listaordenada[i]=diccionario que contiene nombre y puntuación persona iesima

                listaordenada.sort(reverse=True,key=orden)
                print(listaordenada)
                #print(dictionary)

                Game = False
        if keyboard.is_pressed("down arrow"):
            frog.moveDown()
        if keyboard.is_pressed("left arrow"):
            frog.moveLeft()
        if keyboard.is_pressed("right arrow"):
            frog.moveRight()
        later = datetime.now()
        score = 100 - (later - now).total_seconds()
        var.set(score)


    w.delete("all")
    w.create_rectangle(0, 0, WIDTH, HEIGHT, fill="white")

    for lane in lanes:
        lane.draw(w)
    frog.draw(w)
    w.update()

    for lane in lanes:
        for c in lane.cars:
            if frog.collision(c):
                frog.x=WIDTH/2
                frog.y=lanes[-1].y+LANE_HEIGHT+LANE_HEIGHT/4
                #print("Juego finalizado")
                #Game=False

    time.sleep(50/1000)
#w.mainloop()

print("Game over")



