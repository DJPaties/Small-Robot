import speech_recognition as sr
import random
import requests
from moves import *
import pyttsx3
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


url = "http://192.168.1.158:3000/chat"
engine = pyttsx3.init()


def stt(languageCode="en-US"):
    lang_code = languageCode
    # Create a recognizer object
    r = sr.Recognizer()

    # Open the microphone for capturing the speech
    with sr.Microphone() as source:
        print("Listening...")   
        
        # Adjust the energy threshold for silence detection
        r.energy_threshold = 4000

        # Listen for speech and convert it to text
        audio = r.listen(source)

        try:
            print("analying")
            text = r.recognize_google(audio, language=lang_code)
            print("You said:", text)

        
        except sr.UnknownValueError:
            text = 'Not Understand'
            # x = stt(languageCode)
            return text

            
        except sr.RequestError as e:
            text="Could not request results from Google Speech Recognition service; {0}".format(e)
            print(text)
            # self.open_mic()
        return text.lower()
    
    
try:
    while True:
        # Accept user input via voice command
        # command = listen_for_command()
        command = stt()
        payload = {
    "success": True,
    "message":command,
    "language":"en"

}
        response = requests.post(url=url,json=payload)
        response = response.json()
        # Check various conditions based on words in the command
        # Read the text
        engine.say(response[['text']])

        # Start the engine and wait until it finishes speaking
        engine.runAndWait()
        if "forward" == response['intent'] :
            forward()
        elif "backward"  == response['intent']:
            backward()
        elif "left"  == response['intent']:
            left()
        elif "right" == response['intent']:
            right()
        elif "random"  == response['intent']:
            random_movement()
        else:
            print("Invalid command. Please try again.")

        time.sleep(1)
        stop()
        time.sleep(1)

except KeyboardInterrupt:
    # Clean up
    stop()

