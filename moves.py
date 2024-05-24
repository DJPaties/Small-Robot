import subprocess
import time

# Define GPIO pins
GPIO_PINS = {"forward": [29, 27], "backward": [26, 28], "left": [29, 26], "right": [28, 27]}

# Define states
STATE_ON = "1"
STATE_OFF = "0"

# Function to set GPIO pins states
def set_pins(pins, state):
    
    for pin in pins:
        subprocess.run(["gpio", "write", str(pin), state])
        time.sleep(0.35)
        subprocess.run(["gpio", "write", str(pin), STATE_OFF])


# Function to move forward
def forward():
    set_pins(GPIO_PINS["forward"], STATE_ON)
    # set_pins(GPIO_PINS["backward"], STATE_OFF)

# Function to move backward
def backward():
    local_pins = ["28,26"]
    for pin in local_pins:
        subprocess.run(["gpio", "write", str(pin), STATE_ON])
        time.sleep(0.35)
        subprocess.run(["gpio", "write", str(pin), STATE_OFF])
    # set_pins(GPIO_PINS["backward"], STATE_ON)
    # set_pins(GPIO_PINS["forward"], STATE_OFF)

# Function to stop
def stop():
    for pins in GPIO_PINS.values():
        set_pins(pins, STATE_OFF)

# Function to turn left
def left():
    set_pins(GPIO_PINS["left"], STATE_ON)
    set_pins(GPIO_PINS["right"], STATE_OFF)

# Function to turn right
def right():
    set_pins(GPIO_PINS["right"], STATE_ON)
    set_pins(GPIO_PINS["left"], STATE_OFF)

# Set GPIO pins as outputs
for pins in GPIO_PINS.values():
    for pin in pins:
        subprocess.run(["gpio", "mode", str(pin), "out"])

try:
    while True:
        # Accept user input
        direction = input("Enter direction (F: Forward, B: Backward, L: Left, R: Right): ").upper()
        i=0.2
        while i < 1:
            # Call corresponding function based on user input
            if direction == "F":
                forward()
            elif direction == "B":
                backward()
            elif direction == "L":
                left()
            elif direction == "R":
                right()
            else:
                print("Invalid input. Please enter F, B, L, or R.")
            i+=0.2
            # time.sleep(1)
            # stop()
            # time.sleep(1)
        stop()
except KeyboardInterrupt:
    # Clean up
    stop()
