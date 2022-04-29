# Importamos La libreria Turtle (El modulo principal con lo que haremos el juego), time y ramdon (Estos lo utilizaremos para darle algunas
# caracteristicas del juego)
import turtle, time, random

# Creamos nuetra ventana donde se ejecutara el juego, le damos una alto y ancho de 450px fondo negro y un titulo.
juego = turtle.Screen()
juego.setup(width=450, height=450)
juego.title('Juego de la Serpiente')
juego.bgcolor('black')

# Creamos a un puntor que sera nuestra serpiente, y definimos sus caracteristicas
piton = turtle.Turtle()
piton.color('#009982')
piton.penup()
piton.shape('circle')
piton.speed(0)
piton.goto(-150, -140)
piton.speed(2)
# Creamos una variable que nos indicara la direccion del movimento de la serpiente, en un principio sere stop, no se movera.
posicion = 'stop'

# Creemos nuestra funcion para los movimientos de nuestra serpiente, lo cuara hara que segun el valor de nuestra variable posicion, nuestra serpiente se
# movera.
def movimientos():
    global posicion
    if posicion == 'up':
        y = piton.ycor()
        piton.sety(y + 10)
    elif posicion == 'down':
        y = piton.ycor()
        piton.sety(y - 10)    
    elif posicion == 'left':
        x = piton.xcor()
        piton.setx(x - 10)
    elif posicion == 'right':
        x = piton.xcor()
        piton.setx(x + 10)

# Ahora generamos nuestras funciones para cambiar el valor de la variable posicion, y con estas fuinciones haremos que cuando se presione unas
# teclas se llamen esas funciones cambiando el valor de posicion y por tanto, hacer mover a la serpiente segun las teclas

def up():
    global posicion
    posicion = 'up'
def down():
    global posicion
    posicion = 'down'
def left():
    global posicion
    posicion = 'left'
def right():
    global posicion
    posicion = 'right'

# creamos otro ´puntor para que nos cree las paredes dentro de la pantalla.
pared = turtle.Turtle()
pared.shape('square')
pared.color('white')
pared.penup()
# pared.ht()
pared.speed(0)
pared.goto(-215, 180)
pared.pensize(20)
pared.pendown()
for i in range(1, 5):
    if i % 2 != 0:
        pared.forward(425)
        pared.right(90)
        continue
    pared.forward(390)
    pared.right(90)
pared.right(90)
pared.forward(240)
pared.right(270)
pared.forward(50)
pared.penup()
pared.forward(70)
pared.pendown()
pared.forward(30)
pared.right(270)
pared.forward(80)
pared.penup()
pared.forward(70)
pared.pendown()
pared.forward(90)
pared.right(90)
pared.forward(150)
pared.right(90)
pared.forward(80)
pared.right(180)
pared.forward(80)
pared.right(90)
pared.forward(125)
pared.right(90)
pared.forward(250)
pared.right(90)
pared.forward(140)
pared.right(270)
pared.forward(40)
pared.ht()

# Ahora creams nustras funciones de turtle que hacer que cuando se presionen las teclas (arriba, abajo, derecha y izquierda), el valor de posicion
# cambia segun estas, de tal manera que nuestro puntor piton se movera hacia la direccion que queramos.
juego.listen()
turtle.onkeypress(up, 'Up')
turtle.onkeypress(down, 'Down')
turtle.onkeypress(left, 'Left')
turtle.onkeypress(right, 'Right')

# Creamos el ciclo infinito principal donde correra el juego.
while True:
    # dentro de este ciclo estara llamandose la funcion movimiento que hara que se mueva el piton de acuedor a las teclas que presionemos.
    # y es muy importante ir actualizando la pantalla constantemnete ya que asi se actualizaria el nuevo movimiento de la piton y podriamos 
    # visalizar como se mueve.

    juego.update()
    movimientos()
    juego.delay(30)
