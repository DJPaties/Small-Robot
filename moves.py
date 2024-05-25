import subprocess
import time
import random

# Setting GPIO PINS for movement
GPIO_PINS = {"forward": [29, 27], "backward": [28, 26], "left": [29, 26], "right": [28, 27]}

# Define states
STATE_ON = "1"
STATE_OFF = "0"

# Function to set GPIO pins states
def set_pins(pins, state, delay=0.35):
    for pin in pins:
        subprocess.run(["gpio", "write", str(pin), state])
        time.sleep(delay)
        subprocess.run(["gpio", "write", str(pin), STATE_OFF])
        
    for pin in pins:
        subprocess.run(["gpio", "write", str(pin), STATE_OFF])

# Function to move forward
def forward(delay=0.35):
    i = 0.2
    while i<1:
        set_pins(GPIO_PINS["forward"], STATE_ON, delay)
        i+=0.2
# Function to move backward
def backward(delay=0.35):
    i = 0.2
    while i<1:
        set_pins(GPIO_PINS["backward"], STATE_ON, delay)
        i+=0.2
# Function to turn left
def left(delay=0.4):
    set_pins(GPIO_PINS["left"], STATE_ON, delay)

# Function to turn right
def right(delay=0.4):
    set_pins(GPIO_PINS["right"], STATE_ON, delay)

# Function to stop
def stop():
    for pins in GPIO_PINS.values():
        for pin in pins:
            subprocess.run(["gpio", "write", str(pin), STATE_OFF])

# Function to perform a random movement
def random_movement(delay=1.5):
    random_direction = random.randint(0, 1)
    i = 0
    while i<delay: 
        print(random_direction)
        if random_direction == 0:
            forward()
            stop()
            print("Forward Done")
            left(0.2)
            stop()
            print("Left Done")
            right(0.2)
            stop()
            print("Right Done")
        elif random_direction == 1:
            forward()
            stop()
            print("Forward Done")
            left()
            stop()
            print("Left Done")
            right()
            stop()
            print("Right Done")
        i+=1
# Set GPIO pins as outputs
for pins in GPIO_PINS.values():
    for pin in pins:
        subprocess.run(["gpio", "mode", str(pin), "out"])

try:
    while True:
        direction = input("Enter direction (F: Forward, B: Backward, L: Left, R: Right, M: Random Movement): ").upper()
        if direction == "F":
            forward()
        elif direction == "B":
            backward()
        elif direction == "L":
            left()
        elif direction == "R":
            right()
        elif direction == "M":
            random_movement()
        else:
            print("Invalid input. Please enter F, B, L, R, or M.")
        stop()
except KeyboardInterrupt:
    stop()
