import pyfirmata
import time

# get the board
board = pyfirmata.Arduino('COM4')

# iterator to get input
it = pyfirmata.util.Iterator(board)
it.start()

# components
potentiometer = board.get_pin('a:0:i')
button = board.get_pin("d:2:i")
led = board.get_pin('d:11:p')

while True:
    potentiometerValue = potentiometer.read()
    if potentiometerValue is not None:
        led.write(potentiometerValue)
    if button.read():
        led.write(1)
    time.sleep(0.1)