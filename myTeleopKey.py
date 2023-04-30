import curses
import rospy
import math
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

# inicializar nodo de ROS
rospy.init_node('turtlesim_keyboard_control')

# crear un publicador para los comandos de movimiento
pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

# inicializar objeto Twist para los comandos de movimiento
movement = Twist()

# posición central de la pantalla
CENTER_X = 5.5
CENTER_Y = 5.5

# función para manejar la tecla presionada
def _key_pressed(keycode):
    # obtener la posición actual de la tortuga
    pose = rospy.wait_for_message('/turtle1/pose', Pose)

    # definir los movimientos de acuerdo a las teclas presionadas
    if keycode == ord('w'):
        movement.linear.x = 1.0    # mover hacia adelante
        movement.angular.z = 0.0
    elif keycode == ord('s'):
        movement.linear.x = -1.0   # mover hacia atrás
        movement.angular.z = 0.0
    elif keycode == ord('d'):
        movement.angular.z = -1.0  # girar en sentido horario
        movement.linear.x = 0.0 
        movement.linear.y = 0.0 
    elif keycode == ord('a'):
        movement.angular.z = 1.0   # girar en sentido antihorario
        movement.linear.x = 0.0 
        movement.linear.y = 0.0 
    elif keycode == ord('r'):
        # calcular la distancia a mover en cada eje
        delta_x = CENTER_X - pose.x
        delta_y = CENTER_Y - pose.y

        # calcular el ángulo de orientación hacia la derecha
        target_angle = math.atan2(delta_y, delta_x)

        # ajustar la orientación actual de la tortuga hacia la derecha
        delta_angle = target_angle - pose.theta
        if delta_angle > math.pi:
            delta_angle -= 2 * math.pi
        elif delta_angle < -math.pi:
            delta_angle += 2 * math.pi
        movement.angular.z = delta_angle

        # mover la tortuga hacia el centro de la pantalla
        movement.linear.x = math.sqrt(delta_x**2 + delta_y**2)
        
        
    elif keycode == ord(' '):
    
        # girar 180 grados sin cambiar de posición
        movement.linear.x = 0.0 
        movement.linear.y = 0.0 
        movement.angular.z = math.pi
    else: 
    	return
    # publicar los comandos de movimiento
    pub.publish(movement)

# configurar la pantalla de curses
screen = curses.initscr()
curses.cbreak()
screen.keypad(True)

# capturar las teclas presionadas hasta que se presione la tecla 'q'
while True:
    keycode = screen.getch()
    if keycode == ord('q'):
        break
    else:
        _key_pressed(keycode)

# liberar la pantalla de curses y detener el nodo de ROS
curses.nocbreak()
screen.keypad(False)
curses.echo()
curses.endwin()
rospy.signal_shutdown('Keyboard interrupt')
