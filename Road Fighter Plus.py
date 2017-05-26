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
estadopag2 = 0
puntaje = 0


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
    global ventana0, estadopag2, ventana_pagina2
    estadopag2 = 1
    ventana0.destroy()
    ventana_pagina2 = Toplevel()
    ventana_pagina2.title("Road Figther Plus")
    ventana_pagina2.geometry("950x600")
    ventana_pagina2.config(bg="#EFE4B0")

    Mensaje1 = Label(ventana_pagina2, font=(12), bg="#EFE4B0",
                     text="Instrucciones\n\nEl jugador tendrá una puntuación, la cual puede aumentar avanzando,\ncomiendo pizza o haciendo que otros skaters caigan al suelo\nacercandolos a los bordes, pero hay que ser cuidadosos,\n ya que en el intento el jugador también se puede caer."
                     , borderwidth=0, highlightthickness=0).place(x=200, y=0)

    caidas_img = PhotoImage(file="caidas.png")
    caidas = Label(ventana_pagina2, image=caidas_img, borderwidth=0, highlightthickness=0).place(x=330, y=120)

    anterior = Button(ventana_pagina2, text="anterior", font=(12), borderwidth=0, highlightthickness=0,
                      command=ayuda).place(x=150, y=550)

    ventana_pagina2.mainloop()


def ayuda():
    global ventana0, estadopag2, ventana_pagina2
    if estadopag2 == 1:
        ventana_pagina2.destroy()
        estadopag2 = 0
    ventana_principal.iconify()
    ventana0 = Toplevel()
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
    global variable_mapa, puntaje, entrada, i
    if variable_mapa == 1 or variable_mapa == 0:
        global rival, rival_img
        ventana_principal.destroy()
        ventana_mapa1 = Tk()
        ventana_mapa1.title("Road Figther Plus")
        ventana_mapa1.geometry("950x600")
        # Mapa e interfaz del jugador
        canvas_mapa = Canvas(ventana_mapa1, width=950, height=600, borderwidth=0, highlightthickness=0)
        img_mapa = PhotoImage(file="mapa.png")
        mapa = canvas_mapa.create_image(473, -2400, image=img_mapa)
        global img_personaje
        img_personaje = PhotoImage(file="skate main.png")
        global personaje
        personaje = canvas_mapa.create_image(475, 510, image=img_personaje)
        global img_caidap
        img_caidap = PhotoImage(file="caida.png")
        canvas_mapa.pack()
        # barras laterales
        i = 0
        texto_nombre = entrada.get()
        nombre_valor = Label(ventana_mapa1, text=texto_nombre, borderwidth=0, highlightthickness=0, bg="#EFE4B0",
                             font="Comic 15 bold").place(x=805, y=45)
        Score = Label(ventana_mapa1, text="Score", borderwidth=0, highlightthickness=0, bg="#EFE4B0",
                      font="Comic 15 bold").place(x=805, y=100)
        Score_valor = Label(ventana_mapa1, text=puntaje, borderwidth=0, highlightthickness=0, bg="#EFE4B0",
                            font="Comic 15 bold").place(x=815, y=125)
        Hambre = Label(ventana_mapa1, text="Hunger", borderwidth=0, highlightthickness=0, bg="#EFE4B0",
                       font="Comic 15 bold").place(x=800, y=180)
        Hambre_valor = Label(ventana_mapa1, text=i, borderwidth=0, highlightthickness=0, bg="#EFE4B0",
                             font="Comic 15 bold").place(x=825, y=205)

        # Funciones

        while i <= 98:
            lista = list(time.localtime())
            if lista[5] != 0:
                if lista[5] % 1 == 0:
                    i += 2
            Hambre_valor = Label(ventana_mapa1, text=i, borderwidth=0, highlightthickness=0, bg="#EFE4B0",
                                 font="Comic 15 bold").place(x=825, y=205)

            global vel
            vel = 0
            canvas_mapa.after(1)

            def enemigos():
                def movimiento(event):
                    global caidap, personaje, img_personaje, vel, i
                    if event.keysym == "Left":
                        if i < 100:
                            if int(canvas_mapa.coords(personaje)[0]) > 247:
                                canvas_mapa.move(personaje, 0 - vel, 0)
                                canvas_mapa.move(mapa, 0, 0 + vel)
                                vel += 0.1
                            else:
                                img_personaje = PhotoImage(file="caida.png")
                                personaje = canvas_mapa.create_image(245, 510, image=img_personaje)
                                ventana_mapa1.update()
                                canvas_mapa.after(100)
                                canvas_mapa.delete(personaje)
                                img_personaje = PhotoImage(file="skate main.png")
                                personaje = canvas_mapa.create_image(475, 510, image=img_personaje)
                                i += 10
                                if i > 100:
                                    i = 100
                                Hambre_valor = Label(ventana_mapa1, text=i, borderwidth=0, highlightthickness=0,
                                                     bg="#EFE4B0",
                                                     font="Comic 15 bold").place(x=825, y=205)

                    if event.keysym == "Up":
                        if i < 100:
                            if int(canvas_mapa.coords(personaje)[0]) < 715:
                                canvas_mapa.move(personaje, 0 + vel, 0)
                                canvas_mapa.move(mapa, 0, 0 + vel)
                                vel += 0.1
                            else:
                                img_personaje = PhotoImage(file="caida.png")
                                personaje = canvas_mapa.create_image(715, 510, image=img_personaje)
                                ventana_mapa1.update()
                                canvas_mapa.after(100)
                                canvas_mapa.delete(personaje)
                                img_personaje = PhotoImage(file="skate main.png")
                                personaje = canvas_mapa.create_image(475, 510, image=img_personaje)
                                i += 10
                                if i > 100:
                                    i = 100
                                Hambre_valor = Label(ventana_mapa1, text=i, borderwidth=0, highlightthickness=0,
                                                     bg="#EFE4B0",
                                                     font="Comic 15 bold").place(x=825, y=205)
                    if event.keysym == "Down":
                        if i < 100:
                            if int(canvas_mapa.coords(personaje)[0]) > 245:
                                vel += 0.2
                                canvas_mapa.move(mapa, 0, vel)
                                canvas_mapa.move(personaje, -vel, 0)
                            else:
                                img_personaje = PhotoImage(file="caida.png")
                                personaje = canvas_mapa.create_image(245, 510, image=img_personaje)
                                ventana_mapa1.update()
                                canvas_mapa.after(100)
                                canvas_mapa.delete(personaje)
                                img_personaje = PhotoImage(file="skate main.png")
                                personaje = canvas_mapa.create_image(475, 510, image=img_personaje)
                                i += 10
                                if i > 100:
                                    i = 100
                                Hambre_valor = Label(ventana_mapa1, text=i, borderwidth=0, highlightthickness=0,
                                                     bg="#EFE4B0",
                                                     font="Comic 15 bold").place(x=825, y=205)
                    if event.keysym == "Right":
                        if i < 100:
                            if int(canvas_mapa.coords(personaje)[0]) < 715:
                                vel += 0.2
                                canvas_mapa.move(personaje, vel, 0)
                                canvas_mapa.move(mapa, 0, vel)
                            else:
                                img_personaje = PhotoImage(file="caida.png")
                                personaje = canvas_mapa.create_image(715, 510, image=img_personaje)
                                ventana_mapa1.update()
                                canvas_mapa.after(500)
                                canvas_mapa.delete(personaje)
                                img_personaje = PhotoImage(file="skate main.png")
                                personaje = canvas_mapa.create_image(470, 510, image=img_personaje)
                                i += 10
                                if i > 100:
                                    i = 100
                                Hambre_valor = Label(ventana_mapa1, text=i, borderwidth=0, highlightthickness=0,
                                                     bg="#EFE4B0",
                                                     font="Comic 15 bold").place(x=825, y=205)

                canvas_mapa.bind_all("<Up>", movimiento)
                canvas_mapa.bind_all("<Left>", movimiento)
                canvas_mapa.bind_all("<Right>", movimiento)
                canvas_mapa.bind_all("<Down>", movimiento)

                global rival, rival_img, puntaje, i
                x = random.randint(1, 3)
                y = random.randint(1, 3)
                w = random.randint(1, 2)
                z = random.randint(1, 2)
                objeto = StringVar()
                if z == 1:
                    trap_or_treasure = 345
                else:
                    trap_or_treasure = 617
                tinta_o_pizza = random.randint(1, 10)
                if tinta_o_pizza == 3:
                    obstaculo_img = PhotoImage(file="pizza.png")
                    obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                    objeto = "pizza"
                elif tinta_o_pizza == 8:
                    obstaculo_img = PhotoImage(file="mancha.png")
                    obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                    objeto = "mancha"
                else:
                    obstaculo_img = PhotoImage(file="vacio.png")
                    obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                if w == 1:
                    desp = 0.1
                elif w == 2:
                    desp = -0.1
                if y == 1:
                    pos = 265
                elif y == 2:
                    pos = 470
                elif y == 3:
                    pos = 685
                # Enemigo 1
                if x == 1:
                    rival_img = PhotoImage(file="enemigo1.png")
                    rival = canvas_mapa.create_image(pos, 0, image=rival_img)
                    while canvas_mapa.coords(rival)[1] < 640:
                        canvas_mapa.move(rival, 0, 0.1)
                        canvas_mapa.move(obstaculo, 0, 0.1)
                        if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                            if objeto == "pizza":
                                puntaje += 500
                                Score_valor = Label(ventana_mapa1, text=puntaje, borderwidth=0, highlightthickness=0,
                                                    bg="#EFE4B0", font="Comic 15 bold").place(x=815, y=125)
                                i -= 10
                                if i < 0:
                                    i = 0
                                obstaculo_img = PhotoImage(file="vacio.png")
                                obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                                Hambre_valor = Label(ventana_mapa1, text=i, borderwidth=0, highlightthickness=0,
                                                     bg="#EFE4B0",
                                                     font="Comic 15 bold").place(x=825, y=205)
                        ventana_mapa1.update()
                # Enemigo 2
                elif x == 2:
                    rival_img = PhotoImage(file="enemigo2.png")
                    rival = canvas_mapa.create_image(pos, 0, image=rival_img)
                    pos_y = canvas_mapa.coords(personaje)[1]
                    if pos == 265:
                        while canvas_mapa.coords(rival)[1] < 550:
                            if canvas_mapa.coords(rival)[1] < 240:
                                canvas_mapa.move(rival, 0, 0.1)
                                canvas_mapa.move(obstaculo, 0, 0.1)
                                if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                    if objeto == "pizza":
                                        puntaje += 500
                                        Score_valor = Label(ventana_mapa1, text=puntaje, borderwidth=0,
                                                            highlightthickness=0,
                                                            bg="#EFE4B0", font="Comic 15 bold").place(x=815, y=125)
                                        i -= 10
                                        if i < 0:
                                            i = 0
                                        obstaculo_img = PhotoImage(file="vacio.png")
                                        obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                                        Hambre_valor = Label(ventana_mapa1, text=i, borderwidth=0, highlightthickness=0,
                                                             bg="#EFE4B0",
                                                             font="Comic 15 bold").place(x=825, y=205)
                                ventana_mapa1.update()
                            elif canvas_mapa.coords(rival)[1] > 240 and canvas_mapa.coords(rival)[1] < 550:
                                canvas_mapa.move(rival, 0.07, 0.1)
                                canvas_mapa.move(obstaculo, 0, 0.1)
                                if canvas_mapa.coords(obstaculo)[1] + 100 > canvas_mapa.coords(personaje)[1]:
                                    if objeto == "pizza":
                                        puntaje += 500
                                        Score_valor = Label(ventana_mapa1, text=puntaje, borderwidth=0,
                                                            highlightthickness=0, bg="#EFE4B0",
                                                            font="Comic 15 bold").place(x=815, y=125)
                                        i -= 10
                                        if i < 0:
                                            i = 0
                                        obstaculo_img = PhotoImage(file="vacio.png")
                                        obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                                        Hambre_valor = Label(ventana_mapa1, text=i, borderwidth=0, highlightthickness=0,
                                                             bg="#EFE4B0",
                                                             font="Comic 15 bold").place(x=825, y=205)
                                ventana_mapa1.update()
                    elif pos == 470:
                        while canvas_mapa.coords(rival)[1] < 550:
                            if canvas_mapa.coords(rival)[1] < 240:
                                canvas_mapa.move(rival, 0, 0.1)
                                canvas_mapa.move(obstaculo, 0, 0.1)
                                if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                    if objeto == "pizza":
                                        puntaje += 500
                                        Score_valor = Label(ventana_mapa1, text=puntaje, borderwidth=0,
                                                            highlightthickness=0, bg="#EFE4B0",
                                                            font="Comic 15 bold").place(x=815, y=125)
                                        i -= 10
                                        if i < 0:
                                            i = 0
                                        obstaculo_img = PhotoImage(file="vacio.png")
                                        obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                                        Hambre_valor = Label(ventana_mapa1, text=i, borderwidth=0, highlightthickness=0,
                                                             bg="#EFE4B0",
                                                             font="Comic 15 bold").place(x=825, y=205)
                                ventana_mapa1.update()
                            elif canvas_mapa.coords(rival)[1] > 240 and canvas_mapa.coords(rival)[1] < 550:
                                canvas_mapa.move(rival, desp, 0.1)
                                canvas_mapa.move(obstaculo, 0, 0.1)
                                if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                    if objeto == "pizza":
                                        puntaje += 500
                                        Score_valor = Label(ventana_mapa1, text=puntaje, borderwidth=0,
                                                            highlightthickness=0, bg="#EFE4B0",
                                                            font="Comic 15 bold").place(x=815, y=125)
                                        i -= 10
                                        if i < 0:
                                            i = 0
                                        obstaculo_img = PhotoImage(file="vacio.png")
                                        obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                                        Hambre_valor = Label(ventana_mapa1, text=i, borderwidth=0, highlightthickness=0,
                                                             bg="#EFE4B0",
                                                             font="Comic 15 bold").place(x=825, y=205)
                                ventana_mapa1.update()
                    else:
                        while canvas_mapa.coords(rival)[1] < 550:
                            if canvas_mapa.coords(rival)[1] < 240:
                                canvas_mapa.move(rival, 0, 0.1)
                                canvas_mapa.move(obstaculo, 0, 0.1)
                                if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                    if objeto == "pizza":
                                        puntaje += 500
                                        Score_valor = Label(ventana_mapa1, text=puntaje, borderwidth=0,
                                                            highlightthickness=0, bg="#EFE4B0",
                                                            font="Comic 15 bold").place(x=815, y=125)
                                        i -= 10
                                        if i < 0:
                                            i = 0
                                        obstaculo_img = PhotoImage(file="vacio.png")
                                        obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                                        Hambre_valor = Label(ventana_mapa1, text=i, borderwidth=0, highlightthickness=0,
                                                             bg="#EFE4B0",
                                                             font="Comic 15 bold").place(x=825, y=205)
                                ventana_mapa1.update()
                            elif canvas_mapa.coords(rival)[1] > 240 and canvas_mapa.coords(rival)[1] < 550:
                                canvas_mapa.move(rival, -0.07, 0.1)
                                canvas_mapa.move(obstaculo, 0, 0.1)
                                if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                    if canvas_mapa.coords(obstaculo)[0] - 5 > canvas_mapa.coords(personaje)[0] and \
                                                            canvas_mapa.coords(obstaculo)[0] + 5 < \
                                                    canvas_mapa.coords(personaje)[0]:
                                        if objeto == "pizza":
                                            puntaje += 500
                                            Score_valor = Label(ventana_mapa1, text=puntaje, borderwidth=0,
                                                                highlightthickness=0, bg="#EFE4B0",
                                                                font="Comic 15 bold").place(x=815, y=125)
                                            i -= 10
                                            if i < 0:
                                                i = 0
                                            obstaculo_img = PhotoImage(file="vacio.png")
                                            obstaculo = canvas_mapa.create_image(trap_or_treasure, 0,
                                                                                 image=obstaculo_img)
                                            Hambre_valor = Label(ventana_mapa1, text=i, borderwidth=0,
                                                                 highlightthickness=0,
                                                                 bg="#EFE4B0",
                                                                 font="Comic 15 bold").place(x=825, y=205)
                                ventana_mapa1.update()
                # Enemigo 3
                elif x == 3:
                    rival_img = PhotoImage(file="enemigo3.png")
                    rival = canvas_mapa.create_image(pos, 0, image=rival_img)
                    if pos == 470:
                        while canvas_mapa.coords(rival)[1] < 550:
                            if canvas_mapa.coords(rival)[1] < 240:
                                canvas_mapa.move(rival, 0, 0.1)
                                canvas_mapa.move(obstaculo, 0, 0.1)
                                if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                    # if canvas_mapa.coords(obstaculo)[0] - 5 > canvas_mapa.coords(personaje)[0] and canvas_mapa.coords(obstaculo)[0] + 5 < canvas_mapa.coords(personaje)[0]:
                                    if objeto.get() == "pizza":
                                        puntaje += 500
                                        Score_valor = Label(ventana_mapa1, text=puntaje, borderwidth=0,
                                                            highlightthickness=0, bg="#EFE4B0",
                                                            font="Comic 15 bold").place(x=815, y=125)
                                        i -= 10
                                        if i < 0:
                                            i = 0
                                        obstaculo_img = PhotoImage(file="vacio.png")
                                        obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                                        Hambre_valor = Label(ventana_mapa1, text=i, borderwidth=0, highlightthickness=0,
                                                             bg="#EFE4B0",
                                                             font="Comic 15 bold").place(x=825, y=205)
                                ventana_mapa1.update()
                            elif canvas_mapa.coords(rival)[1] > 240 and canvas_mapa.coords(rival)[1] < 550:
                                if canvas_mapa.coords(rival)[1] > 240 and canvas_mapa.coords(rival)[1] < 550:
                                    if canvas_mapa.coords(personaje)[0] > 245 and canvas_mapa.coords(personaje)[
                                        0] < 440:
                                        canvas_mapa.move(rival, -0.07, 0.1)
                                        canvas_mapa.move(obstaculo, 0, 0.1)
                                        if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                            if objeto == "pizza":
                                                puntaje += 500
                                                Score_valor = Label(ventana_mapa1, text=puntaje, borderwidth=0,
                                                                    highlightthickness=0, bg="#EFE4B0",
                                                                    font="Comic 15 bold").place(x=815, y=125)
                                                i -= 10
                                                if i < 0:
                                                    i = 0
                                                obstaculo_img = PhotoImage(file="vacio.png")
                                                obstaculo = canvas_mapa.create_image(trap_or_treasure, 0,
                                                                                     image=obstaculo_img)
                                                Hambre_valor = Label(ventana_mapa1, text=i, borderwidth=0,
                                                                     highlightthickness=0,
                                                                     bg="#EFE4B0",
                                                                     font="Comic 15 bold").place(x=825, y=205)
                                        ventana_mapa1.update()
                                    elif canvas_mapa.coords(personaje)[0] >= 440 and canvas_mapa.coords(personaje)[
                                        0] < 480:
                                        canvas_mapa.move(rival, 0, 0.1)
                                        canvas_mapa.move(obstaculo, 0, 0.1)
                                        if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                            if objeto == "pizza":
                                                puntaje += 500
                                                Score_valor = Label(ventana_mapa1, text=puntaje, borderwidth=0,
                                                                    highlightthickness=0, bg="#EFE4B0",
                                                                    font="Comic 15 bold").place(x=815, y=125)
                                                i -= 10
                                                if i < 0:
                                                    i = 0
                                                obstaculo_img = PhotoImage(file="vacio.png")
                                                obstaculo = canvas_mapa.create_image(trap_or_treasure, 0,
                                                                                     image=obstaculo_img)
                                                Hambre_valor = Label(ventana_mapa1, text=i, borderwidth=0,
                                                                     highlightthickness=0,
                                                                     bg="#EFE4B0",
                                                                     font="Comic 15 bold").place(x=825, y=205)
                                        ventana_mapa1.update()
                                    elif canvas_mapa.coords(personaje)[0] >= 480 and canvas_mapa.coords(personaje)[
                                        0] < 715:
                                        canvas_mapa.move(rival, 0.07, 0.1)
                                        canvas_mapa.move(obstaculo, 0, 0.1)
                                        ventana_mapa1.update()
                    elif pos == 265:
                        while canvas_mapa.coords(rival)[1] < 550:
                            if canvas_mapa.coords(rival)[1] < 240:
                                canvas_mapa.move(rival, 0, 0.1)
                                canvas_mapa.move(obstaculo, 0, 0.1)
                                if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                    if objeto == "pizza":
                                        puntaje += 500
                                        Score_valor = Label(ventana_mapa1, text=puntaje, borderwidth=0,
                                                            highlightthickness=0, bg="#EFE4B0",
                                                            font="Comic 15 bold").place(x=815, y=125)
                                        i -= 10
                                        if i < 0:
                                            i = 0
                                        obstaculo_img = PhotoImage(file="vacio.png")
                                        obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                                        Hambre_valor = Label(ventana_mapa1, text=i, borderwidth=0, highlightthickness=0,
                                                             bg="#EFE4B0",
                                                             font="Comic 15 bold").place(x=825, y=205)
                                        ventana_mapa1.update()
                            elif canvas_mapa.coords(rival)[1] > 240 and canvas_mapa.coords(rival)[1] < 550:
                                if canvas_mapa.coords(rival)[1] > 240 and canvas_mapa.coords(rival)[1] < 550:
                                    if canvas_mapa.coords(personaje)[0] > 245 and canvas_mapa.coords(personaje)[
                                        0] < 460:
                                        canvas_mapa.move(rival, 0, 0.1)
                                        canvas_mapa.move(obstaculo, 0, 0.1)
                                        if canvas_mapa.coords(obstaculo)[1] + 100 > canvas_mapa.coords(personaje)[1]:
                                            if objeto == "pizza":
                                                puntaje += 500
                                                Score_valor = Label(ventana_mapa1, text=puntaje, borderwidth=0,
                                                                    highlightthickness=0, bg="#EFE4B0",
                                                                    font="Comic 15 bold").place(x=815, y=125)
                                                i -= 10
                                                if i < 0:
                                                    i = 0
                                                obstaculo_img = PhotoImage(file="vacio.png")
                                                obstaculo = canvas_mapa.create_image(trap_or_treasure, 0,
                                                                                     image=obstaculo_img)
                                                Hambre_valor = Label(ventana_mapa1, text=i, borderwidth=0,
                                                                     highlightthickness=0,
                                                                     bg="#EFE4B0",
                                                                     font="Comic 15 bold").place(x=825, y=205)
                                        ventana_mapa1.update()
                                    elif canvas_mapa.coords(personaje)[0] >= 460 and canvas_mapa.coords(personaje)[
                                        0] < 480:
                                        canvas_mapa.move(rival, 0.07, 0.1)
                                        canvas_mapa.move(obstaculo, 0, 0.1)
                                        if canvas_mapa.coords(obstaculo)[1] + 100 > canvas_mapa.coords(personaje)[1]:
                                            if objeto == "pizza":
                                                puntaje += 500
                                                Score_valor = Label(ventana_mapa1, text=puntaje, borderwidth=0,
                                                                    highlightthickness=0, bg="#EFE4B0",
                                                                    font="Comic 15 bold").place(x=815, y=125)
                                                i -= 10
                                                if i < 0:
                                                    i = 0
                                                obstaculo_img = PhotoImage(file="vacio.png")
                                                obstaculo = canvas_mapa.create_image(trap_or_treasure, 0,
                                                                                     image=obstaculo_img)
                                                Hambre_valor = Label(ventana_mapa1, text=i, borderwidth=0,
                                                                     highlightthickness=0,
                                                                     bg="#EFE4B0",
                                                                     font="Comic 15 bold").place(x=825, y=205)
                                        ventana_mapa1.update()
                                    elif canvas_mapa.coords(personaje)[0] >= 480 and canvas_mapa.coords(personaje)[
                                        0] < 715:
                                        canvas_mapa.move(rival, 0.07, 0.1)
                                        canvas_mapa.move(obstaculo, 0, 0.1)
                                        if canvas_mapa.coords(obstaculo)[1] + 100 > canvas_mapa.coords(personaje)[1]:
                                            if objeto == "pizza":
                                                puntaje += 500
                                                Score_valor = Label(ventana_mapa1, text=puntaje, borderwidth=0,
                                                                    highlightthickness=0, bg="#EFE4B0",
                                                                    font="Comic 15 bold").place(x=815, y=125)
                                                i -= 10
                                                if i < 0:
                                                    i = 0
                                                obstaculo_img = PhotoImage(file="vacio.png")
                                                obstaculo = canvas_mapa.create_image(trap_or_treasure, 0,
                                                                                     image=obstaculo_img)
                                                Hambre_valor = Label(ventana_mapa1, text=i, borderwidth=0,
                                                                     highlightthickness=0,
                                                                     bg="#EFE4B0",
                                                                     font="Comic 15 bold").place(x=825, y=205)
                                        ventana_mapa1.update()
                    else:
                        while canvas_mapa.coords(rival)[1] < 550:
                            if canvas_mapa.coords(rival)[1] < 240:
                                canvas_mapa.move(rival, 0, 0.1)
                                canvas_mapa.move(obstaculo, 0, 0.1)
                                if canvas_mapa.coords(obstaculo)[1] + 100 > canvas_mapa.coords(personaje)[1]:
                                    if objeto == "pizza":
                                        puntaje += 500
                                        Score_valor = Label(ventana_mapa1, text=puntaje, borderwidth=0,
                                                            highlightthickness=0, bg="#EFE4B0",
                                                            font="Comic 15 bold").place(x=815, y=125)
                                        i -= 10
                                        if i < 0:
                                            i = 0
                                        obstaculo_img = PhotoImage(file="vacio.png")
                                        obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                                        Hambre_valor = Label(ventana_mapa1, text=i, borderwidth=0, highlightthickness=0,
                                                             bg="#EFE4B0",
                                                             font="Comic 15 bold").place(x=825, y=205)
                                ventana_mapa1.update()
                            elif canvas_mapa.coords(rival)[1] > 240 and canvas_mapa.coords(rival)[1] < 550:
                                if canvas_mapa.coords(rival)[1] > 240 and canvas_mapa.coords(rival)[1] < 550:
                                    if canvas_mapa.coords(personaje)[0] > 245 and canvas_mapa.coords(personaje)[
                                        0] < 460:
                                        canvas_mapa.move(rival, -0.07, 0.1)
                                        canvas_mapa.move(obstaculo, 0, 0.1)
                                        if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                            if objeto == "pizza":
                                                puntaje += 500
                                                Score_valor = Label(ventana_mapa1, text=puntaje, borderwidth=0,
                                                                    highlightthickness=0, bg="#EFE4B0",
                                                                    font="Comic 15 bold").place(x=815, y=125)
                                                i -= 10
                                                if i < 0:
                                                    i = 0
                                                obstaculo_img = PhotoImage(file="vacio.png")
                                                obstaculo = canvas_mapa.create_image(trap_or_treasure, 0,
                                                                                     image=obstaculo_img)
                                                Hambre_valor = Label(ventana_mapa1, text=i, borderwidth=0,
                                                                     highlightthickness=0,
                                                                     bg="#EFE4B0",
                                                                     font="Comic 15 bold").place(x=825, y=205)
                                        ventana_mapa1.update()
                                    elif canvas_mapa.coords(personaje)[0] >= 460 and canvas_mapa.coords(personaje)[
                                        0] < 480:
                                        canvas_mapa.move(rival, -0.07, 0.1)
                                        canvas_mapa.move(obstaculo, 0, 0.1)
                                        if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                            if objeto == "pizza":
                                                puntaje += 500
                                                Score_valor = Label(ventana_mapa1, text=puntaje, borderwidth=0,
                                                                    highlightthickness=0, bg="#EFE4B0",
                                                                    font="Comic 15 bold").place(x=815, y=125)
                                                i -= 10
                                                if i < 0:
                                                    i = 0
                                                obstaculo_img = PhotoImage(file="vacio.png")
                                                obstaculo = canvas_mapa.create_image(trap_or_treasure, 0,
                                                                                     image=obstaculo_img)
                                                Hambre_valor = Label(ventana_mapa1, text=i, borderwidth=0,
                                                                     highlightthickness=0,
                                                                     bg="#EFE4B0",
                                                                     font="Comic 15 bold").place(x=825, y=205)
                                        ventana_mapa1.update()
                                    elif canvas_mapa.coords(personaje)[0] >= 480 and canvas_mapa.coords(personaje)[
                                        0] < 715:
                                        canvas_mapa.move(rival, 0, 0.1)
                                        canvas_mapa.move(obstaculo, 0, 0.1)
                                        if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                            if objeto == "pizza":
                                                puntaje += 500
                                                Score_valor = Label(ventana_mapa1, text=puntaje, borderwidth=0,
                                                                    highlightthickness=0, bg="#EFE4B0",
                                                                    font="Comic 15 bold").place(x=815, y=125)
                                                i -= 10
                                                if i < 0:
                                                    i = 0
                                                obstaculo_img = PhotoImage(file="vacio.png")
                                                obstaculo = canvas_mapa.create_image(trap_or_treasure, 0,
                                                                                     image=obstaculo_img)
                                                Hambre_valor = Label(ventana_mapa1, text=i, borderwidth=0,
                                                                     highlightthickness=0,
                                                                     bg="#EFE4B0",
                                                                     font="Comic 15 bold").place(x=825, y=205)
                                        ventana_mapa1.update()

            enemigos()

        ventana_mapa1.mainloop()
    # Segundo mapa
    elif variable_mapa == 2:
        global rival, rival_img
        ventana_principal.destroy()
        ventana2 = Tk()
        ventana2.title("Road Figther Plus")
        ventana2.geometry("950x600")
        # Mapa e interfaz del jugador
        canvas_mapa = Canvas(ventana2, width=950, height=600, borderwidth=0, highlightthickness=0)
        img_mapa = PhotoImage(file="mapa2.png")
        mapa = canvas_mapa.create_image(473, -2400, image=img_mapa)
        # global img_personaje
        img_personaje = PhotoImage(file="skate main.png")
        personaje = canvas_mapa.create_image(475, 510, image=img_personaje)
        img_caidap = PhotoImage(file="caida.png")
        canvas_mapa.pack()
        # barras laterales
        i = 0
        texto_nombre = entrada.get()
        nombre_valor = Label(ventana2, text=texto_nombre, borderwidth=0, highlightthickness=0, bg="#EFE4B0",
                             font="Comic 15 bold").place(x=805, y=45)
        Score = Label(ventana2, text="Score", borderwidth=0, highlightthickness=0, bg="#EFE4B0",
                      font="Comic 15 bold").place(x=805, y=100)
        Score_valor = Label(ventana2, text=puntaje, borderwidth=0, highlightthickness=0, bg="#EFE4B0",
                            font="Comic 15 bold").place(x=815, y=125)
        Hambre = Label(ventana2, text="Hunger", borderwidth=0, highlightthickness=0, bg="#EFE4B0",
                       font="Comic 15 bold").place(x=800, y=180)
        Hambre_valor = Label(ventana2, text=i, borderwidth=0, highlightthickness=0, bg="#EFE4B0",
                             font="Comic 15 bold").place(x=825, y=205)

        # Funciones

        while i <= 98:
            lista = list(time.localtime())
            if lista[5] != 0:
                if lista[5] % 1 == 0:
                    i += 2
            Hambre_valor = Label(ventana2, text=i, borderwidth=0, highlightthickness=0, bg="#EFE4B0",
                                 font="Comic 15 bold").place(x=825, y=205)

            vel = 0
            canvas_mapa.after(1)

            def enemigos():
                def movimiento(event):
                    global caidap, personaje, img_personaje, vel, i
                    if event.keysym == "Left":
                        if i < 100:
                            if int(canvas_mapa.coords(personaje)[0]) > 247:
                                canvas_mapa.move(personaje, 0 - vel, 0)
                                canvas_mapa.move(mapa, 0, 0 + vel)
                                vel += 0.1
                            else:
                                img_personaje = PhotoImage(file="caida.png")
                                personaje = canvas_mapa.create_image(245, 510, image=img_personaje)
                                ventana2.update()
                                canvas_mapa.after(100)
                                canvas_mapa.delete(personaje)
                                img_personaje = PhotoImage(file="skate main.png")
                                personaje = canvas_mapa.create_image(475, 510, image=img_personaje)
                                i += 10
                                if i > 100:
                                    i = 100
                                Hambre_valor = Label(ventana2, text=i, borderwidth=0, highlightthickness=0,
                                                     bg="#EFE4B0",
                                                     font="Comic 15 bold").place(x=825, y=205)

                    if event.keysym == "Up":
                        if i < 100:
                            if int(canvas_mapa.coords(personaje)[0]) < 715:
                                canvas_mapa.move(personaje, 0 + vel, 0)
                                canvas_mapa.move(mapa, 0, 0 + vel)
                                vel += 0.1
                            else:
                                img_personaje = PhotoImage(file="caida.png")
                                personaje = canvas_mapa.create_image(715, 510, image=img_personaje)
                                ventana2.update()
                                canvas_mapa.after(100)
                                canvas_mapa.delete(personaje)
                                img_personaje = PhotoImage(file="skate main.png")
                                personaje = canvas_mapa.create_image(475, 510, image=img_personaje)
                                i += 10
                                if i > 100:
                                    i = 100
                                Hambre_valor = Label(ventana2, text=i, borderwidth=0, highlightthickness=0,
                                                     bg="#EFE4B0",
                                                     font="Comic 15 bold").place(x=825, y=205)
                    if event.keysym == "Down":
                        if i < 100:
                            if int(canvas_mapa.coords(personaje)[0]) > 245:
                                vel += 0.2
                                canvas_mapa.move(mapa, 0, vel)
                                canvas_mapa.move(personaje, -vel, 0)
                            else:
                                img_personaje = PhotoImage(file="caida.png")
                                personaje = canvas_mapa.create_image(245, 510, image=img_personaje)
                                ventana2.update()
                                canvas_mapa.after(100)
                                canvas_mapa.delete(personaje)
                                img_personaje = PhotoImage(file="skate main.png")
                                personaje = canvas_mapa.create_image(475, 510, image=img_personaje)
                                i += 10
                                if i > 100:
                                    i = 100
                                Hambre_valor = Label(ventana2, text=i, borderwidth=0, highlightthickness=0,
                                                     bg="#EFE4B0",
                                                     font="Comic 15 bold").place(x=825, y=205)
                    if event.keysym == "Right":
                        if i < 100:
                            if int(canvas_mapa.coords(personaje)[0]) < 715:
                                vel += 0.2
                                canvas_mapa.move(personaje, vel, 0)
                                canvas_mapa.move(mapa, 0, vel)
                            else:
                                img_personaje = PhotoImage(file="caida.png")
                                personaje = canvas_mapa.create_image(715, 510, image=img_personaje)
                                ventana2.update()
                                canvas_mapa.after(500)
                                canvas_mapa.delete(personaje)
                                img_personaje = PhotoImage(file="skate main.png")
                                personaje = canvas_mapa.create_image(470, 510, image=img_personaje)
                                i += 10
                                if i > 100:
                                    i = 100
                                Hambre_valor = Label(ventana2, text=i, borderwidth=0, highlightthickness=0,
                                                     bg="#EFE4B0",
                                                     font="Comic 15 bold").place(x=825, y=205)

                canvas_mapa.bind_all("<Up>", movimiento)
                canvas_mapa.bind_all("<Left>", movimiento)
                canvas_mapa.bind_all("<Right>", movimiento)
                canvas_mapa.bind_all("<Down>", movimiento)

                global rival, rival_img, puntaje, i
                x = random.randint(1, 3)
                y = random.randint(1, 3)
                w = random.randint(1, 2)
                z = random.randint(1, 2)
                objeto = StringVar()
                if z == 1:
                    trap_or_treasure = 345
                else:
                    trap_or_treasure = 617
                tinta_o_pizza = random.randint(1, 10)
                if tinta_o_pizza == 3:
                    obstaculo_img = PhotoImage(file="pizza.png")
                    obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                    objeto = "pizza"
                elif tinta_o_pizza == 8:
                    obstaculo_img = PhotoImage(file="mancha.png")
                    obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                    objeto = "mancha"
                else:
                    obstaculo_img = PhotoImage(file="vacio.png")
                    obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                if w == 1:
                    desp = 0.1
                elif w == 2:
                    desp = -0.1
                if y == 1:
                    pos = 265
                elif y == 2:
                    pos = 470
                elif y == 3:
                    pos = 685
                # Enemigo 1
                if x == 1:
                    rival_img = PhotoImage(file="enemigo1.png")
                    rival = canvas_mapa.create_image(pos, 0, image=rival_img)
                    while canvas_mapa.coords(rival)[1] < 640:
                        canvas_mapa.move(rival, 0, 0.1)
                        canvas_mapa.move(obstaculo, 0, 0.1)
                        if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                            if objeto == "pizza":
                                puntaje += 500
                                Score_valor = Label(ventana2, text=puntaje, borderwidth=0, highlightthickness=0,
                                                    bg="#EFE4B0", font="Comic 15 bold").place(x=815, y=125)
                                i -= 10
                                if i < 0:
                                    i = 0
                                obstaculo_img = PhotoImage(file="vacio.png")
                                obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                                Hambre_valor = Label(ventana2, text=i, borderwidth=0, highlightthickness=0,
                                                     bg="#EFE4B0",
                                                     font="Comic 15 bold").place(x=825, y=205)
                        ventana2.update()
                # Enemigo 2
                elif x == 2:
                    rival_img = PhotoImage(file="enemigo2.png")
                    rival = canvas_mapa.create_image(pos, 0, image=rival_img)
                    pos_y = canvas_mapa.coords(personaje)[1]
                    if pos == 265:
                        while canvas_mapa.coords(rival)[1] < 550:
                            if canvas_mapa.coords(rival)[1] < 240:
                                canvas_mapa.move(rival, 0, 0.2)
                                canvas_mapa.move(obstaculo, 0, 0.2)
                                if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                    if objeto == "pizza":
                                        puntaje += 500
                                        Score_valor = Label(ventana2, text=puntaje, borderwidth=0, highlightthickness=0,
                                                            bg="#EFE4B0", font="Comic 15 bold").place(x=815, y=125)
                                        i -= 10
                                        if i < 0:
                                            i = 0
                                        obstaculo_img = PhotoImage(file="vacio.png")
                                        obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                                        Hambre_valor = Label(ventana2, text=i, borderwidth=0, highlightthickness=0,
                                                             bg="#EFE4B0",
                                                             font="Comic 15 bold").place(x=825, y=205)
                                ventana2.update()
                            elif canvas_mapa.coords(rival)[1] > 240 and canvas_mapa.coords(rival)[1] < 550:
                                canvas_mapa.move(rival, 0.07, 0.2)
                                canvas_mapa.move(obstaculo, 0, 0.2)
                                if canvas_mapa.coords(obstaculo)[1] + 100 > canvas_mapa.coords(personaje)[1]:
                                    if objeto == "pizza":
                                        puntaje += 500
                                        Score_valor = Label(ventana2, text=puntaje, borderwidth=0,
                                                            highlightthickness=0, bg="#EFE4B0",
                                                            font="Comic 15 bold").place(x=815, y=125)
                                        i -= 10
                                        if i < 0:
                                            i = 0
                                        obstaculo_img = PhotoImage(file="vacio.png")
                                        obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                                        Hambre_valor = Label(ventana2, text=i, borderwidth=0, highlightthickness=0,
                                                             bg="#EFE4B0",
                                                             font="Comic 15 bold").place(x=825, y=205)
                                ventana2.update()
                    elif pos == 470:
                        while canvas_mapa.coords(rival)[1] < 550:
                            if canvas_mapa.coords(rival)[1] < 240:
                                canvas_mapa.move(rival, 0, 0.2)
                                canvas_mapa.move(obstaculo, 0, 0.2)
                                if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                    if objeto == "pizza":
                                        puntaje += 500
                                        Score_valor = Label(ventana2, text=puntaje, borderwidth=0,
                                                            highlightthickness=0, bg="#EFE4B0",
                                                            font="Comic 15 bold").place(x=815, y=125)
                                        i -= 10
                                        if i < 0:
                                            i = 0
                                        obstaculo_img = PhotoImage(file="vacio.png")
                                        obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                                        Hambre_valor = Label(ventana2, text=i, borderwidth=0, highlightthickness=0,
                                                             bg="#EFE4B0",
                                                             font="Comic 15 bold").place(x=825, y=205)
                                ventana2.update()
                            elif canvas_mapa.coords(rival)[1] > 240 and canvas_mapa.coords(rival)[1] < 550:
                                canvas_mapa.move(rival, desp, 0.2)
                                canvas_mapa.move(obstaculo, 0, 0.2)
                                if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                    if objeto == "pizza":
                                        puntaje += 500
                                        Score_valor = Label(ventana2, text=puntaje, borderwidth=0,
                                                            highlightthickness=0, bg="#EFE4B0",
                                                            font="Comic 15 bold").place(x=815, y=125)
                                        i -= 10
                                        if i < 0:
                                            i = 0
                                        obstaculo_img = PhotoImage(file="vacio.png")
                                        obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                                        Hambre_valor = Label(ventana2, text=i, borderwidth=0, highlightthickness=0,
                                                             bg="#EFE4B0",
                                                             font="Comic 15 bold").place(x=825, y=205)
                                ventana2.update()
                    else:
                        while canvas_mapa.coords(rival)[1] < 550:
                            if canvas_mapa.coords(rival)[1] < 240:
                                canvas_mapa.move(rival, 0, 0.2)
                                canvas_mapa.move(obstaculo, 0, 0.2)
                                if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                    if objeto == "pizza":
                                        puntaje += 500
                                        Score_valor = Label(ventana2, text=puntaje, borderwidth=0,
                                                            highlightthickness=0, bg="#EFE4B0",
                                                            font="Comic 15 bold").place(x=815, y=125)
                                        i -= 10
                                        if i < 0:
                                            i = 0
                                        obstaculo_img = PhotoImage(file="vacio.png")
                                        obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                                        Hambre_valor = Label(ventana2, text=i, borderwidth=0, highlightthickness=0,
                                                             bg="#EFE4B0",
                                                             font="Comic 15 bold").place(x=825, y=205)
                                ventana2.update()
                            elif canvas_mapa.coords(rival)[1] > 240 and canvas_mapa.coords(rival)[1] < 550:
                                canvas_mapa.move(rival, -0.07, 0.2)
                                canvas_mapa.move(obstaculo, 0, 0.2)
                                if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                    if canvas_mapa.coords(obstaculo)[0] - 5 > canvas_mapa.coords(personaje)[0] and \
                                                            canvas_mapa.coords(obstaculo)[0] + 5 < \
                                                    canvas_mapa.coords(personaje)[0]:
                                        if objeto == "pizza":
                                            puntaje += 500
                                            Score_valor = Label(ventana2, text=puntaje, borderwidth=0,
                                                                highlightthickness=0, bg="#EFE4B0",
                                                                font="Comic 15 bold").place(x=815, y=125)
                                            i -= 10
                                            if i < 0:
                                                i = 0
                                            obstaculo_img = PhotoImage(file="vacio.png")
                                            obstaculo = canvas_mapa.create_image(trap_or_treasure, 0,
                                                                                 image=obstaculo_img)
                                            Hambre_valor = Label(ventana2, text=i, borderwidth=0, highlightthickness=0,
                                                                 bg="#EFE4B0",
                                                                 font="Comic 15 bold").place(x=825, y=205)
                                ventana2.update()
                # Enemigo 3
                elif x == 3:
                    rival_img = PhotoImage(file="enemigo3.png")
                    rival = canvas_mapa.create_image(pos, 0, image=rival_img)
                    if pos == 470:
                        while canvas_mapa.coords(rival)[1] < 550:
                            if canvas_mapa.coords(rival)[1] < 240:
                                canvas_mapa.move(rival, 0, 0.2)
                                canvas_mapa.move(obstaculo, 0, 0.2)
                                if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                    # if canvas_mapa.coords(obstaculo)[0] - 5 > canvas_mapa.coords(personaje)[0] and canvas_mapa.coords(obstaculo)[0] + 5 < canvas_mapa.coords(personaje)[0]:
                                    if objeto.get() == "pizza":
                                        puntaje += 500
                                        Score_valor = Label(ventana2, text=puntaje, borderwidth=0,
                                                            highlightthickness=0, bg="#EFE4B0",
                                                            font="Comic 15 bold").place(x=815, y=125)
                                        i -= 10
                                        if i < 0:
                                            i = 0
                                        obstaculo_img = PhotoImage(file="vacio.png")
                                        obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                                        Hambre_valor = Label(ventana2, text=i, borderwidth=0, highlightthickness=0,
                                                             bg="#EFE4B0",
                                                             font="Comic 15 bold").place(x=825, y=205)
                                ventana2.update()
                            elif canvas_mapa.coords(rival)[1] > 240 and canvas_mapa.coords(rival)[1] < 550:
                                if canvas_mapa.coords(rival)[1] > 240 and canvas_mapa.coords(rival)[1] < 550:
                                    if canvas_mapa.coords(personaje)[0] > 245 and canvas_mapa.coords(personaje)[
                                        0] < 440:
                                        canvas_mapa.move(rival, -0.07, 0.2)
                                        canvas_mapa.move(obstaculo, 0, 0.2)
                                        if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                            if objeto == "pizza":
                                                puntaje += 500
                                                Score_valor = Label(ventana2, text=puntaje, borderwidth=0,
                                                                    highlightthickness=0, bg="#EFE4B0",
                                                                    font="Comic 15 bold").place(x=815, y=125)
                                                i -= 10
                                                if i < 0:
                                                    i = 0
                                                obstaculo_img = PhotoImage(file="vacio.png")
                                                obstaculo = canvas_mapa.create_image(trap_or_treasure, 0,
                                                                                     image=obstaculo_img)
                                                Hambre_valor = Label(ventana2, text=i, borderwidth=0,
                                                                     highlightthickness=0,
                                                                     bg="#EFE4B0",
                                                                     font="Comic 15 bold").place(x=825, y=205)
                                        ventana2.update()
                                    elif canvas_mapa.coords(personaje)[0] >= 440 and canvas_mapa.coords(personaje)[
                                        0] < 480:
                                        canvas_mapa.move(rival, 0, 0.2)
                                        canvas_mapa.move(obstaculo, 0, 0.2)
                                        if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                            if objeto == "pizza":
                                                puntaje += 500
                                                Score_valor = Label(ventana2, text=puntaje, borderwidth=0,
                                                                    highlightthickness=0, bg="#EFE4B0",
                                                                    font="Comic 15 bold").place(x=815, y=125)
                                                i -= 10
                                                if i < 0:
                                                    i = 0
                                                obstaculo_img = PhotoImage(file="vacio.png")
                                                obstaculo = canvas_mapa.create_image(trap_or_treasure, 0,
                                                                                     image=obstaculo_img)
                                                Hambre_valor = Label(ventana2, text=i, borderwidth=0,
                                                                     highlightthickness=0,
                                                                     bg="#EFE4B0",
                                                                     font="Comic 15 bold").place(x=825, y=205)
                                        ventana2.update()
                                    elif canvas_mapa.coords(personaje)[0] >= 480 and canvas_mapa.coords(personaje)[
                                        0] < 715:
                                        canvas_mapa.move(rival, 0.07, 0.2)
                                        canvas_mapa.move(obstaculo, 0, 0.2)
                                        ventana2.update()
                    elif pos == 265:
                        while canvas_mapa.coords(rival)[1] < 550:
                            if canvas_mapa.coords(rival)[1] < 240:
                                canvas_mapa.move(rival, 0, 0.2)
                                canvas_mapa.move(obstaculo, 0, 0.2)
                                if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                    if objeto == "pizza":
                                        puntaje += 500
                                        Score_valor = Label(ventana2, text=puntaje, borderwidth=0,
                                                            highlightthickness=0, bg="#EFE4B0",
                                                            font="Comic 15 bold").place(x=815, y=125)
                                        i -= 10
                                        if i < 0:
                                            i = 0
                                        obstaculo_img = PhotoImage(file="vacio.png")
                                        obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                                        Hambre_valor = Label(ventana2, text=i, borderwidth=0, highlightthickness=0,
                                                             bg="#EFE4B0",
                                                             font="Comic 15 bold").place(x=825, y=205)
                                        ventana2.update()
                            elif canvas_mapa.coords(rival)[1] > 240 and canvas_mapa.coords(rival)[1] < 550:
                                if canvas_mapa.coords(rival)[1] > 240 and canvas_mapa.coords(rival)[1] < 550:
                                    if canvas_mapa.coords(personaje)[0] > 245 and canvas_mapa.coords(personaje)[
                                        0] < 460:
                                        canvas_mapa.move(rival, 0, 0.2)
                                        canvas_mapa.move(obstaculo, 0, 0.2)
                                        if canvas_mapa.coords(obstaculo)[1] + 100 > canvas_mapa.coords(personaje)[1]:
                                            if objeto == "pizza":
                                                puntaje += 500
                                                Score_valor = Label(ventana2, text=puntaje, borderwidth=0,
                                                                    highlightthickness=0, bg="#EFE4B0",
                                                                    font="Comic 15 bold").place(x=815, y=125)
                                                i -= 10
                                                if i < 0:
                                                    i = 0
                                                obstaculo_img = PhotoImage(file="vacio.png")
                                                obstaculo = canvas_mapa.create_image(trap_or_treasure, 0,
                                                                                     image=obstaculo_img)
                                                Hambre_valor = Label(ventana2, text=i, borderwidth=0,
                                                                     highlightthickness=0,
                                                                     bg="#EFE4B0",
                                                                     font="Comic 15 bold").place(x=825, y=205)
                                        ventana2.update()
                                    elif canvas_mapa.coords(personaje)[0] >= 460 and canvas_mapa.coords(personaje)[
                                        0] < 480:
                                        canvas_mapa.move(rival, 0.07, 0.2)
                                        canvas_mapa.move(obstaculo, 0, 0.2)
                                        if canvas_mapa.coords(obstaculo)[1] + 100 > canvas_mapa.coords(personaje)[1]:
                                            if objeto == "pizza":
                                                puntaje += 500
                                                Score_valor = Label(ventana2, text=puntaje, borderwidth=0,
                                                                    highlightthickness=0, bg="#EFE4B0",
                                                                    font="Comic 15 bold").place(x=815, y=125)
                                                i -= 10
                                                if i < 0:
                                                    i = 0
                                                obstaculo_img = PhotoImage(file="vacio.png")
                                                obstaculo = canvas_mapa.create_image(trap_or_treasure, 0,
                                                                                     image=obstaculo_img)
                                                Hambre_valor = Label(ventana2, text=i, borderwidth=0,
                                                                     highlightthickness=0,
                                                                     bg="#EFE4B0",
                                                                     font="Comic 15 bold").place(x=825, y=205)
                                        ventana2.update()
                                    elif canvas_mapa.coords(personaje)[0] >= 480 and canvas_mapa.coords(personaje)[
                                        0] < 715:
                                        canvas_mapa.move(rival, 0.07, 0.2)
                                        canvas_mapa.move(obstaculo, 0, 0.2)
                                        if canvas_mapa.coords(obstaculo)[1] + 100 > canvas_mapa.coords(personaje)[1]:
                                            if objeto == "pizza":
                                                puntaje += 500
                                                Score_valor = Label(ventana2, text=puntaje, borderwidth=0,
                                                                    highlightthickness=0, bg="#EFE4B0",
                                                                    font="Comic 15 bold").place(x=815, y=125)
                                                i -= 10
                                                if i < 0:
                                                    i = 0
                                                obstaculo_img = PhotoImage(file="vacio.png")
                                                obstaculo = canvas_mapa.create_image(trap_or_treasure, 0,
                                                                                     image=obstaculo_img)
                                                Hambre_valor = Label(ventana2, text=i, borderwidth=0,
                                                                     highlightthickness=0,
                                                                     bg="#EFE4B0",
                                                                     font="Comic 15 bold").place(x=825, y=205)
                                        ventana2.update()
                    else:
                        while canvas_mapa.coords(rival)[1] < 550:
                            if canvas_mapa.coords(rival)[1] < 240:
                                canvas_mapa.move(rival, 0, 0.2)
                                canvas_mapa.move(obstaculo, 0, 0.2)
                                if canvas_mapa.coords(obstaculo)[1] + 100 > canvas_mapa.coords(personaje)[1]:
                                    if objeto == "pizza":
                                        puntaje += 500
                                        Score_valor = Label(ventana2, text=puntaje, borderwidth=0,
                                                            highlightthickness=0, bg="#EFE4B0",
                                                            font="Comic 15 bold").place(x=815, y=125)
                                        i -= 10
                                        if i < 0:
                                            i = 0
                                        obstaculo_img = PhotoImage(file="vacio.png")
                                        obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                                        Hambre_valor = Label(ventana2, text=i, borderwidth=0, highlightthickness=0,
                                                             bg="#EFE4B0",
                                                             font="Comic 15 bold").place(x=825, y=205)
                                ventana2.update()
                            elif canvas_mapa.coords(rival)[1] > 240 and canvas_mapa.coords(rival)[1] < 550:
                                if canvas_mapa.coords(rival)[1] > 240 and canvas_mapa.coords(rival)[1] < 550:
                                    if canvas_mapa.coords(personaje)[0] > 245 and canvas_mapa.coords(personaje)[
                                        0] < 460:
                                        canvas_mapa.move(rival, -0.07, 0.2)
                                        canvas_mapa.move(obstaculo, 0, 0.2)
                                        if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                            if objeto == "pizza":
                                                puntaje += 500
                                                Score_valor = Label(ventana2, text=puntaje, borderwidth=0,
                                                                    highlightthickness=0, bg="#EFE4B0",
                                                                    font="Comic 15 bold").place(x=815, y=125)
                                                i -= 10
                                                if i < 0:
                                                    i = 0
                                                obstaculo_img = PhotoImage(file="vacio.png")
                                                obstaculo = canvas_mapa.create_image(trap_or_treasure, 0,
                                                                                     image=obstaculo_img)
                                                Hambre_valor = Label(ventana2, text=i, borderwidth=0,
                                                                     highlightthickness=0,
                                                                     bg="#EFE4B0",
                                                                     font="Comic 15 bold").place(x=825, y=205)
                                        ventana2.update()
                                    elif canvas_mapa.coords(personaje)[0] >= 460 and canvas_mapa.coords(personaje)[
                                        0] < 480:
                                        canvas_mapa.move(rival, -0.07, 0.2)
                                        canvas_mapa.move(obstaculo, 0, 0.2)
                                        if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                            if objeto == "pizza":
                                                puntaje += 500
                                                Score_valor = Label(ventana2, text=puntaje, borderwidth=0,
                                                                    highlightthickness=0, bg="#EFE4B0",
                                                                    font="Comic 15 bold").place(x=815, y=125)
                                                i -= 10
                                                if i < 0:
                                                    i = 0
                                                obstaculo_img = PhotoImage(file="vacio.png")
                                                obstaculo = canvas_mapa.create_image(trap_or_treasure, 0,
                                                                                     image=obstaculo_img)
                                                Hambre_valor = Label(ventana2, text=i, borderwidth=0,
                                                                     highlightthickness=0,
                                                                     bg="#EFE4B0",
                                                                     font="Comic 15 bold").place(x=825, y=205)
                                        ventana2.update()
                                    elif canvas_mapa.coords(personaje)[0] >= 480 and canvas_mapa.coords(personaje)[
                                        0] < 715:
                                        canvas_mapa.move(rival, 0, 0.2)
                                        canvas_mapa.move(obstaculo, 0, 0.2)
                                        if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                            if objeto == "pizza":
                                                puntaje += 500
                                                Score_valor = Label(ventana2, text=puntaje, borderwidth=0,
                                                                    highlightthickness=0, bg="#EFE4B0",
                                                                    font="Comic 15 bold").place(x=815, y=125)
                                                i -= 10
                                                if i < 0:
                                                    i = 0
                                                obstaculo_img = PhotoImage(file="vacio.png")
                                                obstaculo = canvas_mapa.create_image(trap_or_treasure, 0,
                                                                                     image=obstaculo_img)
                                                Hambre_valor = Label(ventana2, text=i, borderwidth=0,
                                                                     highlightthickness=0,
                                                                     bg="#EFE4B0",
                                                                     font="Comic 15 bold").place(x=825, y=205)
                                        ventana2.update()

            enemigos()

        ventana2.mainloop()
    # Tercer mapa
    elif variable_mapa == 3:
        global rival, rival_img
        ventana_principal.destroy()
        ventana3 = Tk()
        ventana3.title("Road Figther Plus")
        ventana3.geometry("950x600")
        # Mapa e interfaz del jugador
        canvas_mapa = Canvas(ventana3, width=950, height=600, borderwidth=0, highlightthickness=0)
        img_mapa = PhotoImage(file="mapa3.png")
        mapa = canvas_mapa.create_image(473, -2400, image=img_mapa)
        img_personaje = PhotoImage(file="skate main.png")
        personaje = canvas_mapa.create_image(475, 510, image=img_personaje)
        img_caidap = PhotoImage(file="caida.png")
        canvas_mapa.pack()
        # barras laterales
        i = 0
        vel = 0
        texto_nombre = entrada.get()
        nombre_valor = Label(ventana3, text=texto_nombre, borderwidth=0, highlightthickness=0, bg="#EFE4B0",
                             font="Comic 15 bold").place(x=805, y=45)
        Score = Label(ventana3, text="Score", borderwidth=0, highlightthickness=0, bg="#EFE4B0",
                      font="Comic 15 bold").place(x=805, y=100)
        Score_valor = Label(ventana3, text=puntaje, borderwidth=0, highlightthickness=0, bg="#EFE4B0",
                            font="Comic 15 bold").place(x=815, y=125)
        Hambre = Label(ventana3, text="Hunger", borderwidth=0, highlightthickness=0, bg="#EFE4B0",
                       font="Comic 15 bold").place(x=800, y=180)
        Hambre_valor = Label(ventana3, text=i, borderwidth=0, highlightthickness=0, bg="#EFE4B0",
                             font="Comic 15 bold").place(x=825, y=205)

        # Funciones

        while i <= 98:
            lista = list(time.localtime())
            if lista[5] != 0:
                if lista[5] % 1 == 0:
                    i += 2
            Hambre_valor = Label(ventana3, text=i, borderwidth=0, highlightthickness=0, bg="#EFE4B0",
                                 font="Comic 15 bold").place(x=825, y=205)

            canvas_mapa.after(1)

            def enemigos():
                def movimiento(event):
                    global caidap, personaje, img_personaje, vel, i
                    if event.keysym == "Left":
                        if i < 100:
                            if int(canvas_mapa.coords(personaje)[0]) > 247:
                                canvas_mapa.move(personaje, 0 - vel, 0)
                                canvas_mapa.move(mapa, 0, 0 + vel)
                                vel += 0.1
                            else:
                                img_personaje = PhotoImage(file="caida.png")
                                personaje = canvas_mapa.create_image(245, 510, image=img_personaje)
                                ventana3.update()
                                canvas_mapa.after(100)
                                canvas_mapa.delete(personaje)
                                img_personaje = PhotoImage(file="skate main.png")
                                personaje = canvas_mapa.create_image(475, 510, image=img_personaje)
                                i += 10
                                if i > 100:
                                    i = 100
                                Hambre_valor = Label(ventana3, text=i, borderwidth=0, highlightthickness=0,
                                                     bg="#EFE4B0",
                                                     font="Comic 15 bold").place(x=825, y=205)

                    if event.keysym == "Up":
                        if i < 100:
                            if int(canvas_mapa.coords(personaje)[0]) < 715:
                                canvas_mapa.move(personaje, 0 + vel, 0)
                                canvas_mapa.move(mapa, 0, 0 + vel)
                                vel += 0.1
                            else:
                                img_personaje = PhotoImage(file="caida.png")
                                personaje = canvas_mapa.create_image(715, 510, image=img_personaje)
                                ventana3.update()
                                canvas_mapa.after(100)
                                canvas_mapa.delete(personaje)
                                img_personaje = PhotoImage(file="skate main.png")
                                personaje = canvas_mapa.create_image(475, 510, image=img_personaje)
                                i += 10
                                if i > 100:
                                    i = 100
                                Hambre_valor = Label(ventana3, text=i, borderwidth=0, highlightthickness=0,
                                                     bg="#EFE4B0",
                                                     font="Comic 15 bold").place(x=825, y=205)
                    if event.keysym == "Down":
                        if i < 100:
                            if int(canvas_mapa.coords(personaje)[0]) > 245:
                                vel += 0.1
                                canvas_mapa.move(mapa, 0, vel)
                                canvas_mapa.move(personaje, -vel, 0)
                            else:
                                img_personaje = PhotoImage(file="caida.png")
                                personaje = canvas_mapa.create_image(245, 510, image=img_personaje)
                                ventana3.update()
                                canvas_mapa.after(100)
                                canvas_mapa.delete(personaje)
                                img_personaje = PhotoImage(file="skate main.png")
                                personaje = canvas_mapa.create_image(475, 510, image=img_personaje)
                                i += 10
                                if i > 100:
                                    i = 100
                                Hambre_valor = Label(ventana3, text=i, borderwidth=0, highlightthickness=0,
                                                     bg="#EFE4B0",
                                                     font="Comic 15 bold").place(x=825, y=205)
                    if event.keysym == "Right":
                        if i < 100:
                            if int(canvas_mapa.coords(personaje)[0]) < 715:
                                vel += 0.1
                                canvas_mapa.move(personaje, vel, 0)
                                canvas_mapa.move(mapa, 0, vel)
                            else:
                                img_personaje = PhotoImage(file="caida.png")
                                personaje = canvas_mapa.create_image(715, 510, image=img_personaje)
                                ventana3.update()
                                canvas_mapa.after(500)
                                canvas_mapa.delete(personaje)
                                img_personaje = PhotoImage(file="skate main.png")
                                personaje = canvas_mapa.create_image(470, 510, image=img_personaje)
                                i += 10
                                if i > 100:
                                    i = 100
                                Hambre_valor = Label(ventana3, text=i, borderwidth=0, highlightthickness=0,
                                                     bg="#EFE4B0",
                                                     font="Comic 15 bold").place(x=825, y=205)

                canvas_mapa.bind_all("<Up>", movimiento)
                canvas_mapa.bind_all("<Left>", movimiento)
                canvas_mapa.bind_all("<Right>", movimiento)
                canvas_mapa.bind_all("<Down>", movimiento)

                global rival, rival_img, puntaje, i
                x = random.randint(1, 3)
                y = random.randint(1, 3)
                w = random.randint(1, 2)
                z = random.randint(1, 2)
                objeto = StringVar()
                if z == 1:
                    trap_or_treasure = 345
                else:
                    trap_or_treasure = 617
                tinta_o_pizza = random.randint(1, 10)
                if tinta_o_pizza == 3:
                    obstaculo_img = PhotoImage(file="pizza.png")
                    obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                    objeto = "pizza"
                elif tinta_o_pizza == 8 or tinta_o_pizza == 1 or tinta_o_pizza == 9:
                    obstaculo_img = PhotoImage(file="mancha.png")
                    obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                    objeto = "mancha"
                else:
                    obstaculo_img = PhotoImage(file="vacio.png")
                    obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                if w == 1:
                    desp = 0.1
                elif w == 2:
                    desp = -0.1
                if y == 1:
                    pos = 265
                elif y == 2:
                    pos = 470
                elif y == 3:
                    pos = 685
                # Enemigo 1
                if x == 1:
                    rival_img = PhotoImage(file="enemigo1.png")
                    rival = canvas_mapa.create_image(pos, 0, image=rival_img)
                    while canvas_mapa.coords(rival)[1] < 640:
                        canvas_mapa.move(rival, 0, 0.3)
                        canvas_mapa.move(obstaculo, 0, 0.3)
                        if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                            if objeto == "pizza":
                                puntaje += 500
                                Score_valor = Label(ventana3, text=puntaje, borderwidth=0, highlightthickness=0,
                                                    bg="#EFE4B0", font="Comic 15 bold").place(x=815, y=125)
                                i -= 10
                                if i < 0:
                                    i = 0
                                obstaculo_img = PhotoImage(file="vacio.png")
                                obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                                Hambre_valor = Label(ventana3, text=i, borderwidth=0, highlightthickness=0,
                                                     bg="#EFE4B0",
                                                     font="Comic 15 bold").place(x=825, y=205)
                        ventana3.update()
                # Enemigo 2
                elif x == 2:
                    rival_img = PhotoImage(file="enemigo2.png")
                    rival = canvas_mapa.create_image(pos, 0, image=rival_img)
                    pos_y = canvas_mapa.coords(personaje)[1]
                    if pos == 265:
                        while canvas_mapa.coords(rival)[1] < 550:
                            if canvas_mapa.coords(rival)[1] < 240:
                                canvas_mapa.move(rival, 0, 0.3)
                                canvas_mapa.move(obstaculo, 0, 0.3)
                                if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                    if objeto == "pizza":
                                        puntaje += 500
                                        Score_valor = Label(ventana3, text=puntaje, borderwidth=0, highlightthickness=0,
                                                            bg="#EFE4B0", font="Comic 15 bold").place(x=815, y=125)
                                        i -= 10
                                        if i < 0:
                                            i = 0
                                        obstaculo_img = PhotoImage(file="vacio.png")
                                        obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                                        Hambre_valor = Label(ventana3, text=i, borderwidth=0, highlightthickness=0,
                                                             bg="#EFE4B0",
                                                             font="Comic 15 bold").place(x=825, y=205)
                                ventana3.update()
                            elif canvas_mapa.coords(rival)[1] > 240 and canvas_mapa.coords(rival)[1] < 550:
                                canvas_mapa.move(rival, 0.07, 0.3)
                                canvas_mapa.move(obstaculo, 0, 0.3)
                                if canvas_mapa.coords(obstaculo)[1] + 100 > canvas_mapa.coords(personaje)[1]:
                                    if objeto == "pizza":
                                        puntaje += 500
                                        Score_valor = Label(ventana3, text=puntaje, borderwidth=0,
                                                            highlightthickness=0, bg="#EFE4B0",
                                                            font="Comic 15 bold").place(x=815, y=125)
                                        i -= 10
                                        if i < 0:
                                            i = 0
                                        obstaculo_img = PhotoImage(file="vacio.png")
                                        obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                                        Hambre_valor = Label(ventana3, text=i, borderwidth=0, highlightthickness=0,
                                                             bg="#EFE4B0",
                                                             font="Comic 15 bold").place(x=825, y=205)
                                ventana3.update()
                    elif pos == 470:
                        while canvas_mapa.coords(rival)[1] < 550:
                            if canvas_mapa.coords(rival)[1] < 240:
                                canvas_mapa.move(rival, 0, 0.3)
                                canvas_mapa.move(obstaculo, 0, 0.3)
                                if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                    if objeto == "pizza":
                                        puntaje += 500
                                        Score_valor = Label(ventana3, text=puntaje, borderwidth=0,
                                                            highlightthickness=0, bg="#EFE4B0",
                                                            font="Comic 15 bold").place(x=815, y=125)
                                        i -= 10
                                        if i < 0:
                                            i = 0
                                        obstaculo_img = PhotoImage(file="vacio.png")
                                        obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                                        Hambre_valor = Label(ventana3, text=i, borderwidth=0, highlightthickness=0,
                                                             bg="#EFE4B0",
                                                             font="Comic 15 bold").place(x=825, y=205)
                                ventana3.update()
                            elif canvas_mapa.coords(rival)[1] > 240 and canvas_mapa.coords(rival)[1] < 550:
                                canvas_mapa.move(rival, desp, 0.3)
                                canvas_mapa.move(obstaculo, 0, 0.3)
                                if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                    if objeto == "pizza":
                                        puntaje += 500
                                        Score_valor = Label(ventana3, text=puntaje, borderwidth=0,
                                                            highlightthickness=0, bg="#EFE4B0",
                                                            font="Comic 15 bold").place(x=815, y=125)
                                        i -= 10
                                        if i < 0:
                                            i = 0
                                        obstaculo_img = PhotoImage(file="vacio.png")
                                        obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                                        Hambre_valor = Label(ventana3, text=i, borderwidth=0, highlightthickness=0,
                                                             bg="#EFE4B0",
                                                             font="Comic 15 bold").place(x=825, y=205)
                                ventana3.update()
                    else:
                        while canvas_mapa.coords(rival)[1] < 550:
                            if canvas_mapa.coords(rival)[1] < 240:
                                canvas_mapa.move(rival, 0, 0.3)
                                canvas_mapa.move(obstaculo, 0, 0.3)
                                if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                    if objeto == "pizza":
                                        puntaje += 500
                                        Score_valor = Label(ventana3, text=puntaje, borderwidth=0,
                                                            highlightthickness=0, bg="#EFE4B0",
                                                            font="Comic 15 bold").place(x=815, y=125)
                                        i -= 10
                                        if i < 0:
                                            i = 0
                                        obstaculo_img = PhotoImage(file="vacio.png")
                                        obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                                        Hambre_valor = Label(ventana3, text=i, borderwidth=0, highlightthickness=0,
                                                             bg="#EFE4B0",
                                                             font="Comic 15 bold").place(x=825, y=205)
                                ventana3.update()
                            elif canvas_mapa.coords(rival)[1] > 240 and canvas_mapa.coords(rival)[1] < 550:
                                canvas_mapa.move(rival, -0.07, 0.3)
                                canvas_mapa.move(obstaculo, 0, 0.3)
                                if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                    if canvas_mapa.coords(obstaculo)[0] - 5 > canvas_mapa.coords(personaje)[0] and \
                                                            canvas_mapa.coords(obstaculo)[0] + 5 < \
                                                    canvas_mapa.coords(personaje)[0]:
                                        if objeto == "pizza":
                                            puntaje += 500
                                            Score_valor = Label(ventana3, text=puntaje, borderwidth=0,
                                                                highlightthickness=0, bg="#EFE4B0",
                                                                font="Comic 15 bold").place(x=815, y=125)
                                            i -= 10
                                            if i < 0:
                                                i = 0
                                            obstaculo_img = PhotoImage(file="vacio.png")
                                            obstaculo = canvas_mapa.create_image(trap_or_treasure, 0,
                                                                                 image=obstaculo_img)
                                            Hambre_valor = Label(ventana3, text=i, borderwidth=0, highlightthickness=0,
                                                                 bg="#EFE4B0",
                                                                 font="Comic 15 bold").place(x=825, y=205)
                                ventana3.update()
                # Enemigo 3
                elif x == 3:
                    rival_img = PhotoImage(file="enemigo3.png")
                    rival = canvas_mapa.create_image(pos, 0, image=rival_img)
                    if pos == 470:
                        while canvas_mapa.coords(rival)[1] < 550:
                            if canvas_mapa.coords(rival)[1] < 240:
                                canvas_mapa.move(rival, 0, 0.3)
                                canvas_mapa.move(obstaculo, 0, 0.3)
                                if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                    # if canvas_mapa.coords(obstaculo)[0] - 5 > canvas_mapa.coords(personaje)[0] and canvas_mapa.coords(obstaculo)[0] + 5 < canvas_mapa.coords(personaje)[0]:
                                    if objeto.get() == "pizza":
                                        puntaje += 500
                                        Score_valor = Label(ventana3, text=puntaje, borderwidth=0,
                                                            highlightthickness=0, bg="#EFE4B0",
                                                            font="Comic 15 bold").place(x=815, y=125)
                                        i -= 10
                                        if i < 0:
                                            i = 0
                                        obstaculo_img = PhotoImage(file="vacio.png")
                                        obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                                        Hambre_valor = Label(ventana3, text=i, borderwidth=0, highlightthickness=0,
                                                             bg="#EFE4B0",
                                                             font="Comic 15 bold").place(x=825, y=205)
                                ventana3.update()
                            elif canvas_mapa.coords(rival)[1] > 240 and canvas_mapa.coords(rival)[1] < 550:
                                if canvas_mapa.coords(rival)[1] > 240 and canvas_mapa.coords(rival)[1] < 550:
                                    if canvas_mapa.coords(personaje)[0] > 245 and canvas_mapa.coords(personaje)[
                                        0] < 440:
                                        canvas_mapa.move(rival, -0.07, 0.3)
                                        canvas_mapa.move(obstaculo, 0, 0.3)
                                        if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                            if objeto == "pizza":
                                                puntaje += 500
                                                Score_valor = Label(ventana3, text=puntaje, borderwidth=0,
                                                                    highlightthickness=0, bg="#EFE4B0",
                                                                    font="Comic 15 bold").place(x=815, y=125)
                                                i -= 10
                                                if i < 0:
                                                    i = 0
                                                obstaculo_img = PhotoImage(file="vacio.png")
                                                obstaculo = canvas_mapa.create_image(trap_or_treasure, 0,
                                                                                     image=obstaculo_img)
                                                Hambre_valor = Label(ventana3, text=i, borderwidth=0,
                                                                     highlightthickness=0,
                                                                     bg="#EFE4B0",
                                                                     font="Comic 15 bold").place(x=825, y=205)
                                        ventana3.update()
                                    elif canvas_mapa.coords(personaje)[0] >= 440 and canvas_mapa.coords(personaje)[
                                        0] < 480:
                                        canvas_mapa.move(rival, 0, 0.3)
                                        canvas_mapa.move(obstaculo, 0, 0.3)
                                        if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                            if objeto == "pizza":
                                                puntaje += 500
                                                Score_valor = Label(ventana3, text=puntaje, borderwidth=0,
                                                                    highlightthickness=0, bg="#EFE4B0",
                                                                    font="Comic 15 bold").place(x=815, y=125)
                                                i -= 10
                                                if i < 0:
                                                    i = 0
                                                obstaculo_img = PhotoImage(file="vacio.png")
                                                obstaculo = canvas_mapa.create_image(trap_or_treasure, 0,
                                                                                     image=obstaculo_img)
                                                Hambre_valor = Label(ventana3, text=i, borderwidth=0,
                                                                     highlightthickness=0,
                                                                     bg="#EFE4B0",
                                                                     font="Comic 15 bold").place(x=825, y=205)
                                        ventana3.update()
                                    elif canvas_mapa.coords(personaje)[0] >= 480 and canvas_mapa.coords(personaje)[
                                        0] < 715:
                                        canvas_mapa.move(rival, 0.07, 0.3)
                                        canvas_mapa.move(obstaculo, 0, 0.3)
                                        ventana3.update()
                    elif pos == 265:
                        while canvas_mapa.coords(rival)[1] < 550:
                            if canvas_mapa.coords(rival)[1] < 240:
                                canvas_mapa.move(rival, 0, 0.3)
                                canvas_mapa.move(obstaculo, 0, 0.3)
                                if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                    if objeto == "pizza":
                                        puntaje += 500
                                        Score_valor = Label(ventana3, text=puntaje, borderwidth=0,
                                                            highlightthickness=0, bg="#EFE4B0",
                                                            font="Comic 15 bold").place(x=815, y=125)
                                        i -= 10
                                        if i < 0:
                                            i = 0
                                        obstaculo_img = PhotoImage(file="vacio.png")
                                        obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                                        Hambre_valor = Label(ventana3, text=i, borderwidth=0, highlightthickness=0,
                                                             bg="#EFE4B0",
                                                             font="Comic 15 bold").place(x=825, y=205)
                                        ventana3.update()
                            elif canvas_mapa.coords(rival)[1] > 240 and canvas_mapa.coords(rival)[1] < 550:
                                if canvas_mapa.coords(rival)[1] > 240 and canvas_mapa.coords(rival)[1] < 550:
                                    if canvas_mapa.coords(personaje)[0] > 245 and canvas_mapa.coords(personaje)[
                                        0] < 460:
                                        canvas_mapa.move(rival, 0, 0.3)
                                        canvas_mapa.move(obstaculo, 0, 0.3)
                                        if canvas_mapa.coords(obstaculo)[1] + 100 > canvas_mapa.coords(personaje)[1]:
                                            if objeto == "pizza":
                                                puntaje += 500
                                                Score_valor = Label(ventana3, text=puntaje, borderwidth=0,
                                                                    highlightthickness=0, bg="#EFE4B0",
                                                                    font="Comic 15 bold").place(x=815, y=125)
                                                i -= 10
                                                if i < 0:
                                                    i = 0
                                                obstaculo_img = PhotoImage(file="vacio.png")
                                                obstaculo = canvas_mapa.create_image(trap_or_treasure, 0,
                                                                                     image=obstaculo_img)
                                                Hambre_valor = Label(ventana3, text=i, borderwidth=0,
                                                                     highlightthickness=0,
                                                                     bg="#EFE4B0",
                                                                     font="Comic 15 bold").place(x=825, y=205)
                                        ventana3.update()
                                    elif canvas_mapa.coords(personaje)[0] >= 460 and canvas_mapa.coords(personaje)[
                                        0] < 480:
                                        canvas_mapa.move(rival, 0.07, 0.3)
                                        canvas_mapa.move(obstaculo, 0, 0.3)
                                        if canvas_mapa.coords(obstaculo)[1] + 100 > canvas_mapa.coords(personaje)[1]:
                                            if objeto == "pizza":
                                                puntaje += 500
                                                Score_valor = Label(ventana3, text=puntaje, borderwidth=0,
                                                                    highlightthickness=0, bg="#EFE4B0",
                                                                    font="Comic 15 bold").place(x=815, y=125)
                                                i -= 10
                                                if i < 0:
                                                    i = 0
                                                obstaculo_img = PhotoImage(file="vacio.png")
                                                obstaculo = canvas_mapa.create_image(trap_or_treasure, 0,
                                                                                     image=obstaculo_img)
                                                Hambre_valor = Label(ventana3, text=i, borderwidth=0,
                                                                     highlightthickness=0,
                                                                     bg="#EFE4B0",
                                                                     font="Comic 15 bold").place(x=825, y=205)
                                        ventana3.update()
                                    elif canvas_mapa.coords(personaje)[0] >= 480 and canvas_mapa.coords(personaje)[
                                        0] < 715:
                                        canvas_mapa.move(rival, 0.07, 0.3)
                                        canvas_mapa.move(obstaculo, 0, 0.3)
                                        if canvas_mapa.coords(obstaculo)[1] + 100 > canvas_mapa.coords(personaje)[1]:
                                            if objeto == "pizza":
                                                puntaje += 500
                                                Score_valor = Label(ventana3, text=puntaje, borderwidth=0,
                                                                    highlightthickness=0, bg="#EFE4B0",
                                                                    font="Comic 15 bold").place(x=815, y=125)
                                                i -= 10
                                                if i < 0:
                                                    i = 0
                                                obstaculo_img = PhotoImage(file="vacio.png")
                                                obstaculo = canvas_mapa.create_image(trap_or_treasure, 0,
                                                                                     image=obstaculo_img)
                                                Hambre_valor = Label(ventana3, text=i, borderwidth=0,
                                                                     highlightthickness=0,
                                                                     bg="#EFE4B0",
                                                                     font="Comic 15 bold").place(x=825, y=205)
                                        ventana3.update()
                    else:
                        while canvas_mapa.coords(rival)[1] < 550:
                            if canvas_mapa.coords(rival)[1] < 240:
                                canvas_mapa.move(rival, 0, 0.3)
                                canvas_mapa.move(obstaculo, 0, 0.3)
                                if canvas_mapa.coords(obstaculo)[1] + 100 > canvas_mapa.coords(personaje)[1]:
                                    if objeto == "pizza":
                                        puntaje += 500
                                        Score_valor = Label(ventana3, text=puntaje, borderwidth=0,
                                                            highlightthickness=0, bg="#EFE4B0",
                                                            font="Comic 15 bold").place(x=815, y=125)
                                        i -= 10
                                        if i < 0:
                                            i = 0
                                        obstaculo_img = PhotoImage(file="vacio.png")
                                        obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                                        Hambre_valor = Label(ventana3, text=i, borderwidth=0, highlightthickness=0,
                                                             bg="#EFE4B0",
                                                             font="Comic 15 bold").place(x=825, y=205)
                                ventana3.update()
                            elif canvas_mapa.coords(rival)[1] > 240 and canvas_mapa.coords(rival)[1] < 550:
                                if canvas_mapa.coords(rival)[1] > 240 and canvas_mapa.coords(rival)[1] < 550:
                                    if canvas_mapa.coords(personaje)[0] > 245 and canvas_mapa.coords(personaje)[
                                        0] < 460:
                                        canvas_mapa.move(rival, -0.07, 0.3)
                                        canvas_mapa.move(obstaculo, 0, 0.3)
                                        if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                            if objeto == "pizza":
                                                puntaje += 500
                                                Score_valor = Label(ventana3, text=puntaje, borderwidth=0,
                                                                    highlightthickness=0, bg="#EFE4B0",
                                                                    font="Comic 15 bold").place(x=815, y=125)
                                                i -= 10
                                                if i < 0:
                                                    i = 0
                                                obstaculo_img = PhotoImage(file="vacio.png")
                                                obstaculo = canvas_mapa.create_image(trap_or_treasure, 0,
                                                                                     image=obstaculo_img)
                                                Hambre_valor = Label(ventana3, text=i, borderwidth=0,
                                                                     highlightthickness=0,
                                                                     bg="#EFE4B0",
                                                                     font="Comic 15 bold").place(x=825, y=205)
                                        ventana3.update()
                                    elif canvas_mapa.coords(personaje)[0] >= 460 and canvas_mapa.coords(personaje)[
                                        0] < 480:
                                        canvas_mapa.move(rival, -0.07, 0.3)
                                        canvas_mapa.move(obstaculo, 0, 0.3)
                                        if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                            if objeto == "pizza":
                                                puntaje += 500
                                                Score_valor = Label(ventana3, text=puntaje, borderwidth=0,
                                                                    highlightthickness=0, bg="#EFE4B0",
                                                                    font="Comic 15 bold").place(x=815, y=125)
                                                i -= 10
                                                if i < 0:
                                                    i = 0
                                                obstaculo_img = PhotoImage(file="vacio.png")
                                                obstaculo = canvas_mapa.create_image(trap_or_treasure, 0,
                                                                                     image=obstaculo_img)
                                                Hambre_valor = Label(ventana3, text=i, borderwidth=0,
                                                                     highlightthickness=0,
                                                                     bg="#EFE4B0",
                                                                     font="Comic 15 bold").place(x=825, y=205)
                                        ventana3.update()
                                    elif canvas_mapa.coords(personaje)[0] >= 480 and canvas_mapa.coords(personaje)[
                                        0] < 715:
                                        canvas_mapa.move(rival, 0, 0.3)
                                        canvas_mapa.move(obstaculo, 0, 0.3)
                                        if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                            if objeto == "pizza":
                                                puntaje += 500
                                                Score_valor = Label(ventana3, text=puntaje, borderwidth=0,
                                                                    highlightthickness=0, bg="#EFE4B0",
                                                                    font="Comic 15 bold").place(x=815, y=125)
                                                i -= 10
                                                if i < 0:
                                                    i = 0
                                                obstaculo_img = PhotoImage(file="vacio.png")
                                                obstaculo = canvas_mapa.create_image(trap_or_treasure, 0,
                                                                                     image=obstaculo_img)
                                                Hambre_valor = Label(ventana3, text=i, borderwidth=0,
                                                                     highlightthickness=0,
                                                                     bg="#EFE4B0",
                                                                     font="Comic 15 bold").place(x=825, y=205)
                                        ventana3.update()

            enemigos()

        ventana3.mainloop()
    # Cuarto mapa
    elif variable_mapa == 4:
        global rival, rival_img
        ventana_principal.destroy()
        ventana4 = Tk()
        ventana4.title("Road Figther Plus")
        ventana4.geometry("950x600")
        # Mapa e interfaz del jugador
        canvas_mapa = Canvas(ventana4, width=950, height=600, borderwidth=0, highlightthickness=0)
        img_mapa = PhotoImage(file="mapa3.png")
        mapa = canvas_mapa.create_image(473, -2400, image=img_mapa)
        img_personaje = PhotoImage(file="skate main.png")
        personaje = canvas_mapa.create_image(475, 510, image=img_personaje)
        img_caidap = PhotoImage(file="caida.png")
        canvas_mapa.pack()
        # barras laterales
        i = 0
        texto_nombre = entrada.get()
        nombre_valor = Label(ventana4, text=texto_nombre, borderwidth=0, highlightthickness=0, bg="#EFE4B0",
                             font="Comic 15 bold").place(x=805, y=45)
        Score = Label(ventana4, text="Score", borderwidth=0, highlightthickness=0, bg="#EFE4B0",
                      font="Comic 15 bold").place(x=805, y=100)
        Score_valor = Label(ventana4, text=puntaje, borderwidth=0, highlightthickness=0, bg="#EFE4B0",
                            font="Comic 15 bold").place(x=815, y=125)
        Hambre = Label(ventana4, text="Hunger", borderwidth=0, highlightthickness=0, bg="#EFE4B0",
                       font="Comic 15 bold").place(x=800, y=180)
        Hambre_valor = Label(ventana4, text=i, borderwidth=0, highlightthickness=0, bg="#EFE4B0",
                             font="Comic 15 bold").place(x=825, y=205)

        # Funciones

        while i <= 98:
            lista = list(time.localtime())
            if lista[5] != 0:
                if lista[5] % 1 == 0:
                    i += 2
            Hambre_valor = Label(ventana4, text=i, borderwidth=0, highlightthickness=0, bg="#EFE4B0",
                                 font="Comic 15 bold").place(x=825, y=205)

            vel = 0
            canvas_mapa.after(1)

            def enemigos():
                def movimiento(event):
                    global caidap, personaje, img_personaje, vel, i
                    if event.keysym == "Left":
                        if i < 100:
                            if int(canvas_mapa.coords(personaje)[0]) > 247:
                                canvas_mapa.move(personaje, 0 - vel, 0)
                                canvas_mapa.move(mapa, 0, 0 + vel)
                                vel += 0.1
                            else:
                                img_personaje = PhotoImage(file="caida.png")
                                personaje = canvas_mapa.create_image(245, 510, image=img_personaje)
                                ventana4.update()
                                canvas_mapa.after(100)
                                canvas_mapa.delete(personaje)
                                img_personaje = PhotoImage(file="skate main.png")
                                personaje = canvas_mapa.create_image(475, 510, image=img_personaje)
                                i += 10
                                if i > 100:
                                    i = 100
                                Hambre_valor = Label(ventana4, text=i, borderwidth=0, highlightthickness=0,
                                                     bg="#EFE4B0",
                                                     font="Comic 15 bold").place(x=825, y=205)

                    if event.keysym == "Up":
                        if i < 100:
                            if int(canvas_mapa.coords(personaje)[0]) < 715:
                                canvas_mapa.move(personaje, 0 + vel, 0)
                                canvas_mapa.move(mapa, 0, 0 + vel)
                                vel += 0.1
                            else:
                                img_personaje = PhotoImage(file="caida.png")
                                personaje = canvas_mapa.create_image(715, 510, image=img_personaje)
                                ventana4.update()
                                canvas_mapa.after(100)
                                canvas_mapa.delete(personaje)
                                img_personaje = PhotoImage(file="skate main.png")
                                personaje = canvas_mapa.create_image(475, 510, image=img_personaje)
                                i += 10
                                if i > 100:
                                    i = 100
                                Hambre_valor = Label(ventana4, text=i, borderwidth=0, highlightthickness=0,
                                                     bg="#EFE4B0",
                                                     font="Comic 15 bold").place(x=825, y=205)
                    if event.keysym == "Down":
                        if i < 100:
                            if int(canvas_mapa.coords(personaje)[0]) > 245:
                                vel += 0.1
                                canvas_mapa.move(mapa, 0, vel)
                                canvas_mapa.move(personaje, -vel, 0)
                            else:
                                img_personaje = PhotoImage(file="caida.png")
                                personaje = canvas_mapa.create_image(245, 510, image=img_personaje)
                                ventana4.update()
                                canvas_mapa.after(100)
                                canvas_mapa.delete(personaje)
                                img_personaje = PhotoImage(file="skate main.png")
                                personaje = canvas_mapa.create_image(475, 510, image=img_personaje)
                                i += 10
                                if i > 100:
                                    i = 100
                                Hambre_valor = Label(ventana4, text=i, borderwidth=0, highlightthickness=0,
                                                     bg="#EFE4B0",
                                                     font="Comic 15 bold").place(x=825, y=205)
                    if event.keysym == "Right":
                        if i < 100:
                            if int(canvas_mapa.coords(personaje)[0]) < 715:
                                vel += 0.1
                                canvas_mapa.move(personaje, vel, 0)
                                canvas_mapa.move(mapa, 0, vel)
                            else:
                                img_personaje = PhotoImage(file="caida.png")
                                personaje = canvas_mapa.create_image(715, 510, image=img_personaje)
                                ventana4.update()
                                canvas_mapa.after(500)
                                canvas_mapa.delete(personaje)
                                img_personaje = PhotoImage(file="skate main.png")
                                personaje = canvas_mapa.create_image(470, 510, image=img_personaje)
                                i += 10
                                if i > 100:
                                    i = 100
                                Hambre_valor = Label(ventana4, text=i, borderwidth=0, highlightthickness=0,
                                                     bg="#EFE4B0",
                                                     font="Comic 15 bold").place(x=825, y=205)

                canvas_mapa.bind_all("<Up>", movimiento)
                canvas_mapa.bind_all("<Left>", movimiento)
                canvas_mapa.bind_all("<Right>", movimiento)
                canvas_mapa.bind_all("<Down>", movimiento)

                global rival, rival_img, puntaje, i
                x = random.randint(1, 3)
                y = random.randint(1, 3)
                w = random.randint(1, 2)
                z = random.randint(1, 2)
                objeto = StringVar()
                if z == 1:
                    trap_or_treasure = 345
                else:
                    trap_or_treasure = 617
                tinta_o_pizza = random.randint(1, 10)
                if tinta_o_pizza == 3:
                    obstaculo_img = PhotoImage(file="pizza.png")
                    obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                    objeto = "pizza"
                elif tinta_o_pizza == 8:
                    obstaculo_img = PhotoImage(file="mancha.png")
                    obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                    objeto = "mancha"
                else:
                    obstaculo_img = PhotoImage(file="vacio.png")
                    obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                if w == 1:
                    desp = 0.1
                elif w == 2:
                    desp = -0.1
                if y == 1:
                    pos = 265
                elif y == 2:
                    pos = 470
                elif y == 3:
                    pos = 685
                # Enemigo 1
                if x == 1:
                    rival_img = PhotoImage(file="enemigo1.png")
                    rival = canvas_mapa.create_image(pos, 0, image=rival_img)
                    while canvas_mapa.coords(rival)[1] < 640:
                        canvas_mapa.move(rival, 0, 0.5)
                        canvas_mapa.move(obstaculo, 0, 0.5)
                        if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                            if objeto == "pizza":
                                puntaje += 500
                                Score_valor = Label(ventana4, text=puntaje, borderwidth=0, highlightthickness=0,
                                                    bg="#EFE4B0", font="Comic 15 bold").place(x=815, y=125)
                                i -= 10
                                if i < 0:
                                    i = 0
                                obstaculo_img = PhotoImage(file="vacio.png")
                                obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                                Hambre_valor = Label(ventana4, text=i, borderwidth=0, highlightthickness=0,
                                                     bg="#EFE4B0",
                                                     font="Comic 15 bold").place(x=825, y=205)
                        ventana4.update()
                # Enemigo 2
                elif x == 2:
                    rival_img = PhotoImage(file="enemigo2.png")
                    rival = canvas_mapa.create_image(pos, 0, image=rival_img)
                    pos_y = canvas_mapa.coords(personaje)[1]
                    if pos == 265:
                        while canvas_mapa.coords(rival)[1] < 550:
                            if canvas_mapa.coords(rival)[1] < 240:
                                canvas_mapa.move(rival, 0, 0.5)
                                canvas_mapa.move(obstaculo, 0, 0.5)
                                if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                    if objeto == "pizza":
                                        puntaje += 500
                                        Score_valor = Label(ventana4, text=puntaje, borderwidth=0, highlightthickness=0,
                                                            bg="#EFE4B0", font="Comic 15 bold").place(x=815, y=125)
                                        i -= 10
                                        if i < 0:
                                            i = 0
                                        obstaculo_img = PhotoImage(file="vacio.png")
                                        obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                                        Hambre_valor = Label(ventana4, text=i, borderwidth=0, highlightthickness=0,
                                                             bg="#EFE4B0",
                                                             font="Comic 15 bold").place(x=825, y=205)
                                ventana4.update()
                            elif canvas_mapa.coords(rival)[1] > 240 and canvas_mapa.coords(rival)[1] < 550:
                                canvas_mapa.move(rival, 0.07, 0.5)
                                canvas_mapa.move(obstaculo, 0, 0.5)
                                if canvas_mapa.coords(obstaculo)[1] + 100 > canvas_mapa.coords(personaje)[1]:
                                    if objeto == "pizza":
                                        puntaje += 500
                                        Score_valor = Label(ventana4, text=puntaje, borderwidth=0,
                                                            highlightthickness=0, bg="#EFE4B0",
                                                            font="Comic 15 bold").place(x=815, y=125)
                                        i -= 10
                                        if i < 0:
                                            i = 0
                                        obstaculo_img = PhotoImage(file="vacio.png")
                                        obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                                        Hambre_valor = Label(ventana4, text=i, borderwidth=0, highlightthickness=0,
                                                             bg="#EFE4B0",
                                                             font="Comic 15 bold").place(x=825, y=205)
                                ventana4.update()
                    elif pos == 470:
                        while canvas_mapa.coords(rival)[1] < 550:
                            if canvas_mapa.coords(rival)[1] < 240:
                                canvas_mapa.move(rival, 0, 0.5)
                                canvas_mapa.move(obstaculo, 0, 0.5)
                                if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                    if objeto == "pizza":
                                        puntaje += 500
                                        Score_valor = Label(ventana4, text=puntaje, borderwidth=0,
                                                            highlightthickness=0, bg="#EFE4B0",
                                                            font="Comic 15 bold").place(x=815, y=125)
                                        i -= 10
                                        if i < 0:
                                            i = 0
                                        obstaculo_img = PhotoImage(file="vacio.png")
                                        obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                                        Hambre_valor = Label(ventana4, text=i, borderwidth=0, highlightthickness=0,
                                                             bg="#EFE4B0",
                                                             font="Comic 15 bold").place(x=825, y=205)
                                ventana4.update()
                            elif canvas_mapa.coords(rival)[1] > 240 and canvas_mapa.coords(rival)[1] < 550:
                                canvas_mapa.move(rival, desp, 0.5)
                                canvas_mapa.move(obstaculo, 0, 0.5)
                                if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                    if objeto == "pizza":
                                        puntaje += 500
                                        Score_valor = Label(ventana4, text=puntaje, borderwidth=0,
                                                            highlightthickness=0, bg="#EFE4B0",
                                                            font="Comic 15 bold").place(x=815, y=125)
                                        i -= 10
                                        if i < 0:
                                            i = 0
                                        obstaculo_img = PhotoImage(file="vacio.png")
                                        obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                                        Hambre_valor = Label(ventana4, text=i, borderwidth=0, highlightthickness=0,
                                                             bg="#EFE4B0",
                                                             font="Comic 15 bold").place(x=825, y=205)
                                ventana4.update()
                    else:
                        while canvas_mapa.coords(rival)[1] < 550:
                            if canvas_mapa.coords(rival)[1] < 240:
                                canvas_mapa.move(rival, 0, 0.5)
                                canvas_mapa.move(obstaculo, 0, 0.5)
                                if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                    if objeto == "pizza":
                                        puntaje += 500
                                        Score_valor = Label(ventana4, text=puntaje, borderwidth=0,
                                                            highlightthickness=0, bg="#EFE4B0",
                                                            font="Comic 15 bold").place(x=815, y=125)
                                        i -= 10
                                        if i < 0:
                                            i = 0
                                        obstaculo_img = PhotoImage(file="vacio.png")
                                        obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                                        Hambre_valor = Label(ventana4, text=i, borderwidth=0, highlightthickness=0,
                                                             bg="#EFE4B0",
                                                             font="Comic 15 bold").place(x=825, y=205)
                                ventana4.update()
                            elif canvas_mapa.coords(rival)[1] > 240 and canvas_mapa.coords(rival)[1] < 550:
                                canvas_mapa.move(rival, -0.07, 0.5)
                                canvas_mapa.move(obstaculo, 0, 0.5)
                                if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                    if canvas_mapa.coords(obstaculo)[0] - 5 > canvas_mapa.coords(personaje)[0] and \
                                                            canvas_mapa.coords(obstaculo)[0] + 5 < \
                                                    canvas_mapa.coords(personaje)[0]:
                                        if objeto == "pizza":
                                            puntaje += 500
                                            Score_valor = Label(ventana4, text=puntaje, borderwidth=0,
                                                                highlightthickness=0, bg="#EFE4B0",
                                                                font="Comic 15 bold").place(x=815, y=125)
                                            i -= 10
                                            if i < 0:
                                                i = 0
                                            obstaculo_img = PhotoImage(file="vacio.png")
                                            obstaculo = canvas_mapa.create_image(trap_or_treasure, 0,
                                                                                 image=obstaculo_img)
                                            Hambre_valor = Label(ventana4, text=i, borderwidth=0, highlightthickness=0,
                                                                 bg="#EFE4B0",
                                                                 font="Comic 15 bold").place(x=825, y=205)
                                ventana4.update()
                # Enemigo 3
                elif x == 3:
                    rival_img = PhotoImage(file="enemigo3.png")
                    rival = canvas_mapa.create_image(pos, 0, image=rival_img)
                    if pos == 470:
                        while canvas_mapa.coords(rival)[1] < 550:
                            if canvas_mapa.coords(rival)[1] < 240:
                                canvas_mapa.move(rival, 0, 0.5)
                                canvas_mapa.move(obstaculo, 0, 0.5)
                                if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                    # if canvas_mapa.coords(obstaculo)[0] - 5 > canvas_mapa.coords(personaje)[0] and canvas_mapa.coords(obstaculo)[0] + 5 < canvas_mapa.coords(personaje)[0]:
                                    if objeto.get() == "pizza":
                                        puntaje += 500
                                        Score_valor = Label(ventana4, text=puntaje, borderwidth=0,
                                                            highlightthickness=0, bg="#EFE4B0",
                                                            font="Comic 15 bold").place(x=815, y=125)
                                        i -= 10
                                        if i < 0:
                                            i = 0
                                        obstaculo_img = PhotoImage(file="vacio.png")
                                        obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                                        Hambre_valor = Label(ventana4, text=i, borderwidth=0, highlightthickness=0,
                                                             bg="#EFE4B0",
                                                             font="Comic 15 bold").place(x=825, y=205)
                                ventana4.update()
                            elif canvas_mapa.coords(rival)[1] > 240 and canvas_mapa.coords(rival)[1] < 550:
                                if canvas_mapa.coords(rival)[1] > 240 and canvas_mapa.coords(rival)[1] < 550:
                                    if canvas_mapa.coords(personaje)[0] > 245 and canvas_mapa.coords(personaje)[
                                        0] < 440:
                                        canvas_mapa.move(rival, -0.07, 0.5)
                                        canvas_mapa.move(obstaculo, 0, 0.5)
                                        if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                            if objeto == "pizza":
                                                puntaje += 500
                                                Score_valor = Label(ventana4, text=puntaje, borderwidth=0,
                                                                    highlightthickness=0, bg="#EFE4B0",
                                                                    font="Comic 15 bold").place(x=815, y=125)
                                                i -= 10
                                                if i < 0:
                                                    i = 0
                                                obstaculo_img = PhotoImage(file="vacio.png")
                                                obstaculo = canvas_mapa.create_image(trap_or_treasure, 0,
                                                                                     image=obstaculo_img)
                                                Hambre_valor = Label(ventana4, text=i, borderwidth=0,
                                                                     highlightthickness=0,
                                                                     bg="#EFE4B0",
                                                                     font="Comic 15 bold").place(x=825, y=205)
                                        ventana4.update()
                                    elif canvas_mapa.coords(personaje)[0] >= 440 and canvas_mapa.coords(personaje)[
                                        0] < 480:
                                        canvas_mapa.move(rival, 0, 0.5)
                                        canvas_mapa.move(obstaculo, 0, 0.5)
                                        if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                            if objeto == "pizza":
                                                puntaje += 500
                                                Score_valor = Label(ventana4, text=puntaje, borderwidth=0,
                                                                    highlightthickness=0, bg="#EFE4B0",
                                                                    font="Comic 15 bold").place(x=815, y=125)
                                                i -= 10
                                                if i < 0:
                                                    i = 0
                                                obstaculo_img = PhotoImage(file="vacio.png")
                                                obstaculo = canvas_mapa.create_image(trap_or_treasure, 0,
                                                                                     image=obstaculo_img)
                                                Hambre_valor = Label(ventana4, text=i, borderwidth=0,
                                                                     highlightthickness=0,
                                                                     bg="#EFE4B0",
                                                                     font="Comic 15 bold").place(x=825, y=205)
                                        ventana4.update()
                                    elif canvas_mapa.coords(personaje)[0] >= 480 and canvas_mapa.coords(personaje)[
                                        0] < 715:
                                        canvas_mapa.move(rival, 0.07, 0.5)
                                        canvas_mapa.move(obstaculo, 0, 0.5)
                                        ventana4.update()
                    elif pos == 265:
                        while canvas_mapa.coords(rival)[1] < 550:
                            if canvas_mapa.coords(rival)[1] < 240:
                                canvas_mapa.move(rival, 0, 0.5)
                                canvas_mapa.move(obstaculo, 0, 0.5)
                                if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                    if objeto == "pizza":
                                        puntaje += 500
                                        Score_valor = Label(ventana4, text=puntaje, borderwidth=0,
                                                            highlightthickness=0, bg="#EFE4B0",
                                                            font="Comic 15 bold").place(x=815, y=125)
                                        i -= 10
                                        if i < 0:
                                            i = 0
                                        obstaculo_img = PhotoImage(file="vacio.png")
                                        obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                                        Hambre_valor = Label(ventana4, text=i, borderwidth=0, highlightthickness=0,
                                                             bg="#EFE4B0",
                                                             font="Comic 15 bold").place(x=825, y=205)
                                        ventana4.update()
                            elif canvas_mapa.coords(rival)[1] > 240 and canvas_mapa.coords(rival)[1] < 550:
                                if canvas_mapa.coords(rival)[1] > 240 and canvas_mapa.coords(rival)[1] < 550:
                                    if canvas_mapa.coords(personaje)[0] > 245 and canvas_mapa.coords(personaje)[
                                        0] < 460:
                                        canvas_mapa.move(rival, 0, 0.5)
                                        canvas_mapa.move(obstaculo, 0, 0.5)
                                        if canvas_mapa.coords(obstaculo)[1] + 100 > canvas_mapa.coords(personaje)[1]:
                                            if objeto == "pizza":
                                                puntaje += 500
                                                Score_valor = Label(ventana4, text=puntaje, borderwidth=0,
                                                                    highlightthickness=0, bg="#EFE4B0",
                                                                    font="Comic 15 bold").place(x=815, y=125)
                                                i -= 10
                                                if i < 0:
                                                    i = 0
                                                obstaculo_img = PhotoImage(file="vacio.png")
                                                obstaculo = canvas_mapa.create_image(trap_or_treasure, 0,
                                                                                     image=obstaculo_img)
                                                Hambre_valor = Label(ventana4, text=i, borderwidth=0,
                                                                     highlightthickness=0,
                                                                     bg="#EFE4B0",
                                                                     font="Comic 15 bold").place(x=825, y=205)
                                        ventana4.update()
                                    elif canvas_mapa.coords(personaje)[0] >= 460 and canvas_mapa.coords(personaje)[
                                        0] < 480:
                                        canvas_mapa.move(rival, 0.07, 0.5)
                                        canvas_mapa.move(obstaculo, 0, 0.5)
                                        if canvas_mapa.coords(obstaculo)[1] + 100 > canvas_mapa.coords(personaje)[1]:
                                            if objeto == "pizza":
                                                puntaje += 500
                                                Score_valor = Label(ventana4, text=puntaje, borderwidth=0,
                                                                    highlightthickness=0, bg="#EFE4B0",
                                                                    font="Comic 15 bold").place(x=815, y=125)
                                                i -= 10
                                                if i < 0:
                                                    i = 0
                                                obstaculo_img = PhotoImage(file="vacio.png")
                                                obstaculo = canvas_mapa.create_image(trap_or_treasure, 0,
                                                                                     image=obstaculo_img)
                                                Hambre_valor = Label(ventana4, text=i, borderwidth=0,
                                                                     highlightthickness=0,
                                                                     bg="#EFE4B0",
                                                                     font="Comic 15 bold").place(x=825, y=205)
                                        ventana4.update()
                                    elif canvas_mapa.coords(personaje)[0] >= 480 and canvas_mapa.coords(personaje)[
                                        0] < 715:
                                        canvas_mapa.move(rival, 0.07, 0.5)
                                        canvas_mapa.move(obstaculo, 0, 0.5)
                                        if canvas_mapa.coords(obstaculo)[1] + 100 > canvas_mapa.coords(personaje)[1]:
                                            if objeto == "pizza":
                                                puntaje += 500
                                                Score_valor = Label(ventana4, text=puntaje, borderwidth=0,
                                                                    highlightthickness=0, bg="#EFE4B0",
                                                                    font="Comic 15 bold").place(x=815, y=125)
                                                i -= 10
                                                if i < 0:
                                                    i = 0
                                                obstaculo_img = PhotoImage(file="vacio.png")
                                                obstaculo = canvas_mapa.create_image(trap_or_treasure, 0,
                                                                                     image=obstaculo_img)
                                                Hambre_valor = Label(ventana4, text=i, borderwidth=0,
                                                                     highlightthickness=0,
                                                                     bg="#EFE4B0",
                                                                     font="Comic 15 bold").place(x=825, y=205)
                                        ventana4.update()
                    else:
                        while canvas_mapa.coords(rival)[1] < 550:
                            if canvas_mapa.coords(rival)[1] < 240:
                                canvas_mapa.move(rival, 0, 0.5)
                                canvas_mapa.move(obstaculo, 0, 0.5)
                                if canvas_mapa.coords(obstaculo)[1] + 100 > canvas_mapa.coords(personaje)[1]:
                                    if objeto == "pizza":
                                        puntaje += 500
                                        Score_valor = Label(ventana4, text=puntaje, borderwidth=0,
                                                            highlightthickness=0, bg="#EFE4B0",
                                                            font="Comic 15 bold").place(x=815, y=125)
                                        i -= 10
                                        if i < 0:
                                            i = 0
                                        obstaculo_img = PhotoImage(file="vacio.png")
                                        obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                                        Hambre_valor = Label(ventana4, text=i, borderwidth=0, highlightthickness=0,
                                                             bg="#EFE4B0",
                                                             font="Comic 15 bold").place(x=825, y=205)
                                ventana4.update()
                            elif canvas_mapa.coords(rival)[1] > 240 and canvas_mapa.coords(rival)[1] < 550:
                                if canvas_mapa.coords(rival)[1] > 240 and canvas_mapa.coords(rival)[1] < 550:
                                    if canvas_mapa.coords(personaje)[0] > 245 and canvas_mapa.coords(personaje)[
                                        0] < 460:
                                        canvas_mapa.move(rival, -0.07, 0.5)
                                        canvas_mapa.move(obstaculo, 0, 0.5)
                                        if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                            if objeto == "pizza":
                                                puntaje += 500
                                                Score_valor = Label(ventana4, text=puntaje, borderwidth=0,
                                                                    highlightthickness=0, bg="#EFE4B0",
                                                                    font="Comic 15 bold").place(x=815, y=125)
                                                i -= 10
                                                if i < 0:
                                                    i = 0
                                                obstaculo_img = PhotoImage(file="vacio.png")
                                                obstaculo = canvas_mapa.create_image(trap_or_treasure, 0,
                                                                                     image=obstaculo_img)
                                                Hambre_valor = Label(ventana4, text=i, borderwidth=0,
                                                                     highlightthickness=0,
                                                                     bg="#EFE4B0",
                                                                     font="Comic 15 bold").place(x=825, y=205)
                                        ventana4.update()
                                    elif canvas_mapa.coords(personaje)[0] >= 460 and canvas_mapa.coords(personaje)[
                                        0] < 480:
                                        canvas_mapa.move(rival, -0.07, 0.5)
                                        canvas_mapa.move(obstaculo, 0, 0.5)
                                        if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                            if objeto == "pizza":
                                                puntaje += 500
                                                Score_valor = Label(ventana4, text=puntaje, borderwidth=0,
                                                                    highlightthickness=0, bg="#EFE4B0",
                                                                    font="Comic 15 bold").place(x=815, y=125)
                                                i -= 10
                                                if i < 0:
                                                    i = 0
                                                obstaculo_img = PhotoImage(file="vacio.png")
                                                obstaculo = canvas_mapa.create_image(trap_or_treasure, 0,
                                                                                     image=obstaculo_img)
                                                Hambre_valor = Label(ventana4, text=i, borderwidth=0,
                                                                     highlightthickness=0,
                                                                     bg="#EFE4B0",
                                                                     font="Comic 15 bold").place(x=825, y=205)
                                        ventana4.update()
                                    elif canvas_mapa.coords(personaje)[0] >= 480 and canvas_mapa.coords(personaje)[
                                        0] < 715:
                                        canvas_mapa.move(rival, 0, 0.5)
                                        canvas_mapa.move(obstaculo, 0, 0.5)
                                        if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                            if objeto == "pizza":
                                                puntaje += 500
                                                Score_valor = Label(ventana4, text=puntaje, borderwidth=0,
                                                                    highlightthickness=0, bg="#EFE4B0",
                                                                    font="Comic 15 bold").place(x=815, y=125)
                                                i -= 10
                                                if i < 0:
                                                    i = 0
                                                obstaculo_img = PhotoImage(file="vacio.png")
                                                obstaculo = canvas_mapa.create_image(trap_or_treasure, 0,
                                                                                     image=obstaculo_img)
                                                Hambre_valor = Label(ventana4, text=i, borderwidth=0,
                                                                     highlightthickness=0,
                                                                     bg="#EFE4B0",
                                                                     font="Comic 15 bold").place(x=825, y=205)
                                        ventana4.update()

            enemigos()

        ventana4.mainloop()
    elif variable_mapa == 5:
        global rival, rival_img
        ventana_principal.destroy()
        ventana5 = Tk()
        ventana5.title("Road Figther Plus")
        ventana5.geometry("950x600")
        # Mapa e interfaz del jugador
        canvas_mapa = Canvas(ventana5, width=950, height=600, borderwidth=0, highlightthickness=0)
        img_mapa = PhotoImage(file="mapa2.png")
        mapa = canvas_mapa.create_image(473, -2400, image=img_mapa)
        # global img_personaje
        img_personaje = PhotoImage(file="skate main.png")
        personaje = canvas_mapa.create_image(475, 510, image=img_personaje)
        img_caidap = PhotoImage(file="caida.png")
        canvas_mapa.pack()
        # barras laterales
        i = 0
        texto_nombre = entrada.get()
        nombre_valor = Label(ventana5, text=texto_nombre, borderwidth=0, highlightthickness=0, bg="#EFE4B0",
                             font="Comic 15 bold").place(x=805, y=45)
        Score = Label(ventana5, text="Score", borderwidth=0, highlightthickness=0, bg="#EFE4B0",
                      font="Comic 15 bold").place(x=805, y=100)
        Score_valor = Label(ventana5, text=puntaje, borderwidth=0, highlightthickness=0, bg="#EFE4B0",
                            font="Comic 15 bold").place(x=815, y=125)
        Hambre = Label(ventana5, text="Hunger", borderwidth=0, highlightthickness=0, bg="#EFE4B0",
                       font="Comic 15 bold").place(x=800, y=180)
        Hambre_valor = Label(ventana5, text=i, borderwidth=0, highlightthickness=0, bg="#EFE4B0",
                             font="Comic 15 bold").place(x=825, y=205)

        # Funciones

        while i <= 98:
            lista = list(time.localtime())
            if lista[5] != 0:
                if lista[5] % 1 == 0:
                    i += 2
            Hambre_valor = Label(ventana5, text=i, borderwidth=0, highlightthickness=0, bg="#EFE4B0",
                                 font="Comic 15 bold").place(x=825, y=205)

            vel = 0
            canvas_mapa.after(1)

            def enemigos():
                def movimiento(event):
                    global caidap, personaje, img_personaje, vel, i
                    if event.keysym == "Left":
                        if i < 100:
                            if int(canvas_mapa.coords(personaje)[0]) > 247:
                                canvas_mapa.move(personaje, 0 - vel, 0)
                                canvas_mapa.move(mapa, 0, 0 + vel)
                                vel += 0.1
                            else:
                                img_personaje = PhotoImage(file="caida.png")
                                personaje = canvas_mapa.create_image(245, 510, image=img_personaje)
                                ventana5.update()
                                canvas_mapa.after(100)
                                canvas_mapa.delete(personaje)
                                img_personaje = PhotoImage(file="skate main.png")
                                personaje = canvas_mapa.create_image(475, 510, image=img_personaje)
                                i += 10
                                if i > 100:
                                    i = 100
                                Hambre_valor = Label(ventana5, text=i, borderwidth=0, highlightthickness=0,
                                                     bg="#EFE4B0",
                                                     font="Comic 15 bold").place(x=825, y=205)

                    if event.keysym == "Up":
                        if i < 100:
                            if int(canvas_mapa.coords(personaje)[0]) < 715:
                                canvas_mapa.move(personaje, 0 + vel, 0)
                                canvas_mapa.move(mapa, 0, 0 + vel)
                                vel += 0.1
                            else:
                                img_personaje = PhotoImage(file="caida.png")
                                personaje = canvas_mapa.create_image(715, 510, image=img_personaje)
                                ventana5.update()
                                canvas_mapa.after(100)
                                canvas_mapa.delete(personaje)
                                img_personaje = PhotoImage(file="skate main.png")
                                personaje = canvas_mapa.create_image(475, 510, image=img_personaje)
                                i += 10
                                if i > 100:
                                    i = 100
                                Hambre_valor = Label(ventana5, text=i, borderwidth=0, highlightthickness=0,
                                                     bg="#EFE4B0",
                                                     font="Comic 15 bold").place(x=825, y=205)
                    if event.keysym == "Down":
                        if i < 100:
                            if int(canvas_mapa.coords(personaje)[0]) > 245:
                                vel += 0.4
                                canvas_mapa.move(mapa, 0, vel)
                                canvas_mapa.move(personaje, -vel, 0)
                            else:
                                img_personaje = PhotoImage(file="caida.png")
                                personaje = canvas_mapa.create_image(245, 510, image=img_personaje)
                                ventana5.update()
                                canvas_mapa.after(100)
                                canvas_mapa.delete(personaje)
                                img_personaje = PhotoImage(file="skate main.png")
                                personaje = canvas_mapa.create_image(475, 510, image=img_personaje)
                                i += 10
                                if i > 100:
                                    i = 100
                                Hambre_valor = Label(ventana5, text=i, borderwidth=0, highlightthickness=0,
                                                     bg="#EFE4B0",
                                                     font="Comic 15 bold").place(x=825, y=205)
                    if event.keysym == "Right":
                        if i < 100:
                            if int(canvas_mapa.coords(personaje)[0]) < 715:
                                vel += 0.4
                                canvas_mapa.move(personaje, vel, 0)
                                canvas_mapa.move(mapa, 0, vel)
                            else:
                                img_personaje = PhotoImage(file="caida.png")
                                personaje = canvas_mapa.create_image(715, 510, image=img_personaje)
                                ventana5.update()
                                canvas_mapa.after(500)
                                canvas_mapa.delete(personaje)
                                img_personaje = PhotoImage(file="skate main.png")
                                personaje = canvas_mapa.create_image(470, 510, image=img_personaje)
                                i += 10
                                if i > 100:
                                    i = 100
                                Hambre_valor = Label(ventana5, text=i, borderwidth=0, highlightthickness=0,
                                                     bg="#EFE4B0",
                                                     font="Comic 15 bold").place(x=825, y=205)

                canvas_mapa.bind_all("<Up>", movimiento)
                canvas_mapa.bind_all("<Left>", movimiento)
                canvas_mapa.bind_all("<Right>", movimiento)
                canvas_mapa.bind_all("<Down>", movimiento)

                global rival, rival_img, puntaje, i
                x = random.randint(1, 3)
                y = random.randint(1, 3)
                w = random.randint(1, 2)
                z = random.randint(1, 2)
                objeto = StringVar()
                if z == 1:
                    trap_or_treasure = 345
                else:
                    trap_or_treasure = 617
                tinta_o_pizza = random.randint(1, 10)
                if tinta_o_pizza == 3:
                    obstaculo_img = PhotoImage(file="pizza.png")
                    obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                    objeto = "pizza"
                elif tinta_o_pizza == 8:
                    obstaculo_img = PhotoImage(file="mancha.png")
                    obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                    objeto = "mancha"
                else:
                    obstaculo_img = PhotoImage(file="vacio.png")
                    obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                if w == 1:
                    desp = 0.1
                elif w == 2:
                    desp = -0.1
                if y == 1:
                    pos = 265
                elif y == 2:
                    pos = 470
                elif y == 3:
                    pos = 685
                # Enemigo 1
                if x == 1:
                    rival_img = PhotoImage(file="enemigo1.png")
                    rival = canvas_mapa.create_image(pos, 0, image=rival_img)
                    while canvas_mapa.coords(rival)[1] < 640:
                        canvas_mapa.move(rival, 0, 0.4)
                        canvas_mapa.move(obstaculo, 0, 0.4)
                        if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                            if objeto == "pizza":
                                puntaje += 500
                                Score_valor = Label(ventana5, text=puntaje, borderwidth=0, highlightthickness=0,
                                                    bg="#EFE4B0", font="Comic 15 bold").place(x=815, y=125)
                                i -= 10
                                if i < 0:
                                    i = 0
                                obstaculo_img = PhotoImage(file="vacio.png")
                                obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                                Hambre_valor = Label(ventana5, text=i, borderwidth=0, highlightthickness=0,
                                                     bg="#EFE4B0",
                                                     font="Comic 15 bold").place(x=825, y=205)
                        ventana5.update()
                # Enemigo 2
                elif x == 2:
                    rival_img = PhotoImage(file="enemigo2.png")
                    rival = canvas_mapa.create_image(pos, 0, image=rival_img)
                    pos_y = canvas_mapa.coords(personaje)[1]
                    if pos == 265:
                        while canvas_mapa.coords(rival)[1] < 550:
                            if canvas_mapa.coords(rival)[1] < 240:
                                canvas_mapa.move(rival, 0, 0.4)
                                canvas_mapa.move(obstaculo, 0, 0.4)
                                if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                    if objeto == "pizza":
                                        puntaje += 500
                                        Score_valor = Label(ventana5, text=puntaje, borderwidth=0, highlightthickness=0,
                                                            bg="#EFE4B0", font="Comic 15 bold").place(x=815, y=125)
                                        i -= 10
                                        if i < 0:
                                            i = 0
                                        obstaculo_img = PhotoImage(file="vacio.png")
                                        obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                                        Hambre_valor = Label(ventana5, text=i, borderwidth=0, highlightthickness=0,
                                                             bg="#EFE4B0",
                                                             font="Comic 15 bold").place(x=825, y=205)
                                ventana5.update()
                            elif canvas_mapa.coords(rival)[1] > 240 and canvas_mapa.coords(rival)[1] < 550:
                                canvas_mapa.move(rival, 0.07, 0.4)
                                canvas_mapa.move(obstaculo, 0, 0.4)
                                if canvas_mapa.coords(obstaculo)[1] + 100 > canvas_mapa.coords(personaje)[1]:
                                    if objeto == "pizza":
                                        puntaje += 500
                                        Score_valor = Label(ventana5, text=puntaje, borderwidth=0,
                                                            highlightthickness=0, bg="#EFE4B0",
                                                            font="Comic 15 bold").place(x=815, y=125)
                                        i -= 10
                                        if i < 0:
                                            i = 0
                                        obstaculo_img = PhotoImage(file="vacio.png")
                                        obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                                        Hambre_valor = Label(ventana5, text=i, borderwidth=0, highlightthickness=0,
                                                             bg="#EFE4B0",
                                                             font="Comic 15 bold").place(x=825, y=205)
                                ventana5.update()
                    elif pos == 470:
                        while canvas_mapa.coords(rival)[1] < 550:
                            if canvas_mapa.coords(rival)[1] < 240:
                                canvas_mapa.move(rival, 0, 0.4)
                                canvas_mapa.move(obstaculo, 0, 0.4)
                                if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                    if objeto == "pizza":
                                        puntaje += 500
                                        Score_valor = Label(ventana5, text=puntaje, borderwidth=0,
                                                            highlightthickness=0, bg="#EFE4B0",
                                                            font="Comic 15 bold").place(x=815, y=125)
                                        i -= 10
                                        if i < 0:
                                            i = 0
                                        obstaculo_img = PhotoImage(file="vacio.png")
                                        obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                                        Hambre_valor = Label(ventana5, text=i, borderwidth=0, highlightthickness=0,
                                                             bg="#EFE4B0",
                                                             font="Comic 15 bold").place(x=825, y=205)
                                ventana5.update()
                            elif canvas_mapa.coords(rival)[1] > 240 and canvas_mapa.coords(rival)[1] < 550:
                                canvas_mapa.move(rival, desp, 0.4)
                                canvas_mapa.move(obstaculo, 0, 0.4)
                                if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                    if objeto == "pizza":
                                        puntaje += 500
                                        Score_valor = Label(ventana5, text=puntaje, borderwidth=0,
                                                            highlightthickness=0, bg="#EFE4B0",
                                                            font="Comic 15 bold").place(x=815, y=125)
                                        i -= 10
                                        if i < 0:
                                            i = 0
                                        obstaculo_img = PhotoImage(file="vacio.png")
                                        obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                                        Hambre_valor = Label(ventana5, text=i, borderwidth=0, highlightthickness=0,
                                                             bg="#EFE4B0",
                                                             font="Comic 15 bold").place(x=825, y=205)
                                ventana5.update()
                    else:
                        while canvas_mapa.coords(rival)[1] < 550:
                            if canvas_mapa.coords(rival)[1] < 240:
                                canvas_mapa.move(rival, 0, 0.4)
                                canvas_mapa.move(obstaculo, 0, 0.4)
                                if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                    if objeto == "pizza":
                                        puntaje += 500
                                        Score_valor = Label(ventana5, text=puntaje, borderwidth=0,
                                                            highlightthickness=0, bg="#EFE4B0",
                                                            font="Comic 15 bold").place(x=815, y=125)
                                        i -= 10
                                        if i < 0:
                                            i = 0
                                        obstaculo_img = PhotoImage(file="vacio.png")
                                        obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                                        Hambre_valor = Label(ventana5, text=i, borderwidth=0, highlightthickness=0,
                                                             bg="#EFE4B0",
                                                             font="Comic 15 bold").place(x=825, y=205)
                                ventana5.update()
                            elif canvas_mapa.coords(rival)[1] > 240 and canvas_mapa.coords(rival)[1] < 550:
                                canvas_mapa.move(rival, -0.07, 0.4)
                                canvas_mapa.move(obstaculo, 0, 0.4)
                                if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                    if canvas_mapa.coords(obstaculo)[0] - 5 > canvas_mapa.coords(personaje)[0] and \
                                                            canvas_mapa.coords(obstaculo)[0] + 5 < \
                                                    canvas_mapa.coords(personaje)[0]:
                                        if objeto == "pizza":
                                            puntaje += 500
                                            Score_valor = Label(ventana5, text=puntaje, borderwidth=0,
                                                                highlightthickness=0, bg="#EFE4B0",
                                                                font="Comic 15 bold").place(x=815, y=125)
                                            i -= 10
                                            if i < 0:
                                                i = 0
                                            obstaculo_img = PhotoImage(file="vacio.png")
                                            obstaculo = canvas_mapa.create_image(trap_or_treasure, 0,
                                                                                 image=obstaculo_img)
                                            Hambre_valor = Label(ventana5, text=i, borderwidth=0, highlightthickness=0,
                                                                 bg="#EFE4B0",
                                                                 font="Comic 15 bold").place(x=825, y=205)
                                ventana5.update()
                # Enemigo 3
                elif x == 3:
                    rival_img = PhotoImage(file="enemigo3.png")
                    rival = canvas_mapa.create_image(pos, 0, image=rival_img)
                    if pos == 470:
                        while canvas_mapa.coords(rival)[1] < 550:
                            if canvas_mapa.coords(rival)[1] < 240:
                                canvas_mapa.move(rival, 0, 0.4)
                                canvas_mapa.move(obstaculo, 0, 0.4)
                                if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                    # if canvas_mapa.coords(obstaculo)[0] - 5 > canvas_mapa.coords(personaje)[0] and canvas_mapa.coords(obstaculo)[0] + 5 < canvas_mapa.coords(personaje)[0]:
                                    if objeto.get() == "pizza":
                                        puntaje += 500
                                        Score_valor = Label(ventana5, text=puntaje, borderwidth=0,
                                                            highlightthickness=0, bg="#EFE4B0",
                                                            font="Comic 15 bold").place(x=815, y=125)
                                        i -= 10
                                        if i < 0:
                                            i = 0
                                        obstaculo_img = PhotoImage(file="vacio.png")
                                        obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                                        Hambre_valor = Label(ventana5, text=i, borderwidth=0, highlightthickness=0,
                                                             bg="#EFE4B0",
                                                             font="Comic 15 bold").place(x=825, y=205)
                                ventana5.update()
                            elif canvas_mapa.coords(rival)[1] > 240 and canvas_mapa.coords(rival)[1] < 550:
                                if canvas_mapa.coords(rival)[1] > 240 and canvas_mapa.coords(rival)[1] < 550:
                                    if canvas_mapa.coords(personaje)[0] > 245 and canvas_mapa.coords(personaje)[
                                        0] < 440:
                                        canvas_mapa.move(rival, -0.07, 0.4)
                                        canvas_mapa.move(obstaculo, 0, 0.4)
                                        if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                            if objeto == "pizza":
                                                puntaje += 500
                                                Score_valor = Label(ventana5, text=puntaje, borderwidth=0,
                                                                    highlightthickness=0, bg="#EFE4B0",
                                                                    font="Comic 15 bold").place(x=815, y=125)
                                                i -= 10
                                                if i < 0:
                                                    i = 0
                                                obstaculo_img = PhotoImage(file="vacio.png")
                                                obstaculo = canvas_mapa.create_image(trap_or_treasure, 0,
                                                                                     image=obstaculo_img)
                                                Hambre_valor = Label(ventana5, text=i, borderwidth=0,
                                                                     highlightthickness=0,
                                                                     bg="#EFE4B0",
                                                                     font="Comic 15 bold").place(x=825, y=205)
                                        ventana5.update()
                                    elif canvas_mapa.coords(personaje)[0] >= 440 and canvas_mapa.coords(personaje)[
                                        0] < 480:
                                        canvas_mapa.move(rival, 0, 0.4)
                                        canvas_mapa.move(obstaculo, 0, 0.4)
                                        if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                            if objeto == "pizza":
                                                puntaje += 500
                                                Score_valor = Label(ventana5, text=puntaje, borderwidth=0,
                                                                    highlightthickness=0, bg="#EFE4B0",
                                                                    font="Comic 15 bold").place(x=815, y=125)
                                                i -= 10
                                                if i < 0:
                                                    i = 0
                                                obstaculo_img = PhotoImage(file="vacio.png")
                                                obstaculo = canvas_mapa.create_image(trap_or_treasure, 0,
                                                                                     image=obstaculo_img)
                                                Hambre_valor = Label(ventana5, text=i, borderwidth=0,
                                                                     highlightthickness=0,
                                                                     bg="#EFE4B0",
                                                                     font="Comic 15 bold").place(x=825, y=205)
                                        ventana5.update()
                                    elif canvas_mapa.coords(personaje)[0] >= 480 and canvas_mapa.coords(personaje)[
                                        0] < 715:
                                        canvas_mapa.move(rival, 0.07, 0.4)
                                        canvas_mapa.move(obstaculo, 0, 0.4)
                                        ventana5.update()
                    elif pos == 265:
                        while canvas_mapa.coords(rival)[1] < 550:
                            if canvas_mapa.coords(rival)[1] < 240:
                                canvas_mapa.move(rival, 0, 0.4)
                                canvas_mapa.move(obstaculo, 0, 0.4)
                                if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                    if objeto == "pizza":
                                        puntaje += 500
                                        Score_valor = Label(ventana5, text=puntaje, borderwidth=0,
                                                            highlightthickness=0, bg="#EFE4B0",
                                                            font="Comic 15 bold").place(x=815, y=125)
                                        i -= 10
                                        if i < 0:
                                            i = 0
                                        obstaculo_img = PhotoImage(file="vacio.png")
                                        obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                                        Hambre_valor = Label(ventana5, text=i, borderwidth=0, highlightthickness=0,
                                                             bg="#EFE4B0",
                                                             font="Comic 15 bold").place(x=825, y=205)
                                        ventana5.update()
                            elif canvas_mapa.coords(rival)[1] > 240 and canvas_mapa.coords(rival)[1] < 550:
                                if canvas_mapa.coords(rival)[1] > 240 and canvas_mapa.coords(rival)[1] < 550:
                                    if canvas_mapa.coords(personaje)[0] > 245 and canvas_mapa.coords(personaje)[
                                        0] < 460:
                                        canvas_mapa.move(rival, 0, 0.4)
                                        canvas_mapa.move(obstaculo, 0, 0.4)
                                        if canvas_mapa.coords(obstaculo)[1] + 100 > canvas_mapa.coords(personaje)[1]:
                                            if objeto == "pizza":
                                                puntaje += 500
                                                Score_valor = Label(ventana5, text=puntaje, borderwidth=0,
                                                                    highlightthickness=0, bg="#EFE4B0",
                                                                    font="Comic 15 bold").place(x=815, y=125)
                                                i -= 10
                                                if i < 0:
                                                    i = 0
                                                obstaculo_img = PhotoImage(file="vacio.png")
                                                obstaculo = canvas_mapa.create_image(trap_or_treasure, 0,
                                                                                     image=obstaculo_img)
                                                Hambre_valor = Label(ventana5, text=i, borderwidth=0,
                                                                     highlightthickness=0,
                                                                     bg="#EFE4B0",
                                                                     font="Comic 15 bold").place(x=825, y=205)
                                        ventana5.update()
                                    elif canvas_mapa.coords(personaje)[0] >= 460 and canvas_mapa.coords(personaje)[
                                        0] < 480:
                                        canvas_mapa.move(rival, 0.07, 0.4)
                                        canvas_mapa.move(obstaculo, 0, 0.4)
                                        if canvas_mapa.coords(obstaculo)[1] + 100 > canvas_mapa.coords(personaje)[1]:
                                            if objeto == "pizza":
                                                puntaje += 500
                                                Score_valor = Label(ventana5, text=puntaje, borderwidth=0,
                                                                    highlightthickness=0, bg="#EFE4B0",
                                                                    font="Comic 15 bold").place(x=815, y=125)
                                                i -= 10
                                                if i < 0:
                                                    i = 0
                                                obstaculo_img = PhotoImage(file="vacio.png")
                                                obstaculo = canvas_mapa.create_image(trap_or_treasure, 0,
                                                                                     image=obstaculo_img)
                                                Hambre_valor = Label(ventana5, text=i, borderwidth=0,
                                                                     highlightthickness=0,
                                                                     bg="#EFE4B0",
                                                                     font="Comic 15 bold").place(x=825, y=205)
                                        ventana5.update()
                                    elif canvas_mapa.coords(personaje)[0] >= 480 and canvas_mapa.coords(personaje)[
                                        0] < 715:
                                        canvas_mapa.move(rival, 0.07, 0.4)
                                        canvas_mapa.move(obstaculo, 0, 0.4)
                                        if canvas_mapa.coords(obstaculo)[1] + 100 > canvas_mapa.coords(personaje)[1]:
                                            if objeto == "pizza":
                                                puntaje += 500
                                                Score_valor = Label(ventana5, text=puntaje, borderwidth=0,
                                                                    highlightthickness=0, bg="#EFE4B0",
                                                                    font="Comic 15 bold").place(x=815, y=125)
                                                i -= 10
                                                if i < 0:
                                                    i = 0
                                                obstaculo_img = PhotoImage(file="vacio.png")
                                                obstaculo = canvas_mapa.create_image(trap_or_treasure, 0,
                                                                                     image=obstaculo_img)
                                                Hambre_valor = Label(ventana5, text=i, borderwidth=0,
                                                                     highlightthickness=0,
                                                                     bg="#EFE4B0",
                                                                     font="Comic 15 bold").place(x=825, y=205)
                                        ventana5.update()
                    else:
                        while canvas_mapa.coords(rival)[1] < 550:
                            if canvas_mapa.coords(rival)[1] < 240:
                                canvas_mapa.move(rival, 0, 0.4)
                                canvas_mapa.move(obstaculo, 0, 0.4)
                                if canvas_mapa.coords(obstaculo)[1] + 100 > canvas_mapa.coords(personaje)[1]:
                                    if objeto == "pizza":
                                        puntaje += 500
                                        Score_valor = Label(ventana5, text=puntaje, borderwidth=0,
                                                            highlightthickness=0, bg="#EFE4B0",
                                                            font="Comic 15 bold").place(x=815, y=125)
                                        i -= 10
                                        if i < 0:
                                            i = 0
                                        obstaculo_img = PhotoImage(file="vacio.png")
                                        obstaculo = canvas_mapa.create_image(trap_or_treasure, 0, image=obstaculo_img)
                                        Hambre_valor = Label(ventana5, text=i, borderwidth=0, highlightthickness=0,
                                                             bg="#EFE4B0",
                                                             font="Comic 15 bold").place(x=825, y=205)
                                ventana5.update()
                            elif canvas_mapa.coords(rival)[1] > 240 and canvas_mapa.coords(rival)[1] < 550:
                                if canvas_mapa.coords(rival)[1] > 240 and canvas_mapa.coords(rival)[1] < 550:
                                    if canvas_mapa.coords(personaje)[0] > 245 and canvas_mapa.coords(personaje)[
                                        0] < 460:
                                        canvas_mapa.move(rival, -0.07, 0.4)
                                        canvas_mapa.move(obstaculo, 0, 0.4)
                                        if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                            if objeto == "pizza":
                                                puntaje += 500
                                                Score_valor = Label(ventana5, text=puntaje, borderwidth=0,
                                                                    highlightthickness=0, bg="#EFE4B0",
                                                                    font="Comic 15 bold").place(x=815, y=125)
                                                i -= 10
                                                if i < 0:
                                                    i = 0
                                                obstaculo_img = PhotoImage(file="vacio.png")
                                                obstaculo = canvas_mapa.create_image(trap_or_treasure, 0,
                                                                                     image=obstaculo_img)
                                                Hambre_valor = Label(ventana5, text=i, borderwidth=0,
                                                                     highlightthickness=0,
                                                                     bg="#EFE4B0",
                                                                     font="Comic 15 bold").place(x=825, y=205)
                                        ventana5.update()
                                    elif canvas_mapa.coords(personaje)[0] >= 460 and canvas_mapa.coords(personaje)[
                                        0] < 480:
                                        canvas_mapa.move(rival, -0.07, 0.4)
                                        canvas_mapa.move(obstaculo, 0, 0.4)
                                        if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                            if objeto == "pizza":
                                                puntaje += 500
                                                Score_valor = Label(ventana5, text=puntaje, borderwidth=0,
                                                                    highlightthickness=0, bg="#EFE4B0",
                                                                    font="Comic 15 bold").place(x=815, y=125)
                                                i -= 10
                                                if i < 0:
                                                    i = 0
                                                obstaculo_img = PhotoImage(file="vacio.png")
                                                obstaculo = canvas_mapa.create_image(trap_or_treasure, 0,
                                                                                     image=obstaculo_img)
                                                Hambre_valor = Label(ventana5, text=i, borderwidth=0,
                                                                     highlightthickness=0,
                                                                     bg="#EFE4B0",
                                                                     font="Comic 15 bold").place(x=825, y=205)
                                        ventana5.update()
                                    elif canvas_mapa.coords(personaje)[0] >= 480 and canvas_mapa.coords(personaje)[
                                        0] < 715:
                                        canvas_mapa.move(rival, 0, 0.4)
                                        canvas_mapa.move(obstaculo, 0, 0.4)
                                        if canvas_mapa.coords(obstaculo)[1] + 100 > 610:
                                            if objeto == "pizza":
                                                puntaje += 500
                                                Score_valor = Label(ventana5, text=puntaje, borderwidth=0,
                                                                    highlightthickness=0, bg="#EFE4B0",
                                                                    font="Comic 15 bold").place(x=815, y=125)
                                                i -= 10
                                                if i < 0:
                                                    i = 0
                                                obstaculo_img = PhotoImage(file="vacio.png")
                                                obstaculo = canvas_mapa.create_image(trap_or_treasure, 0,
                                                                                     image=obstaculo_img)
                                                Hambre_valor = Label(ventana5, text=i, borderwidth=0,
                                                                     highlightthickness=0,
                                                                     bg="#EFE4B0",
                                                                     font="Comic 15 bold").place(x=825, y=205)
                                        ventana5.update()

            enemigos()

        ventana5.mainloop()


# Botones

RDP = PhotoImage(file="RDP.png")
Road_fighter = Label(ventana_principal, image=RDP, borderwidth=0, highlightthickness=0).place(x=280, y=40)

SinglePlayer = PhotoImage(file="Single.png")
solitario = Button(image=SinglePlayer, bg="Black", borderwidth=0, highlightthickness=0, command=abrir_mapa_1).place(
    x=200, y=230)

MultiPlayer = PhotoImage(file="Multiplayer.png")
multiplayer = Button(image=MultiPlayer, bg="Black", borderwidth=0, highlightthickness=0).place(x=500, y=230)

How_to_play = Button(text="Instrucciones", font=(12), bg="Black", fg="white", activebackground="white", command=ayuda,
                     borderwidth=0, highlightthickness=0).place(x=550, y=430)

# Niveles
global entrada
entrada = StringVar()
nombre = Label(ventana_principal, text="Nombre", font=(12), bg="black", fg="white").place(x=135, y=470)
nombre_input = Entry(ventana_principal, font=(12), textvariable=entrada).place(x=200, y=470)
nivel = Label(ventana_principal, text="Nivel", font=(12), bg="black", fg="white").place(x=135, y=430)

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