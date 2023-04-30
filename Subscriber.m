% Inicializar el nodo de ROS en MATLAB
rosinit

% Suscribirse al topic de posición del robot
pos_sub = rossubscriber('/turtle1/pose');

% Inicializar variables de posición anterior
prev_pos_x = 0;
prev_pos_y = 0;
prev_pos_theta = 0;

while pos_sub ~= 0
    
    % Esperar hasta que se reciba un mensaje de posición
    pos_msg = receive(pos_sub);
    
    % Extraer la información de posición del mensaje
    pos_x = pos_msg.X;
    pos_y = pos_msg.Y;
    pos_theta = pos_msg.Theta;
   
    % Verificar si ha cambiado la posición
    if pos_x ~= prev_pos_x || pos_y ~= prev_pos_y || pos_theta ~= prev_pos_theta
        
        % Actualizar variables de posición anterior
        prev_pos_x = pos_x;
        prev_pos_y = pos_y;
        prev_pos_theta = pos_theta;
        
        % Imprimir la información de posición actualizada
        disp(['La posición actual de Turtle1 es: (', num2str(pos_x), ', ', num2str(pos_y), ', ', num2str(pos_theta), ')']);
    end

end
