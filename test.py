import speech_recognition as sr
import random
from moves import *
# Function to perform a random movement
def random_movement():
    random_direction = random.randint(0, 3)
    if random_direction == 0:
        forward()
    elif random_direction == 1:
        backward()
    elif random_direction == 2:
        left()
    elif random_direction == 3:
        right()

# Function to listen for voice commands
def listen_for_command():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Listening for command...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)  # Listen to microphone input

    try:
        print("Processing...")
        command = recognizer.recognize_google(audio).lower()  # Use Google Speech Recognition to transcribe audio
        print("Command:", command)
        return command
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")
        return None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None
try:
    while True:
        # Accept user input via voice command
        command = listen_for_command()

        # Call corresponding function based on user input
        if command == "forward":
            forward()
        elif command == "backward":
            backward()
        elif command == "left":
            left()
        elif command == "right":
            right()
        elif command == "random":
            random_movement()
        else:
            print("Invalid command. Please try again.")

        time.sleep(1)
        stop()
        time.sleep(1)

except KeyboardInterrupt:
    # Clean up
    stop()