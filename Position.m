% Inicializar el nodo ROS
rosinit;

while true 
    % Crear un objeto de suscriptor ROS
    sub = rossubscriber('/turtle1/pose', 'turtlesim/Pose')
end
% Esperar un tiempo para asegurar la conexión con el tópico
pause(1);

% Obtener la última pose publicada en el tópico
pose = sub.LatestMessage;

% Acceder a los campos de la pose
x = pose.X;
y = pose.Y;
theta = pose.Theta;

% Apagar el nodo ROS
%rosshutdown;