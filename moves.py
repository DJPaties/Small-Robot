import subprocess
import time
import random
#Setting GPIO PINS for movement
GPIO_PINS = {"forward": [29, 27], "backward": [28, 26], "left": [29, 26], "right": [28, 27]}

# Define states
STATE_ON = "1"
STATE_OFF = "0"

# Function to set GPIO pins states
def set_pins(pins, state,delay=0.35):
    
    for pin in pins:
        subprocess.run(["gpio", "write", str(pin), state])
        time.sleep(delay)
        subprocess.run(["gpio", "write", str(pin), STATE_OFF])
    time.sleep(0.1)

    for pin in pins:
        # set_pins(pins, STATE_OFF)
        subprocess.run(["gpio", "write", str(pins), STATE_OFF])
# Function to move forward
def forward(delay=0.35):
    i=0.2
    while i < 1:
        set_pins(GPIO_PINS["forward"], STATE_ON,delay)
        i+=0.2
    # set_pins(GPIO_PINS["backward"], STATE_OFF)

# Function to move backward
def backward(delay=0.35):
    i = 0.2
    while i <1:
        set_pins(GPIO_PINS["backward"], STATE_ON,delay)
        # set_pins(GPIO_PINS["forward"], STATE_OFF)
        i+=0.2
# Function to stop
def stop():
    for pins in GPIO_PINS.values():
        # set_pins(pins, STATE_OFF)
        subprocess.run(["gpio", "write", str(pins), STATE_OFF])

# Function to turn left
def left(delay=0.4):
    local_pins = [29,26]
    for pin in local_pins:
        subprocess.run(["gpio", "write", str(pin), STATE_ON])
        # time.sleep(0.35)
        # subprocess.run(["gpio", "write", str(pin), STATE_OFF])
    time.sleep(delay)
# Function to turn right
def right(delay=0.4):
    local_pins = [28, 27]
    for pin in local_pins:
        subprocess.run(["gpio", "write", str(pin), STATE_ON])
    # set_pins(GPIO_PINS["left"], STATE_OFF)
    time.sleep(delay)

# Function to perform a random movement
def random_movement():
    random_direction = random.randint(0, 1)
    print(random_direction)
    if random_direction == 0:
        forward()
        stop()
        print("Forward Done")
        left(0.2)
        stop()
        print("left Done")
        right(0.2)
        stop()
        print("right Done")
        # backward()
        # stop()
        # print("backward Done")

    elif random_direction == 1:
        # left(0.2)
        # stop()
        # right(0.2)
        # stop()
        # left(0.2)
        # stop()
        # right(0.2)
        # stop()
        forward()
        stop()
        print("Forward Done")
        left()
        stop()
        print("left Done")
        right(
            
        )
        stop()
        print("right Done")
        # backward()
        # stop()
        # print("backward Done")


    # elif random_direction == 2:
    #     left()
    # elif random_direction == 3:
    #     right()





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
        elif direction == "M":
            random_movement()
        else:
            print("Invalid input. Please enter F, B, L, or R.")
            stop()
            
            
        stop()
except KeyboardInterrupt:
    # Clean up
    stop()
