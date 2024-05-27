import speech_recognition as sr
import random
import requests
import threading
import time
from moves import *
from gttsvoice import play_and_delete, text_to_speech



url = "http://192.168.1.158:3000/chat"

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
            print("Analyzing")
            text = r.recognize_google(audio, language=lang_code)
            print("You said:", text)

        except sr.UnknownValueError:
            text = 'Not Understand'
            return text

        except sr.RequestError as e:
            text = "Could not request results from Google Speech Recognition service; {0}".format(e)
            print(text)
            return text

        return text.lower()

def handle_tts(text):
    filename = text_to_speech(text)
    if filename:
        play_and_delete(filename)

try:
    while True:
        # Accept user input via voice command
        command = stt()
        payload = {
            "success": True,
            "message": command,
            "language": "en"
        }
        response = requests.post(url=url, json=payload)
        response = response.json()

        # Read the text
        print(response)

        # Create and start a thread for the TTS operation
        tts_thread = threading.Thread(target=handle_tts, args=(response['text'],))
        tts_thread.start()

        # Check various conditions based on words in the command
        if response['intent'] == "move_forward":
            forward()
        elif response['intent'] == "move_back":
            backward()
        elif response['intent'] == "move_left":
            left()
        elif response['intent'] == "move_right":
            right()
        elif response['intent'] == "move_random":
            random_movement()
        else:
            print("Invalid command. Please try again.")
            random_movement()

        # Wait for the TTS thread to finish before stopping the robot
        tts_thread.join()

        time.sleep(1)
        stop()
        time.sleep(1)

except KeyboardInterrupt:
    # Clean up
    stop()
