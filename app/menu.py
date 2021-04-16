from tkinter import *

canva = Tk()
canva.geometry('400x200')
canva.title('Aplicación con Menú')

#Se genera el menú
menu_bar = Menu(canva)
#Se inserta el menú
canva.config(menu=menu_bar)

#Se crean las opciones a menú
menu_opciones = Menu(menu_bar, tearoff=0)
menu_opciones.add_command(label='Opción 1', command=lambda: frame_opcion1())
menu_opciones.add_command(label='Opción 2', command=lambda: frame_opcion2())
menu_opciones.add_separator()
menu_opciones.add_command(label='Salir', command=canva.quit)

#Se le agregan las opciones
menu_bar.add_cascade(label='Menú de Opciones', menu=menu_opciones)

def frame_opcion1():
    frame_limpiar()
    frame_op1 = Frame()
    frame_op1.pack()
    frame_op1.config(width="400", height="200", bg="slate gray", bd=25)
    frame_op1.config(relief="sunken")
    frame_op1.pack(fill="both", expand=1)
    frame_op1.columnconfigure(1, weight=1)

    label_1 = Label(frame_op1, text='Usuario').grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
    label_2 = Label(frame_op1, text='Contraseñ').grid(row=1, column=0, padx=5, pady=5, sticky=NSEW)

def frame_opcion2():
    frame_limpiar()
    frame_op2 = Frame()
    frame_op2.pack()
    frame_op2.config(width="400", height="200", bg="DodgerBlue4", bd=25)
    frame_op2.config(relief="sunken")
    frame_op2.pack(fill="both", expand=1)
    frame_op2.columnconfigure(1, weight=1)

def frame_limpiar():
    list = layout.pack_slaves()
    for l in list:
        l.pack_forget()

canva.mainloop()