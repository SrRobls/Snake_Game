# Importamos La libreria Turtle (El modulo principal con lo que haremos el juego), time y ramdon (Estos lo utilizaremos para darle algunas
# caracteristicas del juego)
import turtle, time, random

# Creamos nuetra ventana donde se ejecutara el juego, le damos una alto y ancho de 450px fondo negro y un titulo.
juego = turtle.Screen()
juego.setup(width=450, height=450)
juego.title('Juego de la Serpiente')
juego.bgcolor('black')
juego.mainloop()