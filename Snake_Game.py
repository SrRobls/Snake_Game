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
tamanio_piton = 1
piton.color('green')
piton.penup()
piton.shape('square')
piton.speed(0)
piton.goto(-150, -140)
piton.speed(0)
cuerpo_serpiente = []
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

# creamos otro puntor para que nos cree las paredes dentro de la pantalla.
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
pared.forward(90)
pared.right(180)
pared.forward(90)
pared.right(90)
pared.forward(125)
pared.right(90)
pared.forward(250)
pared.right(90)
pared.forward(140)
pared.right(270)
pared.forward(40)
pared.ht()

# Creemos el puntero Comida
manzana = turtle.Turtle()
manzana.color('red')
manzana.penup()
manzana.shape('circle')
manzana.shapesize(0.7)
manzana.speed(0)
tiempo = 0

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

    # cuando nuestra serpiente toca algunas de las paredes, entonces muere
    if piton.xcor() <= -195 or piton.xcor() >= 190 or piton.ycor() >= 160 or piton.ycor() <= -190:
        time.sleep(0.5)
        piton.goto(-150, -140)
    # cuando la serpiente toque los obstaculos entonces muere, este condicional es largo ya que tuve que dar con la posicion de cada uno de los obstaculos.
    if ((piton.xcor() >= -195 and piton.xcor() <= -148) and (piton.ycor() >= -80 and piton.ycor() <= -40)) or ((piton.xcor() >= -115 and piton.xcor() <= -60) and (piton.ycor() >= -75 and piton.ycor() <= -40)) or ((piton.xcor() >= -85 and piton.xcor() <= -45) and (piton.ycor() >= -80 and piton.ycor() <= 30)) or ((piton.xcor() >= 50 and piton.xcor() <= 225) and (piton.ycor() <= -48 and piton.ycor() >= -90)) or ((piton.xcor() >= 50 and piton.xcor() <= 90) and (piton.ycor() <= -48 and piton.ycor() >= -125)) or ((piton.xcor() >= -85 and piton.xcor() <= -45) and (piton.ycor() <= 190 and piton.ycor() >= 70)) or ((piton.xcor() >= 65 and piton.xcor() <= 105) and (piton.ycor() <= 190 and piton.ycor() >= 70)):
        time.sleep(0.5)
        piton.goto(-150, -140)
    # Otra forma de colocar las paredes y los obstaculos era ir creando otros punteros de tal forma que se genere la forma de los obstaculo y partes
    # propuestas y cuando nustra oiton toque a cualquier de esos punteros entonces muere, el proble con este metodo (al menos a mi me pasa) es que
    # cuando se van acomodando los punteros se hace en un tiempo de turtle por tanto se tendria que esperar alrededor de 10 segundos para poder jugar
    # por tabto, decidi hacerlo de la  anetrior manera, dar con las posiciones de los obstaculos y paredes dibujadas por el puntero pared.

    # Si la piton come entonces crece y la manzana aparece en otro lugar
    if piton.distance(manzana) <= 20:
        while True:
            x =  random.randint(-225, 225)
            y = random.randint(-225, 225)
            # con estos dos condicionales nos aseguramos que la las cordenadas de la nueva manzana nunca este sobre las cordenadas de las paredes
            # y obstaculos, por tanto la piton puede comerselas.
            if x <= -195 or x >= 190 or y >= 160 or y <= -190:
                continue
            if ((x >= -195 and x <= -148) and (y >= -80 and y <= -40)) or ((x >= -115 and x <= -60) and (y >= -75 and y <= -40)) or ((x >= -85 and x <= -45) and (y >= -80 and y <= 30)) or ((x >= 50 and x <= 225) and (y <= -48 and y >= -90)) or ((x >= 50 and x <= 90) and (y <= -48 and y >= -125)) or ((x >= -85 and x <= -45) and (y <= 190 and y >= 70)) or ((x >= 65 and x <= 105) and (y <= 190 and y >= 70)):
                continue
            manzana.goto(x, y)
            break
        # creacion de los subcuerpos de la serpiente
        subcuerpo = piton.clone()
        subcuerpo.speed(0)
        subcuerpo.color('light green')
        cuerpo_serpiente.append(subcuerpo)
    
    # este codigo es para que el cuepro del la serpiente tenga movimiento en fila.
    largo_de_la_serpiente = len(cuerpo_serpiente)
    for i in range(largo_de_la_serpiente-1, 0, -1):
        x = cuerpo_serpiente[i-1].xcor()
        y = cuerpo_serpiente[i-1].ycor()
        cuerpo_serpiente[i].goto(x,y)
        
    if largo_de_la_serpiente > 0:
        x = piton.xcor()
        y = piton.ycor()
        cuerpo_serpiente[0].goto(x,y)