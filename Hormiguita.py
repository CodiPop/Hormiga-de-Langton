from tkinter import *
import tkinter as tk
import turtle
import numpy as np
import time

root = Tk()
def speichern():
  global x0,y0,n,H,W,N
  x0 = int(ex.get())
  y0 = int(ey.get())
  n = int(en.get())
  N = int(eN.get())
  H = n
  W = n
  root.destroy()
root.title("Datos iniciales")
l1 = Label(root,text="Ingrese las posicion inicial de la hormiga:")
l2 = Label(root,text="Ingrese el tamaño n de la grilla:")
l3 = Label(root,text="Ingrese el numero N de iteraciones que desea:")
ex = Entry(root, width=10)
ex.insert(0, "X")
ey = Entry(root, width=10)
ey.insert(0, "Y")
en = Entry(root, width=10 )
eN = Entry(root, width=10 )
mybutton = Button(root,text="Guardar e iniciar",command=speichern)
l1.grid(row=0,column=0)
ex.grid(row=1,column=0)
ey.grid(row=1,column=1)
l2.grid(row=2,column=0)
en.grid(row=3,column=0)
l3.grid(row=4,column=0)
eN.grid(row=5,column=0)
mybutton.grid(row=6,column=0, columnspan=2,) 
root.mainloop()
print(N)
print(H)
print(x0)
print(y0)
Ncont = 0

def einrichten():
    global x0, y0,zelleW,zelleH,pxm,pym, MATRIX
    zelleW = 0
    zelleH = 0
    MATRIX = np.zeros((H, W))
    pxm = 0
    pym = 0


#Lassen Sie uns die Ausgangsposition einstellen


#Richtungen 
#1 = rechts - 2 = süd - 3 = links - 4 = nord
#Richtung einstellen
richtung = 2
#Farben
# 0 = weiß - 1 = schwarz


def ausgangsposition(papier):
    global MATRIX, pym, pxm, zelleW, zelleH,richtung
    pxm = x0
    pym = y0
    print(pxm,pym)
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
    global MATRIX, zelleW, zelleH, fenster
    zeile, säule = MATRIX.shape
    width = papier.winfo_width()
    height = papier.winfo_height()
    zelleW = float(width/säule)
    print(zelleW)
    zelleH = float(height/zeile)
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
    global MATRIX, zelleW, zelleH, pxm, pym, richtung, N, Ncont, fenster,l5
    Ncont = Ncont + 1
    papier.create_rectangle(pxm*zelleW, pym*zelleH, pxm*zelleW+zelleW, pym*zelleH+zelleH, fill='red')
    papier.update()
    if(MATRIX[pxm][pym] == 0):
        MATRIX[pxm][pym] = 1
        papier.create_rectangle(pxm*zelleW, pym*zelleH,pxm*zelleW+zelleW, pym*zelleH+zelleH, fill='black')
        if(richtung == 1):
            richtung = 2
            l7 = Label(fenster, bd=5, text="Derecha").grid(row=2,column=4)
            pym += 1
        elif(richtung == 2):
            richtung = 3
            l7 = Label(fenster, bd=5, text="Abajo").grid(row=2,column=4)
            pxm -= 1
        elif(richtung == 3):
            richtung = 4
            l7 = Label(fenster, bd=5, text="Izquierda").grid(row=2,column=4)
            pym -= 1
        else:
            richtung = 1
            l7 = Label(fenster, bd=5, text="Arriba").grid(row=2,column=4)
            pxm += 1
    else:
        MATRIX[pxm][pym] = 0  # Cambiamos el color de la celda a blanco
        papier.create_rectangle(pxm*zelleW, pym*zelleH,pxm*zelleW+zelleW, pym*zelleH+zelleH, fill='white')
        # Ahora determinamos su posicion y avanzamos
        if(richtung == 1):
            richtung = 4
            l7 = Label(fenster, bd=5, text="Derecha").grid(row=2,column=4)
            pym -= 1
        elif(richtung == 2):
            richtung = 1
            l7 = Label(fenster, bd=5, text="Abajo").grid(row=2,column=4)
            pxm += 1
        elif(richtung == 3):
            richtung = 2
            l7 = Label(fenster, bd=5, text="Izquierda").grid(row=2,column=4)
            pym += 1
        else:
            richtung = 3
            l7 = Label(fenster, bd=5, text="Arriba").grid(row=2,column=4)
            pxm -= 1

    if (Ncont==N):
        return False
    else:
        l5 = Label(fenster, bd=5, text=Ncont+1).grid(row=1,column=4)
    papier.create_rectangle(pxm*zelleW, pym*zelleH, pxm*zelleW+zelleW, pym*zelleH+zelleH, fill='red')
    papier.update()
    if(checkPositions()):
        return False
    else:
        return True

def init():
    global sw, Ncont,l5, l4, fenster, richtung, t
    einrichten()
   
    fenster = tk.Tk(className=" Hormiguita Langton")
    fenster.resizable(False, False)
    papier = tk.Canvas(fenster, width=900, height=650)
    papier.grid(rowspan=5,columnspan=2)
    l4 = Label(fenster, bd=5, text="Cantidad de pasos N", justify=CENTER,bg='black',  fg='white').grid(row=1, column=3)
    l5 = Label(fenster, bd=5, text=Ncont).grid(row=1,column=4)
    l6 = Label(fenster, bd=5, text="Direccion:", justify=CENTER,bg='black',  fg='white').grid(row=2, column=3)
    l7 = Label(fenster, bd=5, text="    ").grid(row=2,column=4)
    l8 = Label(fenster, bd=5, text="Tiempo entre cada paso:",justify=CENTER,bg='black',fg='white').grid(row=3,column=3)
    #eT = Entry(fenster, width = 5)
    #eT.grid(row=3,column = 4)
    #eT.insert(0, 1)
    var = StringVar(fenster)
    var.set(1) # initial value

    option = OptionMenu(fenster, var, 1, 0.5, 0.25, 0.125, 0)
    option.grid(row=3,column=4)

    papier.update()
    einrichten_gitter(papier)
    ausgangsposition(papier)
    papier.update()
    sw=True
    while sw==True:
        sw = aktualiserenPapier(papier)
        #t = float(eT.get())
        t = float(var.get())
        if(t!=0 ):
            time.sleep(t)
        

    fenster.mainloop()

init()