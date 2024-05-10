import subprocess
import time

# Define GPIO pin and state
GPIO_PIN = 27
STATE_ON = "1"
STATE_OFF = "0"
subprocess.run(["gpio", "mode", str(GPIO_PIN), "out"])

try:
    while True:
        # Turn on GPIO pin
        subprocess.run(["gpio", "write", str(GPIO_PIN), STATE_ON])
        time.sleep(1)
        
        # Turn off GPIO pin
        subprocess.run(["gpio", "write", str(GPIO_PIN), STATE_OFF])
        time.sleep(1)

except KeyboardInterrupt:
    # Clean up
    subprocess.run(["gpio", "write", str(GPIO_PIN), STATE_OFF])
