import subprocess
import time

# Define GPIO pins
GPIO_PINS = {"forward": [29, 27], "backward": [28, 26], "left": [29, 26], "right": [28, 27]}

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
    i=0.2
    while i < 1:
        set_pins(GPIO_PINS["forward"], STATE_ON)
        i+=0.2
    # set_pins(GPIO_PINS["backward"], STATE_OFF)

# Function to move backward
def backward():
    i = 0.2
    while i <1:
        set_pins(GPIO_PINS["backward"], STATE_ON)
        # set_pins(GPIO_PINS["forward"], STATE_OFF)
        i+=0.2
# Function to stop
def stop():
    for pins in GPIO_PINS.values():
        set_pins(pins, STATE_OFF)

# Function to turn left
def left():
    local_pins = [29,26]
    for pin in local_pins:
        subprocess.run(["gpio", "write", str(pin), STATE_ON])
        # time.sleep(0.35)
        # subprocess.run(["gpio", "write", str(pin), STATE_OFF])
    time.sleep(0.4)
# Function to turn right
def right():
    local_pins = [28, 27]
    for pin in local_pins:
        subprocess.run(["gpio", "write", str(pin), STATE_ON])
    # set_pins(GPIO_PINS["left"], STATE_OFF)
    time.sleep(0.4)

# Set GPIO pins as outputs
for pins in GPIO_PINS.values():
    for pin in pins:
        subprocess.run(["gpio", "mode", str(pin), "out"])

try:
    while True:
        # Accept user input
        # if i>=1:
        direction = input("Enter direction (F: Forward, B: Backward, L: Left, R: Right): ").upper()
        # i=0.2
        
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
            
            # time.sleep(1)
            # stop()
            # time.sleep(1)
        stop()
except KeyboardInterrupt:
    # Clean up
    stop()
