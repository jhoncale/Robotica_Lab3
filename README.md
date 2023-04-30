# Robotica_Lab3


Laboratorio #3 - Robótica de Desarrollo, Intro a ROS

Nombres: Jhon Nelson Cáceres Leal
         Valentina Cruz De Paula
         Oscar Urrego

En la siguiente práctica de laboratorio se tuvo como objetivo principal familiarizarse con ROS, el cual es, un framework para desarrollo de Software de Robots. Todo esto a través del uso de comandos y archivos que hacen posible la conexión de nodos, para llevar a cabo alguna rutina o instrucción dada.

###  ROS y Matlab:


La primera actividad realizada, fue inicializar el nodo maestro (nodo encargado de registrar y ubicar los nodos que ejecutan tareas diferentes), y lanzar una instancia a través de Matlab, es decir, controlar el movimiento de la tortuga enviando un mensaje al Topic de movimiento para que lo lea y lo realice.
Inicialmente, se crea un nodo maestro y un publicador; posteriormente se crea un mensaje y el valor de este. En la siguiente foto, se muestra como el mensaje a enviar toma un valor de x=1, y por ello, la tortuga genera un respectivo movimiento horizontal. 

![image](https://user-images.githubusercontent.com/38961990/235330617-6b434311-2185-4660-8a93-d5f0c3e54787.png)


Posteriormente se hace la subscripción al tópico de pose de la simulación de la tortuga, debido a que es importante primero suscribirse para poder empezar a recibir y leer los mensajes correspondientes. 


![image](https://user-images.githubusercontent.com/38961990/235330627-cd9e307a-6d5c-45a6-a37d-a83d122ab8d9.png)

Con esto, se logra capturar el último mensaje obtenido, indicado en el resultado de la terminal como un vector que posee los datos de la posición en x, en y, y el ángulo theta.
Así mismo, se creó un script que fue mostrando simultáneamente todas las posiciones que adquiría la tortuga, cuando se oprimían las teclas claves del nodo correspondiente. 


![image](https://user-images.githubusercontent.com/38961990/235330636-f004e08f-523a-4780-932c-82745f99b492.png)


Lo anterior, es posible al extraer la última posición con el comando rossuscriber, y mediante un condicional while, ir solicitando en cada momento este dato. Para la impresión de la posición actual, se utilizó un condicional IF dentro del while, el cual se encargaba de comparar las coordenadas de la tortuga, y de esta manera identificar si hubo un cambio de posición.
Por otro lado, el nodo maestro en Matlab se finaliza con el comando ‘rosshutdown’, el cual además de apagarlo, también elimina el nodo global. Es recomendable siempre finalizar el nodo maestro una vez se termine de trabajar con ROS.




###  ROS y Python :

Esta actividad consistía en hacer mover la tortuga con unas letras del teclado. Se obtuvo los siguientes resultados:
Con el siguiente comando, se inicializa el nodo maestro, y como se puede observar aún no tiene ningún nodo registrado. 

![image](https://user-images.githubusercontent.com/38961990/235330656-379721f4-ae71-4dde-88bb-04a414658993.png)



Se crea el siguiente nodo, donde se observará el nuevo código implementado.

![image](https://user-images.githubusercontent.com/38961990/235330662-85735ddb-d570-4e6f-b859-21c50c3496c8.png)


Y posteriormente, se ejecuta un archivo que está dentro de un nodo. Este hace posible el movimiento de la tortuga con las teclas: w, s, a, d, space, r.


![image](https://user-images.githubusercontent.com/38961990/235330667-fb3fc2bf-cccd-4e91-ba7d-fe30b71240c6.png)


Movimiento con la letra ‘W’: se mueve hacia la derecha (adelante), una vez es presionada esta letra. (movement.linear.x =1)


![image](https://user-images.githubusercontent.com/38961990/235330671-8d45760d-ab5c-42b7-b47c-9e3a81c4c7f8.png)

Movimiento con la letra ‘S’: se mueve hacia la izquierda (atrás), una vez es presionada esta letra.
(movement.linear.x = -1)

![image](https://user-images.githubusercontent.com/38961990/235330675-81fb9aae-4151-42c5-8511-07111afdb2a7.png)

Movimiento con la letra ‘D’: se mueve en sentido horario, una vez es presionada esta letra.
(movement.linear.z =-1)

![image](https://user-images.githubusercontent.com/38961990/235330683-c220a37d-3c53-401b-bc8d-8995dd2dbeb1.png)


 Movimiento con la letra ‘A’: se mueve en sentido antihorario, una vez es presionada esta letra.
(movement.linear.z =1)


![image](https://user-images.githubusercontent.com/38961990/235330689-8c126242-06a3-4206-97b4-8b72f95f2b89.png)

Movimiento con la tecla ‘Space’: da un giro de 180°, una vez es presionada esta letra.
(movement.linear.z =pi)


![image](https://user-images.githubusercontent.com/38961990/235330697-c8ca3148-34a3-4332-8f98-d2b5bc73bcc0.png)
Movimiento con la tecla ‘r’: retorna a su posición y orientación central.

Todo lo anterior, se hizo con los comandos movement.linear.x y movement.angular.z, según la instrucción necesaria a seguir. 

###  Descargas:

[lab_3.zip](https://github.com/jhoncale/Robotica_Lab3/files/11360378/lab_3.zip)


