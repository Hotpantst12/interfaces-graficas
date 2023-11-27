from tkinter import Tk, Button, Frame

Ventana = Tk()
Ventana.title("Ejercicio 1")
Ventana.geometry("300x80")

Frame1 = Frame(Ventana, bg="red")
Frame1.pack(expand=True,fill="both")