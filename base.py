from tkinter import * #libreria bonisz :3
from tkinter import messagebox #libreria para todos los messageBox
from tkinter import ttk #Libreria para barra de progreso(cargando)
import os #Libreria para comandos del sistema

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
v1.geometry("500x275") #450x180 
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

index=PhotoImage(file="imagenes/index.png")
index2=Label(root, image=index, bg="#1C1C1C")
index2.place(relx=1, rely=1, anchor=CENTER)

barraMenu=Menu(root) #barra de menu
mnuInicio=Menu(barraMenu) #menus
mnuIndice=Menu(barraMenu)
mnuActiv=Menu(barraMenu)
mnuAyuda=Menu(barraMenu)

####
#estas son ventanitas de dialogo#
####  Incio
def Intro():
	
	index2.pack_forget()  ##elimina lo anterior en la pantalla
    
	T=Text(root, height=1, width=22, fg="#FFBF00", bg="#1C1C1C", bd=0, font=("Arial", 20, "bold"), padx=20, pady=40)
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
	messagebox.showinfo("Información", "Software desarrollado por TechnovaSoft.® 2015\n  •Base de datos:\n    Ernesto Ruíz\n    Alejandro Parra\n  •Interfaz gráfica:\n    Mauicio Reyes\n    Azael Rodríguez\n    Karen Ortiz\n  •Algoritmia:\n    César Rivera\n    Jorge Salinas")

mnuInicio.add_command(label="Introducción", command=Intro)
mnuInicio.add_command(label="Información", command=informacion)
mnuInicio.add_separator()
mnuInicio.add_command(label="Salir", command=root.destroy)

def cosita1():
	T=Text(root, height=1, width=22, fg="#FFBF00", bg="#1C1C1C", bd=0, font=("Arial", 20, "bold"), padx=20, pady=40)
	T.insert(END, "Conceptos generales")
	T.grid(row=1, column=0, sticky=W)
	T.config(state=DISABLED)

	T1=Text(root, height=10, width=80, fg="white", bg="#1C1C1C", bd=0, font=("Arial", 14), padx=20)
	T1.insert(END, "México tiene una rica tradición e materia de información estadística de la cual dan cuenta diversos códices e \
innumerables publicaciones, instrucciones y personajes des de la época colonial hasta nuestros días. Esta riqueza, sin embargo, \
		no siempre es apreciada, pues se le desconoce o simplemente no conoce de manera parcial, lo cual continuamente le da lugar a omisiones o\
		 apreciaciones que no siempre tienen sustento en las evidencias históricas. Antes de continuar, debemos de especificar que es un dato categórico, \
y cual es un dato numérico. Un dato categórico es aquel que proviene de una variable aleatoria categórica, esto es, que es el resultado de una pregunta\
		de tipo cerrado como si no, blanco o negro, es decir, que la respuesta deberá ser siempre con opciones específicas. Usualmente los datos categóricos\
son utilizados también como datos no agrupados, los cuales veremos en seguida. Los datos numéricos son utilizados como datos agrupados.")
	T1.grid(row=2, column=0, sticky=W)
	T1.config(state=DISABLED)

def cosita2():
	T=Text(root, height=1, width=22, fg="#FFBF00", bg="#1C1C1C", bd=0, font=("Arial", 20, "bold"), padx=20, pady=40)
	T.insert(END, "Medidas de tendencia central")
	T.grid(row=1, column=0, sticky=W)
	T.config(state=DISABLED)

	T1=Text(root, height=10, width=80, fg="white", bg="#1C1C1C", bd=0, font=("Arial", 14), padx=20)
	T1.insert(END, "•Media aritmética:\nSe entiende por media aritmética al promedio a una serie de datos, esto es, la suma de todos los datos entre el número total de datos\
	.\n•Moda:\nCorresponde al número que más se repite en una serie de datos.\n•Mediana:\nCorresponde al número intermedio después de ordenar los datos de forma ascenderte o descendente\
	.\n•Media geométrica:\nLa media geométrica de una cantidad finita de números (digamos “N” números) es la raíz enésima del producto de todos los números\
	.\n•Media armónica:\nLa media armónica, denominada H, de una cantidad finita de números es igual al reciproco, o inverso, de la media aritmética de los recíprocos de dichos valores\
	.\n Así, dados los números  X1, X2,…X¡ con sus respectivas frecuencias absolutasN1,N2,…N¡ y siendo “N” el número total de datos.")
	T1.grid(row=2, column=0, sticky=W)
	T1.config(state=DISABLED)

def cosita3():
	T=Text(root, height=1, width=22, fg="#FFBF00", bg="#1C1C1C", bd=0, font=("Arial", 20, "bold"), padx=20, pady=40)
	T.insert(END, "Medidas de dispersión")
	T.grid(row=1, column=0, sticky=W)
	T.config(state=DISABLED)

	T1=Text(root, height=10, width=80, fg="white", bg="#1C1C1C", bd=0, font=("Arial", 14), padx=20)
	T1.insert(END, "Las medidas de dispersión, también llamadas medidas de variabilidad, muestran la variabilidad de una distribución, \
	indicando por medio de un número si las diferentes puntuaciones de una variable están muy alejadas de la media. Cuanto mayor sea ese valor, \
	mayor será la variabilidad, y cuanto menor sea, más homogénea será a la media. Así se sabe si todos los casos son parecidos o varían mucho entre ellos. \
	\n\nPara calcular la variabilidad que una distribución tiene respecto de su media, se calcula la media de las desviaciones de las puntuaciones respecto \
	a la media aritmética. Pero la suma de las desviaciones es siempre cero, así que se adoptan dos clases de estrategias para salvar este problema. \
	Una es tomando las desviaciones en valor absoluto (desviación media) y otra es tomando las desviaciones al cuadrado (varianza).")
	T1.grid(row=2, column=0, sticky=W)
	T1.config(state=DISABLED)

def cosita4():
	T=Text(root, height=1, width=22, fg="#FFBF00", bg="#1C1C1C", bd=0, font=("Arial", 20, "bold"), padx=20, pady=40)
	T.insert(END, "Medidas de forma")
	T.grid(row=1, column=0, sticky=W)
	T.config(state=DISABLED)

	T1=Text(root, height=10, width=80, fg="white", bg="#1C1C1C", bd=0, font=("Arial", 14), padx=20)
	T1.insert(END, "Las medidas de forma permiten comprobar si una distribución de frecuencia tiene características especiales como \
	simetría, asimetría, nivel de concentración de datos y nivel de apuntamiento que la clasifiquen en un tipo particular de distribución.\
	\n•Sesgo:\nMedia estadística que describe la simetría de la distribución alrededor de un promedio, esto es, el sesgo refleja el grado de \
	simetría respecto a media aritmética. \n•Curtosis:\nEs una medida estadística que describe el apuntamiento o achatamiento de una cierta distribución\
	con respecto a una distribución normal. La curtosis positiva indica una distribución relativamente apuntada, y la negativa indica una distribución relativamente achatada.")
	T1.grid(row=2, column=0, sticky=W)
	T1.config(state=DISABLED)

def cosita5():
	T=Text(root, height=1, width=22, fg="#FFBF00", bg="#1C1C1C", bd=0, font=("Arial", 20, "bold"), padx=20, pady=40)
	T.insert(END, "Medidas de correlación")
	T.grid(row=1, column=0, sticky=W)
	T.config(state=DISABLED)

	T1=Text(root, height=10, width=80, fg="white", bg="#1C1C1C", bd=0, font=("Arial", 14), padx=20)
	T1.insert(END, "Las medidas de correlación indican la fuerza y la dirección de una relación lineal y \
	proporcionalidad entre dos variables estadísticas. Se considera que dos variables cuantitativas están correlacionadas cuando\
	 los valores de una de ellas varían sistemáticamente con respecto a los valores homónimos de la otra: si tenemos dos variables (A y B) \
	 existe correlación si al aumentar los valores de A lo hacen también los de B y viceversa. La correlación entre dos variables no implica, \
	 por sí misma, ninguna relación de causalidad.\n•Regresión lineal:\nEl análisis de regresión lineal se utiliza principalmente con el propósito \
	 de hacer predicciones considerando únicamente 2 variables, una independiente (X) y una variable dependiente (y), siempre y cuando los \
valores estadísticos  graficados tengan una tendencia lineal.")
	T1.grid(row=2, column=0, sticky=W)
	T1.config(state=DISABLED)

def cosita6():
	T=Text(root, height=1, width=22, fg="#FFBF00", bg="#1C1C1C", bd=0, font=("Arial", 20, "bold"), padx=20, pady=40)
	T.insert(END, "Teoría de conjuntos")
	T.grid(row=1, column=0, sticky=W)
	T.config(state=DISABLED)

	T1=Text(root, height=10, width=80, fg="white", bg="#1C1C1C", bd=0, font=("Arial", 14), padx=20)
	T1.insert(END, "La teoría de conjuntos es una rama de las matemáticas que estudia las propiedades y relaciones de los conjuntos: \
colecciones abstractas de objetos, consideradas como objetos en sí mismas. Los conjuntos y sus operaciones más elementales son una \
		herramienta básica en la formulación de cualquier teoría matemática.\nDiagramas de Venn:\nPara efectuar operaciones con conjunto una vez \
		conocida su simbología, es recomendable conocer lo que son los diagramas de venn.\nLos diagramas de venn, llamados así en honor a su creador John venn\
		, son ilustraciones usadas en la rama de la matemática y lógica de clases, conocida como teoría de conjuntos, representando cada \
		conjunto mediante un circulo o un ovalo.")
	T1.grid(row=2, column=0, sticky=W)
	T1.config(state=DISABLED)

def cosita7():
	T=Text(root, height=1, width=22, fg="#FFBF00", bg="#1C1C1C", bd=0, font=("Arial", 20, "bold"), padx=20, pady=40)
	T.insert(END, "Técnicas de conteo")
	T.grid(row=1, column=0, sticky=W)
	T.config(state=DISABLED)

	T1=Text(root, height=10, width=80, fg="white", bg="#1C1C1C", bd=0, font=("Arial", 14), padx=20)
	T1.insert(END, "El principio fundamental en el proceso de contar ofrece un método general para contar el numero de posibles \
arreglos de objetos dentro de un solo conjunto o entre carios conjuntos. Las técnicas de conteo son aquellas que son usadas para \
	enumerar eventos difíciles de cuantificar.\nUn paso necesario para la asignación de posibilidades es la de poder identificar  \
	y contar los resultados experimentales dentro de un proceso probabilístico. Es necesario el coocimiento de ciertas reglas y métodos \
para determinar el número o la manera de formar diferentes grupos de los elementos de un conjunto.\nSi un evento A puede ocurrir de n1 \
maneras y una vez que este ha ocurrido, otro evento B puede n2 maneras diferentes entonces, el número total de formas diferentes en \
que ambos eventos pueden ocurrir en el orden indicado, es igual a  n1 x n2.")
	T1.grid(row=2, column=0, sticky=W)
	T1.config(state=DISABLED)

def cosita8():
	T=Text(root, height=1, width=22, fg="#FFBF00", bg="#1C1C1C", bd=0, font=("Arial", 20, "bold"), padx=20, pady=40)
	T.insert(END, "Probabilidad para eventos")
	T.grid(row=1, column=0, sticky=W)
	T.config(state=DISABLED)

	T1=Text(root, height=10, width=80, fg="white", bg="#1C1C1C", bd=0, font=("Arial", 14), padx=20)
	T1.insert(END, "Algunas situaciones de probabilidad implican más de un evento. Cuando los eventos no se afectan \
	entre sí, se les conoce como eventos independientes. Los eventos independientes pueden incluir la repetición de una acción como lanzar \
	un dado más de una vez, o usar dos elementos aleatorios diferentes, como lanzar una moneda y girar una ruleta. Muchas otras situaciones \
	también pueden incluir eventos independientes. \nCon frecuencia la probabilidad de un evento A se ve influenciado por la ocurrencia de otro \
	evento B. esto es, supongamos que tenemos un evento A con probabilidad P(A) y que tenemos otro evento relacionado B con probabilidad P(B). \
	Utilizamos la información del evento B para obtener una nueva probabilidad para el evento A, a esta nueva probabilidad del evento A se le \
	conoce como probabilidad condicional y se presenta  como P(A|B).")
	T1.grid(row=2, column=0, sticky=W)
	T1.config(state=DISABLED)



####  Indice
mnuIndice.add_command(label="1 - Conceptos generales", command=cosita1)
mnuIndice.add_command(label="2 - Medidas de tendencia central", command=cosita2)
mnuIndice.add_command(label="3 - Medidas de dispersión", command=cosita3)
mnuIndice.add_command(label="4 - Medidas de forma", command=cosita4)
mnuIndice.add_command(label="5 - Medidas de correlación", command=cosita5)
mnuIndice.add_command(label="6 - Teoría de conjuntos", command=cosita6)
mnuIndice.add_command(label="7 - Técnicas de conteo", command=cosita7)
mnuIndice.add_command(label="8 - Probabilidad para eventos", command=cosita8)

###Funciones de las acciones en cada botón.
def bloque1():
	os.startfile("algoritmia\Bloque1.py")
def bloque2():
	os.startfile("algoritmia\Bloque2.py")
def bloque3():
	os.startfile("algoritmia\Bloque3.py")
def bloque4():
	os.startfile("algoritmia\Bloque4.py")
def bloque5():
	os.startfile("algoritmia\Bloque5.py")
def bloque6():
	os.startfile("algoritmia\Bloque6.py")
def bloque7():
	os.startfile("algoritmia\Bloque7.py")
def bloque8():
	os.startfile("algoritmia\Bloque8.py")

####  Actividades
mnuActiv.add_command(label="Bloque 1", command=bloque1)
mnuActiv.add_command(label="Bloque 2", command=bloque2)
mnuActiv.add_command(label="Bloque 3", command=bloque3)
mnuActiv.add_command(label="Bloque 4", command=bloque4)
mnuActiv.add_command(label="Bloque 5", command=bloque5)
mnuActiv.add_command(label="Bloque 6", command=bloque6)
mnuActiv.add_command(label="Bloque 7", command=bloque7)
mnuActiv.add_command(label="Bloque 8", command=bloque8)

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
	Tayuda2.insert(END, "BeeSoft v. 1.0 BETA es software libre para los sistemas operativos Windows, MacOS, Linux y Solaris. \n\n•Requerimientos mínimos:\n32Gb de memoria RAM, \
	5 Tbs. de espacio en disco duro, procesador Intel Xeon E5 64 nucleos, 3 monitores 8K sincronizados, Internet LiFi 1024 mbps de velocidad; \n-Mac OS X 10.6 o posterior; \n-Ubuntu 12.04, Fedora Linux 20 o posteriores;\
	\n-Windows 7 o posterior. \n\n•Resultados: \nCuando se ingresan datos dentro de las cajas de texto y arroja un resultado erroneo o no arroja un resultado es \
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
