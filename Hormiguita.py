import tkinter as tk
import turtle
import numpy as np
import time

#Lassen Sie uns die Ausgangsposition einstellen
x0 = 600/2
y0 = 600/2
zelleW = 0
zelleH = 0
MATRIX = np.zeros((100, 100))
pxm = 0
pym = 0
#Richtungen 
#1 = rechts - 2 = süd - 3 = links - 4 = nord
#Richtung einstellen
richtung = 2
#Farben
# 0 = weiß - 1 = schwarz


def ausgangsposition(papier):
    global MATRIX, pym, pxm, zelleW, zelleH,richtung
    pxm = int(x0/zelleW)
    pym = int(y0/zelleW)
    MATRIX[pxm][pym] = 1
    if(richtung == 1):
        richtung = 4
        pym -= 1
    elif(richtung == 2):
        richtung = 1
        pxm += 1
    elif(richtung == 3):
        richtung = 2
        pym += 1
    else:
        richtung = 3
        pxm -= 1
    zeile, säule = MATRIX.shape
    papier.create_rectangle( pxm*zelleW, pym*zelleH, pxm*zelleW+zelleW, pym*zelleH+zelleH, fill='black')


def einrichten_gitter(papier):
    global MATRIX, zelleW, zelleH
    zeile, säule = MATRIX.shape
    width = papier.winfo_width()
    height = papier.winfo_height()
    zelleW = int(width/säule)
    zelleH = int(height/zeile)
    for i in range(säule):
        papier.create_line(i*zelleW, 0, i*zelleW, height, fill="gray")
    for i in range(zeile):
        papier.create_line(0, i*zelleH, width, i*zelleH, fill="gray")

def checkPositions():
    global MATRIX, pxm,pym
    zeile, säule = MATRIX.shape
    if(pxm==säule):
        return True
    elif(pxm==0):
        return True
    elif(pym==zeile):
        return True
    elif(pym==0):
        return True
    else:
        return False

def aktualiserenPapier(papier):
    global MATRIX, zelleW, zelleH, pxm, pym, richtung
    papier.create_rectangle(pxm*zelleW, pym*zelleH, pxm*zelleW+zelleW, pym*zelleH+zelleH, fill='red')
    papier.update()
    if(MATRIX[pxm][pym] == 0):
        MATRIX[pxm][pym] = 1
        papier.create_rectangle(pxm*zelleW, pym*zelleH,pxm*zelleW+zelleW, pym*zelleH+zelleH, fill='black')
        if(richtung == 1):
            richtung = 2
            pym += 1
        elif(richtung == 2):
            richtung = 3
            pxm -= 1
        elif(richtung == 3):
            richtung = 4
            pym -= 1
        else:
            richtung = 1
            pxm += 1
    else:
        MATRIX[pxm][pym] = 0  # Cambiamos el color de la celda a blanco
        papier.create_rectangle(pxm*zelleW, pym*zelleH,pxm*zelleW+zelleW, pym*zelleH+zelleH, fill='white')
        # Ahora determinamos su posicion y avanzamos
        if(richtung == 1):
            richtung = 4
            pym -= 1
        elif(richtung == 2):
            richtung = 1
            pxm += 1
        elif(richtung == 3):
            richtung = 2
            pym += 1
        else:
            richtung = 3
            pxm -= 1

    papier.update()
    if(checkPositions()):
        return False
    else:
        return True

def init():
    fenster = tk.Tk(className=" Hormiguita Langton")
    papier = tk.Canvas(fenster, width=600, height=600)
    fenster.resizable(False, False)
    papier.pack()
    papier.update()
    einrichten_gitter(papier)
    ausgangsposition(papier)
    papier.update()
    sw = True
    while sw:
        sw = aktualiserenPapier(papier)
    
    fenster.mainloop()

init()