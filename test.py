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
# def listen_for_command():
#     recognizer = sr.Recognizer()
#     microphone = sr.Microphone()

#     with microphone as source:
#         print("Listening for command...")
#         recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
#         audio = recognizer.listen(source)  # Listen to microphone input

#     try:
#         print("Processing...")
#         command = recognizer.recognize_google(audio).lower()  # Use Google Speech Recognition to transcribe audio
#         print("Command:", command)
#         return command
#     except sr.UnknownValueError:
#         print("Sorry, I couldn't understand the audio.")
#         return None
#     except sr.RequestError as e:
#         print("Could not request results from Google Speech Recognition service; {0}".format(e))
#         return None
    

# def stt(languageCode):
#     lang_code = languageCode
#     # Create a recognizer object
#     r = sr.Recognizer()

#     # Open the microphone for capturing the speech
#     with sr.Microphone() as source:
#         print("Listening...")   
        
#         # Adjust the energy threshold for silence detection
#         r.energy_threshold = 4000

#         # Listen for speech and convert it to text
#         audio = r.listen(source)

#         try:

#             text = r.recognize_google(audio, language=lang_code)
#             print("You said:", text)

        
#         except sr.UnknownValueError:
#             x = 'Not Understand'
#             # x = stt(languageCode)
#             return x

            
#         except sr.RequestError as e:
#             text="Could not request results from Google Speech Recognition service; {0}".format(e)
#             print(text)
#             # self.open_mic()
#         return text
    
# Python program to translate
# speech to text and text to speech


import speech_recognition as sr
import pyttsx3 

# Initialize the recognizer 
r = sr.Recognizer() 

# Function to convert text to
# speech
def SpeakText(command):
	
	# Initialize the engine
	engine = pyttsx3.init()
	engine.say(command) 
	engine.runAndWait()
	
	
# Loop infinitely for user to
# speak
def stt():
# while(1): 
	
	# Exception handling to handle
	# exceptions at the runtime
	try:
		
		# use the microphone as source for input.
		with sr.Microphone() as source2:
			
			# wait for a second to let the recognizer
			# adjust the energy threshold based on
			# the surrounding noise level 
			r.adjust_for_ambient_noise(source2, duration=0.2)
			
			#listens for the user's input 
			audio2 = r.listen(source2)
			
			# Using google to recognize audio
			MyText = r.recognize_google(audio2)
			MyText = MyText.lower()

			print("Did you say ",MyText)
			SpeakText(MyText)
			
	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))
		
	except sr.UnknownValueError:
		print("unknown error occurred")
    
    




try:
    while True:
        # Accept user input via voice command
        # command = listen_for_command()
        command = stt()

        # Check various conditions based on words in the command
        if "forward" in command:
            forward()
        elif "backward" in command:
            backward()
        elif "left" in command:
            left()
        elif "right" in command:
            right()
        elif "random" in command:
            random_movement()
        else:
            print("Invalid command. Please try again.")

        time.sleep(1)
        stop()
        time.sleep(1)

except KeyboardInterrupt:
    # Clean up
    stop()

