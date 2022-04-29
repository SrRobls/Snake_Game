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
piton.speed(2)
piton.goto(0, 0)
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
    movimientos()
    juego.update()


turtle.done()