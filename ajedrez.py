#importación de la librería
import turtle 
import time #permite pausar la aplicación al final por un timpo determinado

#definir las características de la ventana
vent=turtle.Screen()
vent.bgcolor('brown') # color de fondo de la ventana
vent.title('Tablero de Ajedrez') #titulo de la aplicación

greg=turtle.Turtle()
greg.speed(20) #velocidad con la que dibuja en el tablero

#dibujar y llenar un cuadro
def cuadro(tamaño,alternar,color):
	greg.color(color)
	greg.begin_fill()
	for i in range(4):
		greg.fd(tamaño)
		greg.lt(90)
	greg.end_fill()
	greg.fd(tamaño)