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
v1.title("BeeSoft")
v1.geometry("500x270") #450x180 
v1.config(bg="#1C1C1C")
bit=v1.iconbitmap('imagenes/icon.ico')
v1.protocol("WM_DELETE_WINDOW", "onexit")
v1.resizable(0,0)

ocultar(root)
def cerrar_splashscreen():
    ejecutar(ocultar(v1))
    ejecutar(mostrar(root))
v1.after(4000,cerrar_splashscreen)
loading=PhotoImage(file="imagenes/loading.png")
loading2=Label(v1, image=loading, bg="#1C1C1C")
loading2.pack()
pb=ttk.Progressbar(v1, orient="horizontal", length=440, mode="determinate")
pb.pack()
pb.start()


#####################Apartir de aqui comienza todo el programa

root.title("BeesSoft") #Nombre
root.geometry("930x520") #tamaño de la ventana o 720x480
root.config(bg="#1C1C1C") #color principal #2E2E2E  #D8D8D8  #1C1C1C
bit=root.iconbitmap('imagenes/icon.ico') #icono del programa


textintro=Text(root, height=1, width=36, fg="white", bg="#1C1C1C", bd=0, font=("Arial", 22, "bold"), padx=20, pady=40)
textintro.insert(END, "¡Disponible próximamente para Android!")
textintro.pack(side="top")
textintro.config(state=DISABLED)
android=PhotoImage(file="imagenes/phone.png")
android2=Label(root, image=android, bg="#1C1C1C")
android2.pack()

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
	
	textintro.pack_forget()
	android2.pack_forget()  ##elimina lo anterior en la pantalla
    
	T=Text(root, height=1, width=12, fg="#FFBF00", bg="#1C1C1C", bd=0, font=("Arial", 20, "bold"), padx=20, pady=40)
	T.insert(END, "Introducción")
	T.grid(row=1, column=0, sticky=W)
	T.config(state=DISABLED)

	T1=Text(root, height=10, width=80, fg="white", bg="#1C1C1C", bd=0, font=("Arial", 14), padx=20)
	T1.insert(END, "El término probabilidad se refiere al estudio del azar y la incertidumbre. \
	En aquellas situaciones en las cuales se puede producir uno o varios resultados posibles, la teoría de la probabilidad\
		proveé métodos para cuantificar la oportunidad de ocurrencia de cada uno de ellos.\
		\n\nLa Estadística alude al enorme interés de esta rama matemática para los asuntos del Estado,\
		y su introducción en el mundo científico se debe a la importancia indiscutible para el desarrollo de las ciencias sociales y humanas.\
	De ahí la importancia que se da en las currículas actuales de Bachillerato.")
	T1.grid(row=2, column=0, sticky=W)
	T1.config(state=DISABLED)


def informacion():
	messagebox.showinfo("Información", "Software desarrollado por TechnovaSoft.® 2015\n  •Base de datos:\n    Ernesto Ruíz\n    Alejandro Parra\n  •Interfaz gráfica:\n    Mauicio Reyes\n    Azael Rodríguez\n    Karen Ortiz\n  •Algoritmia:\n    César Rivera\n    Carlos Hernandez\n    Jorge Salinas")

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

###Funciones de las acciones en cada botón.
def bloque1():
	os.startfile("algoritmia-master\Bloque1.py") ###"os.startfile()"" inicializa y ejecuta el archivo especifícado.
def bloque2():
	os.startfile("algoritmia-master\Bloque2.py") ###Éste no sé porque no lo abre.
###NOTA: Dentro de los paréntesis poner la dirección de donde están almacenados cada uno de los Bloques.

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
	bit=ayuda.iconbitmap('imagenes/icon.ico')
	ayuda.resizable(0,0)
	ayuda.config(bg="white")
	Tayuda=Text(ayuda, height=1, width=7, fg="black", bg="white", bd=0, font=("Arial", 16, "bold italic"), padx=20, pady=40)
	Tayuda.insert(END, "Ayuda")
	Tayuda.grid(row=1, column=0, sticky=W)
	Tayuda.config(state=DISABLED)
	Tayuda2=Text(ayuda, height=100, width=40, fg="black", bg="white", bd=0, font=("Arial", 10), padx=20)
	Tayuda2.insert(END, "BeeSoft v. 1.0 BETA es software libre para los sistemas operativos Windows, MacOS, y Linux. \n\n•Requerimientos mínimos:\n512 Mbs. de memoria RAM, \
	30 Mbs. de espacio en disco duro, procesador Intel Pentium 4 o versiones posteriores; \n-Mac OS X 10.6 o posterior; \n-Ubuntu 12.04, Fedora Linux 20 o posteriores;\
	\n-Windows 7 O posterior. \n\n•Resultados: \nCuando se ingresan datos dentro de las cajas de texto y arroja un resultado erroneo o no arroja un resultado es \
	necesario verificar que se haya ingresado un dato válido, si persiste el problema, reinstale el software.\n\n¡Gracias por usar BeeSoft! :)")
	Tayuda2.grid(row=2, column=0, sticky=W)
	Tayuda2.config(state=DISABLED)


mnuAyuda.add_command(label="Ver Ayuda", command=Ayuda)
####
barraMenu.add_cascade(label="Inicio", menu=mnuInicio)
barraMenu.add_cascade(label="Índice", menu=mnuIndice)
barraMenu.add_cascade(label="Actividades", menu=mnuActiv)
barraMenu.add_cascade(label="Ayuda", menu=mnuAyuda)
root.config(menu=barraMenu)

root.mainloop() #comienzo de evento principal
