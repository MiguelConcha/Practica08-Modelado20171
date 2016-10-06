import sys
from PyQt4 import QtGui, QtCore, uic

class VentanaServidor(QtGui.QMainWindow):
    def __init__(self):
    	'''
    	Constructor de la ventana principal del servidor mismo que se 
    	encarga de llevar a cabo la acción del juego y mandar el estado del mismo
    	a la ventana del cliente.
    	'''
    	super(VentanaServidor, self).__init__() #Se crea la ventana del servidor.
    	uic.loadUi('servidor.ui', self)
    	self.espera = 0 #Esta será la espera del cliente y qué tan rápido se actualiza el juego. Por ahora creé un método dummy para probarlo.
    	self.expandir_cuadros_tabla() #Especificando que las celdas tienen que cubrir el tamaño del QTableWidget.
    	self.crear_contadores() #Crea los contadores de la ventana.
    	self.show() #Se muestra la vetana.

    def crear_contadores(self):
    	'''
    	Crea dos contadores: el principal, mismo que nos dice qué tan rápido se tiene que actualizar
    	el juego y el intervalo de respuesta al cliente; el segundo sirve para determinar
    	cada cuánto se tiene que checar el número de celdas en el QTableWidget.
    	'''
    	self.timer = QtCore.QTimer(self) #Se crea el contador.
    	self.timer.timeout.connect(self.actualizar_tabla) #Se asocia con una función.
    	self.timer.start(500) #Se especifica el intervalo.
    	self.main_timer = QtCore.QTimer(self) #Análogamente para el segundo.
    	self.main_timer.timeout.connect(self.checar_timeout)
    	self.main_timer.start(500)

    def checar_timeout(self):
    	'''
    	Función que sirve para estar fijando el tiempo de espera del contador
    	principal. Para este propósito extramos el valor que está presente en el 
    	spinBox correspondiente.
    	'''
    	self.espera = self.spinBox.value()
    	self.timer.setInterval(self.espera) #Fijamos el nuevo intervalo del timer de la tabla.

    def expandir_cuadros_tabla(self):
    	'''
        Función encargada de lograr que las celdas del TableWidget de expandan
        dinámicamente para ajustarse a las dimensiones del mismo sin importar 
        que cambien las dimensiones de la ventana princiapal del cliente.
        Se especifica --para las filas y columnas-- que pueden expandirse para llenar
        el espacio del tableWidget y ésto lo hacen de forma uniforme considerando el tamaño
        total y el número de celdas para ajustar su tamaño. El tamaño mínimo
        de los encabezados respectivos fue establecido para que tuviera como mínimo un pixel.
        '''
    	self.tableWidget.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
    	self.tableWidget.verticalHeader().setResizeMode(QtGui.QHeaderView.Stretch)

    def actualizar_tabla(self):
    	'''
    	Función que permite incrementar el número de filas y columnas de la tabla.
    	'''
    	num_filas = self.spinBox_3.value() #Extraemos los valores de los spinboxes.
    	num_columnas = self.spinBox_2.value()
    	self.tableWidget.setRowCount(num_filas)  #Y fijamos el número de columnas/celdas para adaptarse al ńuevo número.
    	self.tableWidget.setColumnCount(num_columnas)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv) #Creando la aplicación.
    ventana = VentanaServidor() #Ya con la aplicación creada, podemos crear un objeto del tipo ventana principal de tipo cliente.
    sys.exit(app.exec_()) #Y continúa la ejecución en tanto que no se considere lo contrario.
