import wiringpi as wp
import time

# Set GPIO pin numbering mode
wp.wiringPiSetupGpio()

# Define LED pin
LED_PIN = 27

# Set pin mode to output
wp.pinMode(LED_PIN, wp.OUTPUT)

try:
    while True:
        # Toggle LED
        wp.digitalWrite(LED_PIN, wp.HIGH)
        time.sleep(1)
        wp.digitalWrite(LED_PIN, wp.LOW)
        time.sleep(1)
except KeyboardInterrupt:
    # Clean up
    wp.pinMode(LED_PIN, wp.INPUT)
