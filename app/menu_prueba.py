from tkinter import *

root = Tk()

menuprueba = Menu(root)
root.config(menu=menuprueba)

menu_file = Menu(menuprueba, tearoff=0)
menu_file.add_command(label="Nuevo")
menu_file.add_command(label="Abrir")
menu_file.add_command(label="Guardar")
menu_file.add_command(label="Cerrar")
menu_file.add_separator()
menu_file.add_command(label="Cerrar", command=root.quit)

menu_edit = Menu(menuprueba, tearoff=0)
menu_edit.add_command(label="Cortar")
menu_edit.add_command(label="Copiar")
menu_edit.add_command(label="Pegar")

menu_help = Menu(menuprueba, tearoff=0)
menu_help.add_command(label="Ayuda")
menu_help.add_separator()
menu_help.add_command(label="Información")

menu_bar = Menu(menuprueba, tearoff=0)
menu_bar.add_cascade(label="Archivo", menu=menu_file)
menu_bar.add_cascade(label="Editar", menu=menu_edit)
menu_bar.add_cascade(label="Ayuda", menu=menu_help)

root.mainloop()