# Lab_4_Robotica

# Integrantes: 
-Joyner Stiven Caballero Abril.

# Introduccion: 

Este laboratorio tiene como objetivo principal el desarrollo y control de los Joint Controllers para los servomotores Dynamixel AX-12, permitiendo manipular el robot de manera precisa mediante la publicación y suscripción a tópicos de ROS.

El Phantom X Pincher es un manipulador robótico utilizado ampliamente en el ámbito educativo y de investigación debido a su versatilidad y facilidad de integración con diversas plataformas de software. En este laboratorio, se emplearán herramientas como MATLAB y Python para establecer una conexión efectiva con ROS, facilitando el control y la simulación del robot.

A lo largo del laboratorio, se realizarán mediciones de las longitudes de los eslabones del robot y se calcularán los parámetros Denavit-Hartenberg (DH), esenciales para modelar su cinemática. Los scripts desarrollados permitirán el movimiento secuencial de las articulaciones del robot, validando las posiciones simuladas con las obtenidas en el entorno real.

# Objetivos:

• Crear todos los Joint Controllers con ROS para manipular servomotores Dynamixel AX-12 del robot Phantom X Pincher.
• Manipular los tópicos de estado y comando para todos los Joint Controllers del robot Phantom X Pincher.
• Manipular los servicios para todos los Joint Controllers del robot Phantom X Pincher.
• Conectar el robot Phantom X Pincher con MATLAB o Python usando ROS.

# Descripción de la solución planteada:

El primer paso para la elaboración de este laboratorio fue tomar las medidas de los eslabones del robot Phantom X Pincher. Para ello, se midió la distancia de junta a junta utilizando un calibrador. 

L1 = 10.5 cm 
L2 = 10.5 cm 
L3 = 6.5 cm 
L4 = 8 cm 

# Parametros DH del robot Pincher: 

Para construir el modelo del robot Phantom X Pincher, se utilizó la función SerialLink de MATLAB junto con los parámetros Denavit-Hartenberg (DH) obtenidos. Este proceso permitió crear una representación precisa del robot, esencial para la simulación y control. Además, se calculó la matriz de transformación homogénea, que relaciona el sistema de coordenadas global (World) con el sistema de coordenadas del efector final (TCP). Esta matriz es crucial para determinar la posición y orientación del efector final en el espacio de trabajo.

El siguiente diagrama ilustra la estructura y los parámetros DH del robot Phantom X Pincher:

![robot general](https://github.com/JoyS06/Lab_4_Robotica/assets/105253521/efd707a3-7c50-42d8-b07d-d73027750dce)

Para describir el robot utilizando los parámetros Denavit-Hartenberg (DH), se establecieron los siguientes marcos de referencia basados en el diagrama del robot Phantom X Pincher y las distancias medidas entre las articulaciones:

![Sin título](https://github.com/JoyS06/Lab_4_Robotica/assets/105253521/727be210-72d2-4175-bfec-b3cbecc9dfbd)

La tabla con los parametros DH se muestra a continuación:

![image](https://github.com/JoyS06/Lab_4_Robotica/assets/105253521/7faf1ba4-b145-4656-9e21-cd7e3f19a192)

El robot contruido con las herramientas SerialLink de matlab se ve de la siguiente forma:

![image](https://github.com/JoyS06/Lab_4_Robotica/assets/105253521/55ad3220-e4e0-41ac-8aa4-c748c844bd67)

Sin embargo, la pose Home es cuando el robot se encuentra completamente vertical. Por esta razón, la posición inicial del robot se define de la siguiente manera:

# Posición Inicial (Pose Home)
La pose Home se establece con todas las articulaciones alineadas verticalmente, lo que significa que el robot está en una posición completamente extendida y recta. Esta configuración asegura que el robot esté en su posición base y listo para realizar movimientos precisos desde una posición conocida y estable. A continuación, se presenta la configuración inicial para esta pose:

![posicion home](https://github.com/JoyS06/Lab_4_Robotica/assets/105253521/fefda90d-d17d-49ef-9a86-361c6498af2e)

Teniendo en cuenta las diferentes poses requeridas descritas en la siguiente tabla, se presentan las configuraciones articulares correspondientes para cada una de las poses del robot Phantom X Pincher:

![image](https://github.com/JoyS06/Lab_4_Robotica/assets/105253521/402cef20-ade0-442e-9644-741e0ed65d1b)

Se grafican dichas posiciones en el robot hecho en Matlab, tomando en cuenta que la pose home ya la conocemos: 

![image](https://github.com/JoyS06/Lab_4_Robotica/assets/105253521/300e4553-440f-40e5-ad1e-ad575a9c5750)

![image](https://github.com/JoyS06/Lab_4_Robotica/assets/105253521/159efa63-7080-4e46-aa60-5162fa1b94c7)

![image](https://github.com/JoyS06/Lab_4_Robotica/assets/105253521/87cb8fd7-199e-48d7-809e-ad7e96bd4642)

![image](https://github.com/JoyS06/Lab_4_Robotica/assets/105253521/1480fae1-9b3c-4474-a3d2-29a3609a575c)

Primero, se ajusta la configuración de los motores en el archivo de configuración de Dynamixel, proporcionado en la página del curso. En este archivo, se crean los ajustes necesarios para los cinco motores que componen el robot Phantom X Pincher. Una vez creado este archivo, se procede a trabajar con el código en Python, donde se importan las siguientes dependencias:

![image](https://github.com/JoyS06/Lab_4_Robotica/assets/105253521/dbc62ae4-823f-4d82-99f1-ce6fd920dd57)

Para trabajar con ROS en Python, es fundamental importar el módulo rospy, que ofrece las funciones y clases necesarias para interactuar con el sistema ROS. También se utiliza el módulo numpy para realizar cálculos numéricos y operaciones matriciales eficientemente. Además, se requieren tópicos y mensajes específicos de ROS como JointTrajectory, que representa una secuencia de posiciones y velocidades de las articulaciones.

# Descripción de la Función joint_publisher
La función joint_publisher es responsable de crear un objeto Publisher que publica en el tópico joint_trajectory, utilizado por el controlador del brazo robótico. La función se inicializa con:

![image](https://github.com/JoyS06/Lab_4_Robotica/assets/105253521/6b676ab3-7446-48d0-872c-ad44e738fa79)

Dentro de un bucle que se ejecuta mientras ROS esté activo rospy.is_shutdown(), la función:

Crea un objeto JointTrajectory
Define un punto de trayectoria JointTrajectoryPoint
Publica el estado en el tópico

Esta función, aunque originalmente usada para pruebas, ilustra cómo enviar comandos de trayectoria a los motores del robot. No se utiliza en la implementación principal del programa, pero es crucial para entender cómo interactuar con el controlador del brazo robótico en ROS.

Este código en Python utiliza las funciones callback y listener para trabajar con los datos de los servomotores del robot.

# Descripción de las Funciones:

Inicialización del Nodo ROS:

listener inicializa el nodo de ROS, representando el script de Python dentro del entorno de ROS, permitiendo la comunicación con otros nodos.
Suscripción al Tópico:

listener se suscribe al tópico /dynamixel_workbench/joint_states para recibir los estados de las articulaciones del robot, usando JointState para procesar los mensajes.
Procesamiento de Datos:

La función callback convierte los datos de posición de las articulaciones de radianes a grados, almacenándolos en la variable global PosActual. Esto facilita el uso de estos datos fuera de la función callback.

Este enfoque asegura que los datos de las articulaciones del robot sean accesibles y utilizables en cualquier parte del programa, proporcionando una base sólida para controlar y monitorear el robot

![image](https://github.com/JoyS06/Lab_4_Robotica/assets/105253521/3cb7f986-c2f4-4683-a09d-97bab3dd3ab5)

La función jointCommand envía comandos a un motor Dynamixel a través de un servicio ROS. Primero, espera a que el servicio dynamixel_command esté disponible. Luego, crea un ServiceProxy para enviar el comando, que incluye el tipo de comando, el identificador del motor, el nombre de la dirección de memoria y el nuevo valor a escribir. Tras enviar el comando, la función espera el tiempo especificado y devuelve el resultado del comando. Si ocurre un error durante la transmisión, la excepción se captura y se imprime.

Inicialización y Espera del Servicio: La función espera a que el servicio dynamixel_command esté disponible.

Envía el Comando: Utiliza ServiceProxy para enviar el comando al motor, especificando el tipo de comando, identificador del motor, dirección de memoria y nuevo valor.

Espera y Retorno del Resultado: Tras enviar el comando, espera el tiempo especificado y devuelve el resultado. En caso de error, imprime la excepción.

![image](https://github.com/JoyS06/Lab_4_Robotica/assets/105253521/1d1e4fde-ffc1-4640-92b3-b3f9652f52b7)

Al ejecutar el archivo desde la terminal, se activa la función listener para inicializar el nodo de ROS y recibir datos de los motores. Luego, se definen listas de posiciones en valores de bits y en grados para las articulaciones del robot. Estas posiciones se almacenan en una lista de listas, que se muestra al usuario en grados para facilitar la comprensión y uso.

![image](https://github.com/JoyS06/Lab_4_Robotica/assets/105253521/99482779-388d-408b-a84a-54f32ca2e945)







