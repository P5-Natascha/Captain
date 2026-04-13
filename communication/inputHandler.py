from communication.comms import active_tcp_connection
from comps.motors.motors import vorwaerts

def inputHandler(y):
    if active_tcp_connection:
        if y > 1950:
            movement_y = ((y - 1950) / (4096 - 1950)) * 100
            vorwaerts(movement_y)
