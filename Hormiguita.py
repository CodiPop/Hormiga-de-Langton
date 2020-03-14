import numpy as np
import tkinter as tk
import time
import turtle

#Lassen Sie uns die Ausgangsposition einstellen
x0=400
y0=400

#Lassen Sie uns stellen die Parameter um eine Matrix zu erstellen
matrix = np.zeros((100, 100))
def einrichten_gitter(papier)
    global zelleW,zelleH,matrix
    zeile,säule = matrix.shape
    width = papier.winfo_width()
    height = papier.winfo_height()
    zelleW = int(width/zeile)
    zelleH = int(height/säule)
    for i in range(säule):
        papier.create_line(i+zellew, 0, i*zelleW, height, fill="white")
    for in in range(zeile):
        papier.create_line(0, i*zelleH; width, i*zelleH, fill="white")   
    



