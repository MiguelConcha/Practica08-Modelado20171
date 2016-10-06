# Practica08-Modelado20171

![roku-channel-reviews-snake](https://cloud.githubusercontent.com/assets/13952922/19173187/a91260b6-8beb-11e6-88f4-bfd09a3284a1.jpg)

Dos interfaces fueron creadas: cliente.ui y servidor.ui. La última se encarga de llevar a cabo la actualización constante del juego de snake, permitir incrementar el número de celdas del juego, facilitar el movimiento de la serpiente, etc. Por otro lado, la ventana del cliente será usada para mostrar al usuario el estado de su víbora realizando peticiones al servidor cada cierto tiempo. 

Algunas de las herramientas empleadas de QtDesigner fueron:

* Label

* Push Button

* Table Widget

* Group Box

* Widget

* Spin Box

* Line Edit

* Layouts:
 * Vertical
 * Horizontal
 * Grid
 
Para lograr que las celdas de la tabla ocuparan todo el espacio disponible del QTableWidget de manera dimámica sin importar las dimensiones de las dos ventanas, se empleó la función setResizeMode() de los encabezados de las columnas y las filas, luego de haber especificado el valor mínimo de los mismos en QtDesigner.

Finalmente, se creó un QTimer para poder efectuar la operación de verificación del número de renglones y columnas en el TableWidget cada cierto intervalo del tiempo definido por otro contador para permitir de esta manera la inserción de nuevas celdas por parte del usuario del servidor. 
