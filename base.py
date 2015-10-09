from tkinter import * #libreria bonisz :3
from tkinter import messagebox #libreria para todos los messageBox
from tkinter import ttk #Libreria para barra de progreso(cargando)

root=Tk() #crear ventana

#############################Ventana de carga
def mostrar(ventana):
    return ventana.deiconify # Muestra una ventana
def ocultar(ventana): 
    return ventana.withdraw() # Oculta una ventana
def ejecutar(f): 
	root.after(100, f)

v1=Toplevel(root)
v1.title("Bee 1.0")
v1.geometry("450x180")
v1.config(bg="#1C1C1C")
v1.protocol("WM_DELETE_WINDOW", "onexit")
v1.resizable(0,0)

ocultar(root)
def cerrar_splashscreen():
    ejecutar(ocultar(v1))
    ejecutar(mostrar(root))
v1.after(4000,cerrar_splashscreen)
Label(v1, text="Cargando... ", bg="#1C1C1C", fg="white", font=("Arial", (16)), padx="80", pady="50").pack()
pb=ttk.Progressbar(v1, orient="horizontal", length=440, mode="determinate")
pb.pack()
pb.start()
#####################Apartir de aqui comienza todo el programa

root.title("BeesSoft") #Nombre
root.geometry("930x520") #tamaño de la ventana o 720x480
root.config(bg="#1C1C1C") #color principal #2E2E2E  #D8D8D8  #1C1C1C

barraMenu=Menu(root) #barra de menu
mnuInicio=Menu(barraMenu) #menus
mnuIndice=Menu(barraMenu)
mnuIndice_1=Menu(mnuIndice)
mnuActiv=Menu(barraMenu)
mnuAyuda=Menu(barraMenu)

####
#estas son ventanitas de dialogo#
####  Incio
def Intro():
	T=Text(root, height=5, width=90, fg="#8181F7", bg="#1C1C1C", bd=0, font=("Arial", 16, "bold"), padx=20)
	T.insert(END, "\n\nIntroducción")
	T.grid(row=1, column=0, sticky=W)
	T.config(state=DISABLED)

	T1=Text(root, height=5, width=90, fg="white", bg="#1C1C1C", bd=0, font=("Arial", 12), padx=20)
	T1.insert(END, "El término probabilidad se refiere al estudio del azar y la incertidumbre. En aquellas situaciones en las cuales se puede producir uno o varios resultados posibles, la teoría de la probabilidad proveé métodos para cuantificar la oportunidad de ocurrencia de cada uno de ellos.")
	T1.grid(row=2, column=0, sticky=W)
	T1.config(state=DISABLED)

	T2=Text(root, height=5, width=90, fg="white", bg="#1C1C1C", bd=0, font=("Arial", 12), padx=20)
	T2.insert(END, "La Estadística alude al enorme nterés de esta rama matemática para los asuntos del Estado, y su introducción en el mundo científico se debe a la importancia indiscutible para el desarrollo de las ciencias sociales y humanas. De ahí la importancia que se da en las currículas actuales de Bachillerato.")
	T2.grid(row=3, column=0, sticky=W)
	T2.config(state=DISABLED)

def informacion():
	messagebox.showinfo("Información", "Software desarrollado por TechnovaSoft.® 2015\n  •Base de datos:\n    Ernesto Ruíz\n    Alejandro Parra\n  •Interfaz gráfica:\n    Mauicio Reyes\n    Azael Rodríguez\n  •Algoritmia:\n    César Rivera\n    Carlos Hernandez")

mnuInicio.add_command(label="Introducción", command=Intro)
mnuInicio.add_command(label="Información", command=informacion)
mnuInicio.add_separator()
mnuInicio.add_command(label="Salir", command=root.destroy)
####  Indice
mnuIndice.add_command(label="1 - Conceptos generales")
mnuIndice.add_command(label="2 - Medidas de tendencia central")
mnuIndice.add_command(label="3 - Medidas de dispersión")
mnuIndice.add_command(label="4 - Medidas de forma")
mnuIndice.add_command(label="5 - Medidas de correlación")
mnuIndice.add_command(label="6 - Teoría de conjuntos")
mnuIndice.add_command(label="7 - Técnicas de conteo")
mnuIndice.add_command(label="8 - Probabilidad para eventos")
####  Actividades
mnuActiv.add_command(label="Bloque 1")
mnuActiv.add_command(label="Bloque 2")
mnuActiv.add_command(label="Bloque 3")
mnuActiv.add_command(label="Bloque 4")
mnuActiv.add_command(label="Bloque 5")
mnuActiv.add_command(label="Bloque 6")
mnuActiv.add_command(label="Bloque 7")
mnuActiv.add_command(label="Bloque 8")
####  Ayuda
def Ayuda():
	ayuda=Tk()
	ayuda.title("Ayuda")
	ayuda.geometry("320x480")
	ayuda.config(bg="white")
	text=Label(ayuda, text="Ayuda de Bee", fg="#2E2E2E", bg="white", font=("Arial", 14), padx=20, pady=20)
	text1=Label(ayuda, text="", fg="#2E2E2E", bg="white", font=("Arial", 12), padx=20)
	text.pack()
	text1.pack()

mnuAyuda.add_command(label="Ver Ayuda", command=Ayuda)
####
barraMenu.add_cascade(label="Inicio", menu=mnuInicio)
barraMenu.add_cascade(label="Índice", menu=mnuIndice)
barraMenu.add_cascade(label="Actividades", menu=mnuActiv)
barraMenu.add_cascade(label="Ayuda", menu=mnuAyuda)
root.config(menu=barraMenu)

root.mainloop() #comienzo de evento principal
