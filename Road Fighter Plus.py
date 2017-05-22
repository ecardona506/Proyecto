"""
Documentación del prototipo del juego

Procedimiento:
#Se importan todos los elementos de la libreria de tkinter de python
#Se crea una ventana llamada ventana_principal
#Se le cambia el nombre de la ventana de ventana_principal a Road Fighter Plus,
ya que el nombre por defecto es Tk
#Se le cambian las dimensiones de la ventana, de forma que tenga 950 pixeles de ancho
y 600 pixeles de alto.
#se importa una imagen que esta ubicada en la misma carpeta que este documento, la cual se
llama fondo y es de tipo PNG, dicha imagen se almacena en una variable llamada fondo_img
#se crea una etiqueta llamada Fondo ubicada en la ventana "ventana_principal", se le coloca una imagen
contenida en la variable Fondo_img, dicha etiqueta "no tiene borde", y esta ubicada en las coordenadas 0,0
#se crea 2 funciones que contiene 2 ventanas con las instrucciones del juego
#se crean varias funciones que permitiran abrir diferentes mapas, dependiendo de la dificultad seleccionada
#se importa una imagen que esta ubicada en la misma carpeta que este documento, la cual se
llama RPD y es de tipo PNG, dicha imagen se almacena en una variable llamada RPD
#se crea una etiqueta Llamada Road_Fighter ubicada en la ventana "ventana_principal", se le coloca una imagen
contenida en la variable RPD, dicha etiqueta "no tiene borde", y esta ubicada en las coordenadas 280,40
#se importa una imagen que esta ubicada en la misma carpeta que este documento, la cual se
llama Single y es de tipo PNG, dicha imagen se almacena en una variable llamada SinglePlayer
#se crea una boton Llamado solitario ubicado en la ventana "ventana_principal", se le coloca una imagen
contenida en la variable SinglePlayer, dicho botón "no tiene borde",tiene fondo negro y esta ubicado en las coordenadas 200,230
#se importa una imagen que esta ubicada en la misma carpeta que este documento, la cual se
llama Multiplayer y es de tipo PNG, dicha imagen se almacena en una variable llamada Multiplayer
#se crea una boton Llamado multiplayer ubicado en la ventana "ventana_principal", se le coloca una imagen
contenida en la variable Multiplayer, dicho botón "no tiene borde",tiene fondo negro y esta ubicado en las coordenadas 500,230
#para la selección de los niveles, se hace lo siguiente:
	#se crea una etiqueta llamada nivel, ubicada en la ventana "ventana_principal" , con fondo negro, con color de fuente blanco
	y tamaño de fuente 12, mostrando un texto que dice select level, esa ubicado en las coordenadas 100,430
	#se define una variable lvl como una variable entera
	#se crea una variable llamada lvl1, la cual almacena un radiobutton en la ventana_principal que tiene como texto 1,
	que al ser oprimido cambia de color por un verde claro, y esta ubicado en las coordenadas 200,430
	#se crea una variable llamada lvl2, la cual almacena un radiobutton en la ventana_principal que tiene como texto 2,
	que al ser oprimido cambia de color por un verde mas oscuro que el que emite el radiobutton de lvl1, y esta ubicado en las coordenadas 200,430
	#se crea una variable llamada lvl3, la cual almacena un radiobutton en la ventana_principal que tiene como texto 3,
	que al ser oprimido cambia de color por un amarillo, y esta ubicado en las coordenadas 266,430
	#se crea una variable llamada lvl4, la cual almacena un radiobutton en la ventana_principal que tiene como texto 4,
	que al ser oprimido cambia de color por un naranja, y esta ubicado en las coordenadas 299,430
	#se crea una variable llamada lvl5, la cual almacena un radiobutton en la ventana_principal que tiene como texto 5,
	que al ser oprimido cambia de color por un rojo, y esta ubicado en las coordenadas 333,430
	#cabe aclarar que solo uno de estos radiobuttons puede estar encendido, esto debido a la configuracion de value y variable que tienen
#finalmente, se hace visible la ventana con el metodo mainloop()


"""
from tkinter import *
import time
import random

ventana_principal = Tk()

# Titulo y Fondo

ventana_principal.title("Road Figther Plus")
ventana_principal.geometry("950x600")
Fondo_img = PhotoImage(file="fondo.png")
Fondo = Label(ventana_principal, image=Fondo_img, borderwidth=0, highlightthickness=0).place(x=0, y=0)

# Variables
variable_mapa = 0


# Funciones

def abrir_nivel():
    global lvl, variable_mapa
    if lvl.get() == 1:
        variable_mapa = 1
    elif lvl.get() == 2:
        variable_mapa = 2
    elif lvl.get() == 3:
        variable_mapa = 3
    elif lvl.get() == 4:
        variable_mapa = 4
    elif lvl.get() == 5:
        variable_mapa = 5


def pagina2_ayuda():
    ventana0.destroy()
    ventana_pagina2 = Tk()
    ventana_pagina2.title("Road Figther Plus")
    ventana_pagina2.geometry("950x600")
    ventana_pagina2.config(bg="#EFE4B0")

    Mensaje1 = Label(ventana_pagina2, font=(12), bg="#EFE4B0",
                     text="Instrucciones\n\nEl jugador tendrá una puntuación, la cual puede aumentar avanzando,\ncomiendo pizza o haciendo que otros skaters caigan al suelo\nacercandolos a los bordes, pero hay que ser cuidadosos,\n ya que en el intento el jugador también se puede caer."
                     , borderwidth=0, highlightthickness=0).place(x=200, y=0)

    caidas_img = PhotoImage(file="caidas.png")
    caidas = Label(ventana_pagina2, image=caidas_img, borderwidth=0, highlightthickness=0).place(x=330, y=120)

    anterior = Button(ventana0, text="anterior", font=(12), borderwidth=0, highlightthickness=0,
                      command=ayuda).place(x=150, y=550)

    ventana_pagina2.mainloop()


def ayuda():
    ventana0 = Tk()
    ventana0.title("Road Figther Plus")
    ventana0.geometry("950x600")
    ventana0.config(bg="#EFE4B0")

    Mensaje1 = Label(ventana0, font=(12), bg="#EFE4B0",
                     text="Instrucciones\n\nRoad Fighter Plus es un videojuego en el cual el jugador controla un skater \nque recorre diferentes partes de la ciudad, esquivando algunos otros \nskaters hasta llegar a su destino.\n\nPara ello, el jugador deberá ser ágil y veloz, pues al skater poco a poco\nle irá dando más y más hambre hasta el punto de no poder seguir corriendo.\nPor eso, el jugador deberá tratar de conseguir la mayor cantidad de pizza\ndurante su recorrido. Como adicional, en el camino el jugador encontrará\nciertos obstaculos que le dificultaran avanzar tales como manchas de aceite."
                     , borderwidth=0, highlightthickness=0).place(x=200, y=0)

    objetos_img = PhotoImage(file="objetos.png")
    objetos = Label(ventana0, image=objetos_img, borderwidth=0, highlightthickness=0).place(x=360, y=200)

    Mensaje2 = Label(ventana0, font=(12), bg="#EFE4B0",
                     text="Habrán 3 tipos de enemigos, los cuales tendrán comportamientos diferentes:\n El primero será el skater verde, el cual simplemente aparecerá y estorbará.\nEl segundo será el skater azul, el cual cambiara de trayectoria aleatoriamente.\nEl tercero será el skater rojo, el cual tratará siempre de hacer caer al jugador"
                     , borderwidth=0, highlightthickness=0).place(x=200, y=300)

    enemigos_img = PhotoImage(file="enemigos.png")
    Enemigos = Label(ventana0, image=enemigos_img, borderwidth=0, highlightthickness=0).place(x=370, y=400)

    siguiente = Button(ventana0, text="siguiente", font=(12), borderwidth=0, highlightthickness=0,
                       command=pagina2_ayuda).place(x=850, y=550)

    ventana0.mainloop()


def abrir_mapa_1():
    global variable_mapa
    if variable_mapa == 1 or variable_mapa == 0:
        global rival, rival_img
        ventana_principal.destroy()
        ventana_mapa1 = Tk()
        ventana_mapa1.title("Road Figther Plus")
        ventana_mapa1.geometry("950x600")
        # Mapa
        canvas_mapa = Canvas(ventana_mapa1, width=950, height=600, borderwidth=0, highlightthickness=0)
        img_mapa = PhotoImage(file="mapa.png")
        mapa = canvas_mapa.create_image(473, -900, image=img_mapa)
        global img_personaje
        img_personaje = PhotoImage(file="skate main.png")
        global personaje
        personaje = canvas_mapa.create_image(475, 510, image=img_personaje)
        global img_caidap
        img_caidap = PhotoImage(file="caida.png")
        canvas_mapa.pack()
        # barras laterales
        i = 0
        Score = Label(ventana_mapa1, text="Score", borderwidth=0, highlightthickness=0, bg="#EFE4B0",
                      font="Comic 15 bold").place(x=800, y=40)
        Hambre = Label(ventana_mapa1, text="Hunger", borderwidth=0, highlightthickness=0, bg="#EFE4B0",
                       font="Comic 15 bold").place(x=800, y=140)
        Hambre_valor = Label(ventana_mapa1, text=i, borderwidth=0, highlightthickness=0, bg="#EFE4B0",
                             font="Comic 15 bold").place(x=825, y=165)

        # Funciones
        while i <= 50:
            lista = list(time.localtime())
            if lista[5] != 0:
                if lista[5] % 1 == 0:
                    i += 2
            Hambre_valor = Label(ventana_mapa1, text=i, borderwidth=0, highlightthickness=0, bg="#EFE4B0",
                                 font="Comic 15 bold").place(x=825, y=165)

            def movimiento(event):
                global caidap, personaje, img_personaje
                if event.keysym == "Left":
                    if int(canvas_mapa.coords(personaje)[0]) > 245:
                        canvas_mapa.move(mapa, 0, 10)
                        canvas_mapa.move(personaje, -10, 0)
                        # ventana_mapa1.update()
                        print(canvas_mapa.coords(personaje))
                    else:
                        img_personaje = PhotoImage(file="caida.png")
                        personaje = canvas_mapa.create_image(245, 510, image=img_personaje)
                        ventana_mapa1.update()
                        time.sleep(1)
                        canvas_mapa.delete(personaje)
                        img_personaje = PhotoImage(file="skate main.png")
                        personaje = canvas_mapa.create_image(475, 510, image=img_personaje)

                if event.keysym == "Up":
                    if int(canvas_mapa.coords(personaje)[0]) < 715:
                        canvas_mapa.move(personaje, 10, 0)
                        canvas_mapa.move(mapa, 0, 10)
                    else:
                        img_personaje = PhotoImage(file="caida.png")
                        personaje = canvas_mapa.create_image(715, 510, image=img_personaje)
                        ventana_mapa1.update()
                        time.sleep(1)
                        canvas_mapa.delete(personaje)
                        img_personaje = PhotoImage(file="skate main.png")
                        personaje = canvas_mapa.create_image(475, 510, image=img_personaje)

                if event.keysym == "Down":
                    if int(canvas_mapa.coords(personaje)[0]) > 245:
                        canvas_mapa.move(mapa, 0, 15)
                        canvas_mapa.move(personaje, -10, 0)
                    else:
                        img_personaje = PhotoImage(file="caida.png")
                        personaje = canvas_mapa.create_image(245, 510, image=img_personaje)
                        ventana_mapa1.update()
                        time.sleep(1)
                        canvas_mapa.delete(personaje)
                        img_personaje = PhotoImage(file="skate main.png")
                        personaje = canvas_mapa.create_image(475, 510, image=img_personaje)

                if event.keysym == "Right":
                    if int(canvas_mapa.coords(personaje)[0]) < 715:
                        canvas_mapa.move(personaje, 10, 0)
                        canvas_mapa.move(mapa, 0, 15)
                    else:
                        img_personaje = PhotoImage(file="caida.png")
                        personaje = canvas_mapa.create_image(715, 510, image=img_personaje)
                        ventana_mapa1.update()
                        time.sleep(1)
                        canvas_mapa.delete(personaje)
                        img_personaje = PhotoImage(file="skate main.png")
                        personaje = canvas_mapa.create_image(475, 510, image=img_personaje)

            def enemigos():
                global rival, rival_img
                x = random.randint(1, 3)
                y = random.randint(1, 3)
                if y == 1:
                    pos = 265
                elif y == 2:
                    pos = 475
                elif y == 3:
                    pos = 685
                if x == 1:
                    rival_img = PhotoImage(file="enemigo1.png")
                    rival = canvas_mapa.create_image(pos, 100, image=rival_img)
                    for i in range(1000):
                        canvas_mapa.move(rival, 0, 0.1)
                        ventana_mapa1.update()
                elif x == 2:
                    rival_img = PhotoImage(file="enemigo2.png")
                    rival = canvas_mapa.create_image(pos, 100, image=rival_img)
                    for i in range(1000):
                        canvas_mapa.move(rival, 0, 0.1)
                        ventana_mapa1.update()
                elif x == 3:
                    rival_img = PhotoImage(file="enemigo3.png")
                    rival = canvas_mapa.create_image(pos, 100, image=rival_img)
                    for i in range(1000):
                        canvas_mapa.move(rival, 0, 0.1)
                        ventana_mapa1.update()
                print("finish")

            enemigos()
            # skate principal
            canvas_mapa.bind_all("<Up>", movimiento)
            canvas_mapa.bind_all("<Left>", movimiento)
            canvas_mapa.bind_all("<Right>", movimiento)
            canvas_mapa.bind_all("<Down>", movimiento)

        ventana_mapa1.mainloop()

    elif variable_mapa == 2:
        ventana2 = Tk()
        ventana_principal.destroy()
        ventana2.title("Road Figther Plus")
        ventana2.geometry("950x600")
        ventana2.mainloop()
    elif variable_mapa == 3:
        ventana3 = Tk()
        ventana_principal.destroy()
        ventana3.title("Road Figther Plus")
        ventana3.geometry("950x600")
        ventana3.mainloop()
    elif variable_mapa == 4:
        ventana4 = Tk()
        ventana_principal.destroy()
        ventana4.title("Road Figther Plus")
        ventana4.geometry("950x600")
        ventana4.mainloop()
    elif variable_mapa == 5:
        ventana5 = Tk()
        ventana_principal.destroy()
        ventana5.title("Road Figther Plus")
        ventana5.geometry("950x600")
        ventana5.mainloop()


# Botones

RDP = PhotoImage(file="RDP.png")
Road_fighter = Label(ventana_principal, image=RDP, borderwidth=0, highlightthickness=0).place(x=280, y=40)

SinglePlayer = PhotoImage(file="Single.png")
solitario = Button(image=SinglePlayer, bg="Black", borderwidth=0, highlightthickness=0, command=abrir_mapa_1).place(
    x=200, y=230)

MultiPlayer = PhotoImage(file="Multiplayer.png")
multiplayer = Button(image=MultiPlayer, bg="Black", borderwidth=0, highlightthickness=0).place(x=500, y=230)

How_to_play = Button(text="How to play?", font=(12), bg="Black", fg="white", activebackground="white", command=ayuda,
                     borderwidth=0, highlightthickness=0).place(x=550, y=430)

# Niveles

nivel = Label(ventana_principal, text="Select level :", font=(12), bg="black", fg="white").place(x=100, y=430)

lvl = IntVar()

lvl1 = Radiobutton(ventana_principal, text="1", activebackground="#00FF04", value=1, variable=lvl,
                   command=abrir_nivel).place(x=200, y=430)
lvl2 = Radiobutton(ventana_principal, text="2", activebackground="#62FF00", value=2, variable=lvl,
                   command=abrir_nivel).place(x=233, y=430)
lvl3 = Radiobutton(ventana_principal, text="3", activebackground="yellow", value=3, variable=lvl,
                   command=abrir_nivel).place(x=266, y=430)
lvl4 = Radiobutton(ventana_principal, text="4", activebackground="#FFA200", value=4, variable=lvl,
                   command=abrir_nivel).place(x=299, y=430)
lvl5 = Radiobutton(ventana_principal, text="5", activebackground="red", value=5, variable=lvl,
                   command=abrir_nivel).place(x=333, y=430)

ventana_principal.mainloop()